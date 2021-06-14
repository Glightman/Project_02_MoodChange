from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    name_player = 'Emoções'
    award = True
    return render_template(
        'index.html',
        name_player = name_player,
        award = award
    )

if __name__ == "__main__":
    app.run(debug=True)