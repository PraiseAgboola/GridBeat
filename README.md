# GridHeartbeat Nigeria

This is the documentation for the GridHeartbeat Nigeria project. The project focuses on providing real-time grid status prediction and notifications using various technologies.

## Project Structure

- **replit.nix:** Nix configuration for Playwright installation.
- **main.py:** FastAPI backend entry point.
- **app/scraper.py:** Playwright scraper for NISO and NigGrid.
- **app/database.py:** SQLite database models and operations.
- **app/rocof_calculator.py:** RoCoF calculation engine.
- **app/grid_logic.py:** Grid status prediction logic.
- **app/whatsapp_gateway.py:** IPC/API bridge to Node.js WhatsApp service.
- **whatsapp_service.js:** Node.js WhatsApp notification handler.
- **static/index.html:** Frontend dashboard with Tailwind CSS.
- **static/dashboard.js:** Chart.js real-time visualization.
- **requirements.txt:** Python dependencies.
- **package.json:** Node.js dependencies.
- **.gitignore:** Git ignore file.
- **README.md:** Project documentation.

## Installation

### Python Dependencies

To install the Python dependencies, run:
```bash
pip install -r requirements.txt
```

### Node.js Dependencies

To install the Node.js dependencies, run:
```bash
npm install
```