from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import shutil

app = Flask(__name__)

MUSIC_FOLDER = 'static/music'
TRASH_FOLDER = 'static/trash'
CURRENT_FILE = 'current_song.txt'

def get_songs():
    return sorted(os.listdir(MUSIC_FOLDER))

def get_trash():
    return sorted(os.listdir(TRASH_FOLDER))

def get_current_song():
    if os.path.exists(CURRENT_FILE):
        with open(CURRENT_FILE, 'r') as f:
            return f.read().strip()
    return ""

def save_current_song(song):
    with open(CURRENT_FILE, 'w') as f:
        f.write(song)

@app.route('/')
def index():
    songs = get_songs()
    current = get_current_song()
    trash = get_trash()
    return render_template('index.html', songs=songs, current=current, trash=trash)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    position = request.form.get('position')
    if file:
        filepath = os.path.join(MUSIC_FOLDER, file.filename)
        file.save(filepath)

        if position:
            position = int(position) - 1
            songs = get_songs()
            songs.remove(file.filename)
            songs.insert(position, file.filename)
            # Reorganiza las canciones (solo cambia el orden en la carpeta)
            for idx, song in enumerate(songs):
                os.rename(os.path.join(MUSIC_FOLDER, song), os.path.join(MUSIC_FOLDER, f"temp_{idx}_{song}"))
            for temp_file in os.listdir(MUSIC_FOLDER):
                if temp_file.startswith("temp_"):
                    new_name = "_".join(temp_file.split('_')[2:])
                    os.rename(os.path.join(MUSIC_FOLDER, temp_file), os.path.join(MUSIC_FOLDER, new_name))
    return redirect(url_for('index'))

@app.route('/delete/<song>')
def delete(song):
    src = os.path.join(MUSIC_FOLDER, song)
    dst = os.path.join(TRASH_FOLDER, song)
    if os.path.exists(src):
        shutil.move(src, dst)
    return redirect(url_for('index'))

@app.route('/recover/<song>')
def recover(song):
    src = os.path.join(TRASH_FOLDER, song)
    dst = os.path.join(MUSIC_FOLDER, song)
    if os.path.exists(src):
        shutil.move(src, dst)
    return redirect(url_for('index'))

@app.route('/delete_permanently/<song>')
def delete_permanently(song):
    trash_path = os.path.join(TRASH_FOLDER, song)
    if os.path.exists(trash_path):
        os.remove(trash_path)
    return redirect(url_for('index'))

@app.route('/set_current/<song>')
def set_current(song):
    save_current_song(song)
    return '', 204

@app.route('/next')
def next_song():
    songs = get_songs()
    current = get_current_song()
    if current in songs:
        idx = songs.index(current)
        next_idx = (idx + 1) % len(songs)
        next_song = songs[next_idx]
        save_current_song(next_song)
        return jsonify({'song': next_song})
    elif songs:
        save_current_song(songs[0])
        return jsonify({'song': songs[0]})
    return jsonify({'song': None})

@app.route('/previous')
def previous_song():
    songs = get_songs()
    current = get_current_song()
    if current in songs:
        idx = songs.index(current)
        prev_idx = (idx - 1) % len(songs)
        prev_song = songs[prev_idx]
        save_current_song(prev_song)
        return jsonify({'song': prev_song})
    elif songs:
        save_current_song(songs[0])
        return jsonify({'song': songs[0]})
    return jsonify({'song': None})

if __name__ == '__main__':
    os.makedirs(MUSIC_FOLDER, exist_ok=True)
    os.makedirs(TRASH_FOLDER, exist_ok=True)
    app.run(debug=True)
