# PhotoGalleryWeb

A simple Django photo gallery project with user registration, login, profile management, password change, and a photo browsing page.

## Features
- User registration and login
- Password change flow
- Profile page with bio and profile picture
- Home page with photo cards and tag search
- Photo detail page with like/dislike buttons

## Setup
1. Create and activate a virtual environment.
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Notes
- The project uses SQLite for local development.
- Sample photos are added automatically when you run the seed command in the shell.
- For deployment, you can host it on Render or another Python hosting platform.

