# EmptyCup

A modern web application for browsing and managing listings with a clean, user-friendly interface.

## Features

- 📱 Responsive design with mobile-first approach
- 🎨 Modern UI using Tailwind CSS
- 📋 Listing management system
- ⭐ Rating display
- 📞 Contact information display
- 📌 Shortlisting functionality
- 🔍 Filtering and sorting options
- 🗺️ Map integration (coming soon)
- 📸 Gallery view (coming soon)

## Deployment

### Frontend (Vercel)
The frontend is hosted on Vercel. Any changes pushed to the main branch will automatically trigger a new deployment.

### Backend (Render)
The backend is hosted on Render. To deploy:
1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Add any required environment variables in Render's dashboard

## Local Development

## Tech Stack

- Frontend:
  - HTML5
  - Tailwind CSS
  - JavaScript (Vanilla)
  - Custom CSS
- Backend:
  - Flask (Python)
  - RESTful API

## Prerequisites

- Python 3.x
- Node.js (for development)
- Modern web browser

## Setup Instructions

1. Clone the repository:
```bash
git clone [repository-url]
cd emptycup
```

2. Set up the Python environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Start the Flask backend:
```bash
python app.py
```

4. Open the frontend:
- Navigate to the `frontend` directory
- Open `index.html` in your web browser
- Or serve it using a local server

## Project Structure

```
emptycup/
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── styles.css
│   └── assets/
├── app.py
├── requirements.txt
└── README.md
```

## API Endpoints

- `GET /api/listings` - Retrieve all listings
- Base URL: `https://emptycup-backend.onrender.com` (Production)
- Base URL: `http://127.0.0.1:5000` (Local Development)
- More endpoints coming soon...

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any queries or support, please reach out to [your-email@example.com]
