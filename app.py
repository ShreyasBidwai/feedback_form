from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Feedback

app = Flask(__name__)

# Update your username and password
DATABASE_URL = "mysql+mysqlconnector://root:rootpass@localhost/feedback_db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@app.route('/submit', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    session = Session()
    feedback = Feedback(name=data['name'], email=data['email'], feedback=data['feedback'])
    session.add(feedback)
    session.commit()
    session.close()
    return jsonify({"message": "Feedback submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
