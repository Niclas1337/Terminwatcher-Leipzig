# Terminwatcher-Leipzig

A Python script that automatically monitors the availability of appointments at the online Kfz-Zulassungsbehörde appointment booking system of the Stadt Leipzig and notifies you when free appointments become available. Given how difficult it is to obtain an appointment in time through conventional means, this tool helps you catch available slots as soon as they open up.

## Installation

### Requirements
- Python 3.8+
- Chrome/Chromium browser (installed and up-to-date)

### Step 1: Install Selenium

```bash
pip install selenium
```

### Step 2: Download or clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Terminwatcher-Leipzig.git
cd Terminwatcher-Leipzig
```

## Usage

### Select your service

Edit `main.py` and change the `SERVICE_NAME` variable (line 14):

```python
SERVICE_NAME = "Umschreibung eines Fahrzeuges mit auswärtigem Kennzeichen"
```

If you're unsure about the exact service name: Run the script and it will show you all available services.

**Examples of service names:**
- `"Neuzulassung eines Fahrzeuges"`
- `"Zulassung eines ausländischen Fahrzeuges"`
- `"Umschreibung eines Fahrzeuges mit Leipziger Kennzeichen"`
- `"Umkennzeichnung"`
- `"Kurzzeitkennzeichen"`
- Any other available service from your booking system

### Start the script

```bash
python main.py
```

The script will then:
- Check availability every 5 minutes
- Automatically select your service
- When appointments are available: Beep 3 times + print "APPOINTMENTS AVAILABLE!"
- When no appointments: Print "No appointments"

Stop with `Ctrl+C`.

## Configuration

Open `main.py` and adjust these variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `URL` | Online-Terminvergabe booking URL | The appointment booking system to monitor |
| `SERVICE_NAME` | Registration service name | The service you want to monitor |
| `CHECK_INTERVAL` | 300 (5 minutes) | Seconds between checks |

### Change check interval

```python
CHECK_INTERVAL = 60  # Check every 60 seconds
```

## Important Notes

- **Educational Purpose**: This tool was developed for demonstrational and educational purposes only
- This script is intended for personal use with Leipzig's appointment booking systems
- Respect the website's terms of service
- Don't overload the server with requests (recommended: at least 60 seconds between checks)
- This script is not officially affiliated with the Stadt Leipzig
- The script may need adjustments if the booking system layout changes
- Users are solely responsible for compliance with the terms of service of the respective booking systems
- The author assumes no liability for misuse or any consequences arising from the use of this tool

## License

Free to use for personal purposes.
