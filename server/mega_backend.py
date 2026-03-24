from mega import Mega
from flask import Flask, send_file

app = Flask(__name__)

# Mega.nz ga ulanish
mega = Mega()
m = mega.login('email@mega.nz', 'parolingiz')

@app.route('/rasm/<manga_id>/<bob>//<sahifa>')
def rasm_olish(manga_id, bob, sahifa):
    # Mega.nz dan rasmni topib yuborish
    rasm_yoli = f'Mangas/{manga_id}/chapter_{bob}/{sahifa}.jpg'
    fayl = m.find(rasm_yoli)
    return send_file(m.download(fayl), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run()
