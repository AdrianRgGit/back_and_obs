from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'public/videos/'


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/video')
def video_page():
    return render_template("video.html")

@app.route('/image')
def image_page():
    return render_template("image.html")

@app.route('/gif')
def gif_page():
    return render_template("gif.html")

@app.route('/video/<filename>')
def video_route(filename):
    return send_from_directory('public/videos', filename)

@app.route('/image/<filename>')
def image(filename):
    return send_from_directory('public/images', filename)

@app.route('/gif/<filename>')
def gif(filename):
    return send_from_directory('public/gifs', filename)


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    new_filename = "video_prueba.mp4"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
    return 'Archivo subido exitosamente'

if __name__ == '__main__':
    app.run(debug=True)
