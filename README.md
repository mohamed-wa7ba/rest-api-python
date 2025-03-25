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
<div style="background-color: #f0fdf4; padding: 15px; border-radius: 10px; border-left: 5px solid #16a34a;"> 💡 <strong>Tip:</strong> For production, use environment variables for sensitive data! </div> ```

👨‍💻 About Me
<div style="background-color: #fff0f6; padding: 15px; border-radius: 10px; border-left: 5px solid #d6336c;"> <h3 style="color: #d6336c;">Mohammed Wahba</h3> <p><strong>Team Leader at Baianat</strong> | 5+ years experience in full-stack development</p>
🛠 <strong>Technical Skills:</strong>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;"> <div> <span style="color: #1e40af;">• Frontend:</span> Nuxt.js, Vue.js, Angular, Svelte, React </div> <div> <span style="color: #1e40af;">• Backend:</span> Python, Java, Spring Boot, Node.js, GraphQL </div> <div> <span style="color: #1e40af;">• Databases:</span> MySQL, PostgreSQL, MongoDB </div> <div> <span style="color: #1e40af;">• Mobile:</span> Flutter, React Native </div> </div>
💡 <strong>Passionate</strong> about solving complex problems and delivering high-quality solutions

</div>
📬 Contact
<div style="background-color: #e6f7ff; padding: 15px; border-radius: 10px; border-left: 5px solid #0891b2;"> 📧 <strong>Email:</strong> <a href="mailto:mohamed@baianat.com" style="color: #2563eb;">mohamed@baianat.com</a><br> 🏢 <strong>Company:</strong> <a href="https://baianat.com" style="color: #2563eb;">Baianat</a><br> 🔗 <strong>LinkedIn:</strong> <a href="https://linkedin.com/in/yourprofile" style="color: #2563eb;">Mohammed Wahba</a> </div>