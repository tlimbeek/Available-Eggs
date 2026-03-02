# Available-Eggs

## Setup Instructions

### Option A — Use the live deployment 
#### (no setup required, startup buffer takes 30-60 seconds)
The app is deployed on Render and available at:
https://available-eggs.onrender.com/

No installation or code execution needed. Just open the URL in your browser.
Note: The free tier may take 30–60 seconds to wake up on first visit if idle.

### Option B — Run locally
1. Install dependencies:
```
pip install -r requirements.txt
```
2. Start the app (one command):
```
python app.py
```
3. Open your browser at `http://localhost:8080`

### Running the tests
With the app dependencies installed, run:
```
py test_app.py
```

### Exporting the CSV
Visit the following URL while the app is running (locally or on Render):
```
http://localhost:8080/exportcsv
```
The browser will automatically download `export.csv`.

## Endpoint Documentation
A table listing all 5 routes:

Method	Path	Description
GET	/	Renders the form
POST	/submit	Saves a record, returns { id: "..." }
GET	/entries	Returns all records as JSON
GET	/exportcsv	Downloads all records as CSV
GET	/healthz	Returns 200 OK

## Request -> Handler -> Storage
Browser -> GET /        -> index()       -> renders form.html
Browser -> POST /submit -> submit()      -> INSERT INTO eggs.db
Browser -> GET /entries -> entries()     -> SELECT from eggs.db -> JSON
Browser -> GET /exportcsv -> export_csv() -> SELECT from eggs.db -> CSV file


Trade-off 1: Switching to Render instead of Google Cloud for hosting as the Google Cloud verification system is incompatible with my bank.
Pros: easier to setup
Cons: less scalable, web app will enter sleep mode after 15 minutes of inactivity. Next startup request will take 30-60 seconds to load.



app.py: 
Database and backend logic

form.html:
the skeleton of the web app