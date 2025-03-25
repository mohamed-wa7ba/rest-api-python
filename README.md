# 🌟 Flask MySQL REST API / GraphQL Server

<div style="background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #2563eb;">
A powerful hybrid API server built with Python, Flask, and MySQL supporting both REST and GraphQL endpoints.
</div>

## 🚀 How to Run

### 1️⃣ Set Up MySQL Database
```sql
-- Create database
CREATE DATABASE shop;

-- Create users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- Insert sample data
INSERT INTO users (name, email) VALUES 
('Mohamed Wahba', 'mohamed@baianat.com');
2️⃣ Configure Database Connection
Update config/database.py with your credentials:

python
Copy
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'yourpassword'
MYSQL_DB = 'shop'
3️⃣ Install Dependencies
bash
Copy
pip install -r requirements.txt
4️⃣ Run the Server
bash
Copy
# Development mode
python app.py

# Production mode
gunicorn -w 4 -b 0.0.0.0:5000 app:app

🏗 Project Structure
Copy
my_project/
├── app.py                # Main application
├── config/               # Configuration
├── graphql/              # GraphQL setup
├── rest/                 # REST endpoints
├── models/               # Database models
└── requirements.txt      # Dependencies
👨‍💻 About Me
    I'm Mohammed Wahba, a software developer with 5+ years of experience in building scalable and efficient applications. Currently, I serve as a Team Leader at Baianat, where I lead a talented team of developers to deliver high-quality software solutions.:
      Frontend Development: Nuxt.js, Vue.js, Angular, Svelte and React.
      Backend Development: Java, Spring Boot, Nest.js, express.js,  Node.js, and GraphQL.
      Database Management: MySQL, PostgreSQL, and MongoDB.
      Mobile Apps: Cross-platform mobile applications built using Flutter or React Native.
      Problem Solving: Passionate about solving complex problems and delivering high-quality solutions.
      I enjoy working on challenging projects and always strive to learn and improve my skills. Feel free to reach out if you have any questions or need assistance! 

Contact: 
If you have any questions or need help, feel free to reach out:
Name: Mohammed Wahba
Email: mohamed@baianat.com
Company: Baianat