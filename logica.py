from flask import Flask, request, render_template
from pytube import YouTube


app = Flask("logica de programacion")

@app.route("/")
def hello_world():
    return render_template("main.html")


@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        link = request.form['youtube_link']
        try:
            yt = YouTube(link)
            yt = yt.streams.get_highest_resolution()
            yt.download()
            message = "¡Descarga completada con éxito!"
        except Exception as e:
            message = f"Hubo un error al descargar el video del URL proporcionado: {str(e)}"
        return render_template('main.html', message=message)
    


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port= '5000')