from flask import Flask
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="postgres://kmtbyuctjqttfv:cc90a7f1245bfd6fd8b269ab62c492bc2496ba4693def1c7041a6caf23d3f8d0@ec2-107-20-239-47.compute-1.amazonaws.com:5432/d5053esn9ed62c"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
