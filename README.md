# Find Uz and Diplomatic Dictionary API

A comprehensive Django-based web application that combines a lost and found platform ("Find Uz") with a diplomatic dictionary system. The platform enables users to report lost and found items, communicate via messaging, and access a rich database of diplomatic terms in Uzbek language.

## Features

### 🔍 Lost and Found System (Find Uz)

- **User Management**: Custom user model with phone number authentication
- **Item Reporting**: Report lost or found items with detailed descriptions, categories, locations, and images
- **Item Status Tracking**: Track items through statuses (Lost, Found, Claimed, Returned)
- **Messaging System**: Direct messaging between users for item coordination
- **Location Services**: GPS coordinates for item locations
- **Image Upload**: Support for multiple item images and message attachments

### 📚 Diplomatic Dictionary

- **Term Database**: Extensive collection of diplomatic terms with Uzbek definitions
- **Categorization**: Terms organized by categories, countries, and sources
- **Search Functionality**: Full-text search across terms and definitions
- **Photo Support**: Visual aids for diplomatic terms
- **Web Interface**: User-friendly web pages for browsing and searching terms
- **Admin Management**: Comprehensive admin interface for content management

### 🔐 Authentication & Security

- **JWT Authentication**: Secure token-based authentication
- **Phone Number Verification**: SMS-based phone authentication
- **Role-Based Access**: Different user types (Dict User, Find Uz User)
- **Admin Permissions**: Granular permissions for dictionary management

### 🛠 Technical Features

- **REST API**: Full REST API with OpenAPI/Swagger documentation
- **Async Support**: ASGI support with Uvicorn for high performance
- **OCR Integration**: Tesseract OCR for image text extraction
- **Docker Support**: Containerized deployment
- **Modern Package Management**: UV for fast dependency management
- **ORJSON Rendering**: High-performance JSON responses

## Technology Stack

- **Backend**: Django 5.2.1, Django REST Framework
- **Authentication**: Django Simple JWT
- **Database**: SQLite (development), PostgreSQL (production)
- **Async**: Uvicorn, ADRF
- **API Documentation**: DRF Spectacular (Swagger/ReDoc)
- **Image Processing**: Pillow
- **OCR**: Tesseract
- **Package Management**: UV
- **Deployment**: Docker
- **Frontend**: HTML/CSS Templates

## Project Structure

```
find-uz/
├── api/                    # Lost and Found API app
│   ├── models.py          # User, Item, Message models
│   ├── views.py           # API endpoints
│   ├── serializers.py     # DRF serializers
│   └── urls.py            # URL routing
├── authenticate/          # Authentication app
│   ├── views.py           # Auth endpoints
│   └── urls.py            # Auth URLs
├── dictionary/            # Diplomatic Dictionary app
│   ├── models.py          # Term, Category, Country models
│   ├── views.py           # Dictionary API and web views
│   ├── templates/         # HTML templates
│   └── urls.py            # Dictionary URLs
├── manager/               # Management app
│   └── models.py          # App management models
├── core/                  # Django project settings
│   ├── settings.py        # Main configuration
│   ├── urls.py            # Root URL configuration
│   └── asgi.py            # ASGI application
├── templates/             # Global HTML templates
├── media/                 # User uploaded files
├── static/                # Static assets
└── requirements.txt       # Python dependencies
```

## Installation

### Prerequisites

- Python 3.12+
- Docker (optional)
- Tesseract OCR (for image text extraction)

### Local Development

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd find-uz
   ```
2. **Install UV package manager**

   ```bash
   pip install uv
   ```
3. **Install dependencies**

   ```bash
   uv sync
   ```
4. **Run migrations**

   ```bash
   uv run python manage.py migrate
   ```
5. **Create superuser**

   ```bash
   uv run python manage.py createsuperuser
   ```
6. **Run development server**

   ```bash
   uv run python manage.py runserver
   ```

### Docker Deployment

1. **Build and run with Docker**
   ```bash
   docker build -t find-uz .
   docker run -p 8000:8000 find-uz
   ```

## API Endpoints

### Authentication

- `POST /auth/login/` - User login
- `POST /auth/register/` - User registration
- `POST /auth/refresh/` - Refresh JWT token

### Lost and Found (Find Uz)

- `GET /finduz/items/` - List items
- `POST /finduz/items/` - Create new item
- `GET /finduz/items/{id}/` - Get item details
- `PUT /finduz/items/{id}/` - Update item
- `DELETE /finduz/items/{id}/` - Delete item
- `GET /finduz/messages/` - List messages
- `POST /finduz/messages/` - Send message

### Diplomatic Dictionary

- `GET /dictionary/terms/` - List diplomatic terms
- `POST /dictionary/terms/` - Create new term (admin only)
- `GET /dictionary/terms/{id}/` - Get term details
- `PUT /dictionary/terms/{id}/` - Update term (admin only)
- `GET /dictionary/categories/` - List categories
- `GET /dictionary/countries/` - List countries

### API Documentation

- Swagger UI: `/api/swagger/`
- ReDoc: `/api/redoc/`
- OpenAPI Schema: `/api/schema/`

## Web Interface

The application includes a web interface for the diplomatic dictionary:

- `/` - Home page with featured terms
- `/terms/` - Browse all terms
- `/categories/` - Browse by categories
- `/term/{id}/` - Individual term page
- `/about/` - About page

## Data Population

To populate the diplomatic dictionary with initial data:

```bash
uv run python main.py
```

This script reads from `result.json` and creates DiplomaticTerm instances.

## Configuration

### Environment Variables

- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode (default: True)
- `DATABASE_URL` - Database connection URL
- `ALLOWED_HOSTS` - Comma-separated allowed hosts

### Settings

Key settings in `core/settings.py`:

- JWT configuration
- CORS settings
- Media file handling
- Installed apps configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:

- Create an issue in the repository
- Contact the development team

---

**Last Update:** 2026-01-26
