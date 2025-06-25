
### Installation Steps

1. ✅ Clone the repository
   ```bash
   git clone https://github.com/yourusername/SGET_FPBM.git
   cd SGET_FPBM
   ```

2. ✅ Create a virtual environment
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Unix/MacOS
   source venv/bin/activate
   ```

3. ✅ Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. ✅ Create a PostgreSQL database
   ```sql
   CREATE DATABASE unitasker_db1;
   ```

5. ✅ Create a `.env` file with the following content:
   ```
   SECRET_KEY=your-super-secret-key-change-this
   DATABASE_URL=postgresql://postgres:your_password@localhost:5432/unitasker_db1
   FLASK_APP=app.py
   FLASK_ENV=development
   ```

6. ✅ Initialize and apply database migrations
   ```bash
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade
   ```

7. ✅ Create an admin user (run in Python shell)
   ```python
   from app import app, db
   from models import User
   
   with app.app_context():
       admin = User(
           username='admin',
           email='admin@example.com',
           first_name='Admin',
           last_name='User',
           role='admin'
       )
       admin.set_password('your_password')
       db.session.add(admin)
       db.session.commit()
   ```

8. ✅ Run the application
   ```bash
   flask run
   ```

9. ✅ Access the application at http://127.0.0.1:5000
