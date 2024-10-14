
# Inventory Management API

### Setup Instructions
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up PostgreSQL and Redis as per `settings.py`.

3. Run migrations:
   ```
   python manage.py migrate
   ```

4. Start the server:
   ```
   python manage.py runserver
   ```

5. Access endpoints at `/api/items/` and JWT tokens at `/api/token/`.
    