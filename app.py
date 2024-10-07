from flask import Flask, render_template, request, session, jsonify
import random
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Server-side storage of chat messages
chat_messages = []

# Home route to render the HTML page
@app.route('/')
def home():
    # Assign unique user ID for each session
    if 'user_id' not in session:
        session['user_id'] = f'User{random.randint(1000, 9999)}'
    return render_template('index.html', user_id=session['user_id'])

# Home route to render the HTML page
@app.route('/article')
def article():
    # Assign unique user ID for each session
    return render_template('article.html')

# API to get the latest chat messages
@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(chat_messages)

# API to send a new message
@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('message')
    user_id = session.get('user_id', 'Anonymous')  # Get user ID from session
    if user_message:
        message_data = {
            'user': user_id,
            'message': user_message,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        chat_messages.append(message_data)
    return '', 204  # Return success but no content

if __name__ == '__main__':
    app.run(debug=True)
