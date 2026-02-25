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
