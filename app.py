from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
<<<<<<< HEAD
    return "<h1>Hello! My name is  Ahmad Dagher. Google Cloud Architect! As a Professional service engineer, I am tasked with designing and
implementing strong, flexible systems that will adapt to the different needs of
businesses. In particular, I have concentrated on Google Cloud Architecture
and helped companies migrate by optimizing the platform using Google
Cloud.</h1>"
=======
    return "<h1>Hello! My name is  Ahmad Dagher. Google Cloud Architect </h1>"
>>>>>>> ssh-origin/master

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

