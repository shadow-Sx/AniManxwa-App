from mega import Mega
from flask import Flask, send_file

app = Flask(__name__)

mega = Mega()
m = mega.login('email@mega.nz', 'parolingiz')

@app.route('/<manga>/<bob>/<sahifa>')
def manga(manga, bob, sahifa):
    fayl = m.find(f'Mangas/{manga}/chapter_{bob}/{sahifa}.jpg')
    return send_file(m.download(fayl), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run()
