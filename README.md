# Student Registration & File Upload System

## Overview
This project is a **Student Registration & File Upload System** built using **Flask, HTML, Bootstrap 5, and JavaScript**. It allows students to register, log in, upload files, and manage their uploaded documents.

## Features
- **User Authentication** (Predefined credentials for login)
- **Student Registration Form** with form validation
- **Session Handling** using Flask sessions
- **File Upload System** with a dedicated upload directory
- **Bootstrap 5 for Responsive Design**
- **File Deletion Functionality**
- **Session-Based Access Control**
- **Redirection Based on Authentication Status**

## Technology Stack
- **Flask** (Python) for backend
- **HTML** for structure
- **Bootstrap 5** for styling and layout
- **JavaScript** for interactivity
- **SessionStorage** for temporary data handling

## File Structure
```
project-folder/
│── app.py             # Main Flask application
│── templates/
│   │── login.html     # Login Page
│   │── session.html   # User session page
│   │── upload.html    # File upload page
│   │── details.html   # Uploaded file list page
│── static/
│── uploads/          # Directory to store uploaded files
```

## Installation & Usage
1. Clone or download the repository.
2. Install required dependencies:
   ```bash
   pip install flask
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000/` in a web browser.
5. Log in using predefined credentials (default: `admin/password123`).
6. Register, upload files, and manage them via the interface.

## Flask Functionality
### **User Authentication**
- Users must log in with predefined credentials.
- Session-based authentication ensures restricted access.

### **File Upload & Management**
- Users can upload multiple files at once.
- Files are stored in an `uploads/` directory.
- Users can delete their uploaded files.

### **Session Handling**
- Users must be logged in to access upload and details pages.
- Session is stored using Flask’s `session` module.
- Logout functionality clears the session.

## Bootstrap 5 Integration
- Uses Bootstrap 5 for a clean UI.
- **Card layout** for structured design.
- **Form control classes** for improved styling.
- **Responsive container** for better accessibility.

## Conclusion
This project provides a **modern, secure, and user-friendly student registration and file management system** using Flask, Bootstrap 5, and JavaScript. With user authentication and session handling, it ensures restricted access to file uploads and management.

---
**Author:** Harish  
**Internship:** MinervaSoft  
**Project:** Student Registration & File Upload System

