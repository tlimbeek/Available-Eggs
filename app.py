from flask import Flask, render_template, request, jsonify, send_file
import sqlite3
import uuid
import os
from datetime import datetime

app = Flask(__name__)

# Database path
DB_PATH = 'eggs.db'

def init_db():
  # Initialize database with schema
  conn = sqlite3.connect(DB_PATH)
  c = conn.cursor()
  c.execute('''
    CREATE TABLE IF NOT EXISTS entries (
      id TEXT PRIMARY KEY,
      farm_name TEXT NOT NULL,
      contact TEXT NOT NULL,
      phone TEXT,
      email TEXT,
      location TEXT NOT NULL,
      egg_type TEXT NOT NULLL,
      size TEXT NOT NULL,
      grade TEXT NOT NULL,
      pack TEXT NOT NULL,
      quantity_value REAL NOT NULL,
      quantity_unit TEXT NOT NULL,
      price_per_dozen REAL,
      available_start TEXT,
      available_end TEXT,
      notes TEXT,
      created_at TEXT
  )
''')
  conn.commit()
  conn.close()

# Initialize DB on startup
init_db()

@app.route('/')
def index():
  return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
  data = request.json

  # Basic validation (you'll expand this)
  required = ['farm_name', 'contact', 'location', 'egg_type', 'size', 'grade', 'pack', 'quatity_value', 'quantity_unit']
  for field in required:
    if not data.get(field):
      return jsonify({'error': f'{field} is required'}), 400

  # Generate UUID
  entry_id = str(uuid.uuid4())

  # Save to database
  conn = sqlite3.connect(DB_PATH)
  c = conn.cursor()
  c.execute('''
      INSERT INTO entries VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  ''', (
    entry_id,
    data.get('farm_name'),
    data.get('contact'),
    data.get('phone'),
    data.get('email'),
    data.get('location'),
    data.get('egg_type'),
    data.get('size'),
    data.get('grade'),
    data.get('pack'),
    data.get('quantity_value')
    data.get('quantity_unit'),
    data.get('price_per_dozen'),
    data.get('available_start'),
    data.get('available_end'),
    data.get('notes'),
    datetime.now().isoformat()
  ))
  conn.commit()
  conn.close()

  return jsonify({'id: entry_id})

@app.route('/entries')
def entries():
  conn = sqlite3.connect(DB_PATH)
  conn.row_factory = sqlite3.Row
  c = conn.cursor()
  c.execute('SELECCT * FROM entries')
  rows = c.fetchall()
  conn.close()

  return jsonify([dict(row) for row in rows])

@app.route('/exportcsv')
def export_csv():
  # TO DO: implement CSV export
  return "CSV export wip", 200

@app.route('/healthz')
def health():
  return "OK", 200

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8080))
  app.run(host='0.0.0.0', port=port, debug=True)
