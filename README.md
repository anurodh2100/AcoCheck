# AcoCheck

AcoCheck is a Django-based hostel and resident management application used to manage hostels, residents, verifications and user accounts. This repository contains the Django project and several apps including `accounts`, `hostels`, `residents`, `verification`, `search`, and `dashboard`.

## Features
- User registration, login and profile management
- Hostel CRUD (create, update, delete) and listing
- Resident management and verification workflow
- Search interface for residents/hostels
- Admin dashboard

## Tech stack
- Python 3.x
- Django
- PostgreSQL (recommended in production)
- Docker / docker-compose (optional)

## Requirements
- Git
- Python 3.8+ (use the version in `requirements.txt`)
- pip

## Quick setup (local)
1. Clone the repo:

```bash
git clone <repo-url>
cd AcoCheck
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables or update `acocheck/settings.py` for database and secret key.

5. Run migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to view the app.


Adjust environment variables in the `docker-compose.yml` or a .env file as needed.

- Keep migrations committed. Use `python manage.py makemigrations` to generate them.

## Contributing
- Fork the repo and open a pull request with a clear description of changes.
- Follow project style and add tests where appropriate.

## License
This project does not include a license file. Add a `LICENSE` file to indicate terms. For example, add an MIT or Apache 2.0 license as appropriate.

## Maintainers / Contact
- Project maintainer: (add your name and email or contact method here)

---

For more details, see the `docs/` directory (`docs/DEPLOYMENT.md`, `docs/API.md`, `docs/ARCHITECTURE.md`).
