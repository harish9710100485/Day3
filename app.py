from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

USER_CREDENTIALS = {'admin': 'password123'}  # Predefined credentials

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('session_page'))  # Redirect to session page if logged in
    return render_template('login.html')  # Show login page if not logged in

@app.route('/login', methods=['POST'])
def login_user():
    username = request.form['username']
    password = request.form['password']
    
    # Check if the credentials are correct
    if USER_CREDENTIALS.get(username) == password:
        session['user'] = username
        return redirect(url_for('session_page'))  # Redirect to session page after successful login
    else:
        flash('Invalid username or password. Please try again.')  # Flash an error message
        return redirect(url_for('home'))  # Redirect back to login page if failed

@app.route('/session')
def session_page():
    if 'user' not in session:
        return redirect(url_for('home'))  # Redirect to home (login page) if not logged in
    return render_template('session.html', username=session['user'])

@app.route('/upload', methods=['GET', 'POST'])
def upload_files():
    if 'user' not in session:
        return redirect(url_for('home'))  # Ensure user is logged in to access the upload page
    
    if request.method == 'POST':
        files = request.files.getlist('files')
        for file in files:
            if file:
                file.save(os.path.join(UPLOAD_FOLDER, file.filename))  # Save file to the upload folder
        return redirect(url_for('details'))  # Redirect to details page after upload

    return render_template('upload.html')

@app.route('/details')
def details():
    if 'user' not in session:
        return redirect(url_for('home'))  # Ensure user is logged in to access details page
    
    files = os.listdir(UPLOAD_FOLDER)  # List all uploaded files
    return render_template('details.html', username=session['user'], files=files)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    if 'user' not in session:
        return redirect(url_for('home'))  # Ensure user is logged in to delete files
    
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)  # Remove the file
    return redirect(url_for('details'))  # Redirect back to details page after deletion

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)  # Remove the user from the session
    return redirect(url_for('home'))  # Redirect to home (login page)

if __name__ == '__main__':
    app.run(debug=True)
