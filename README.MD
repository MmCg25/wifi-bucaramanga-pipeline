# 📡 Bucaramanga Public WiFi Zones – Data Pipeline & Geospatial Analysis

This project builds a small **data engineering and geospatial analysis pipeline** to process and visualize public WiFi zones in Bucaramanga, Colombia.

The goal of the project is to practice:

* Python ETL pipelines
* PostgreSQL database integration
* Geospatial analysis with GeoPandas
* Interactive and static map visualization
* Data pipeline structuring for portfolio projects

---

## 🧠 Project Architecture

```
Open Data Source
       │
       ▼
   Python ETL
 (Extract / Transform)
       │
       ▼
   PostgreSQL Database
       │
       ▼
 Geospatial Processing
    (GeoPandas)
       │
       ▼
 Data Visualization
```

---

## 🗂 Project Structure

```
wifi-bucaramanga-pipeline
│
├── src
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── database.py
│
├── data
│   └── raw
│
├── notebooks
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Technologies Used

* Python
* PostgreSQL
* Pandas
* GeoPandas
* Contextily
* Matplotlib
* python-dotenv

---

## 🔐 Database Connection

Database credentials are stored using environment variables through a `.env` file.

Example configuration:

```
DB_NAME=zonas_wifi
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=5432
```

---

## ▶️ Running the Project

Install dependencies:

```
pip install -r requirements.txt
```

Run the pipeline:

```
python main.py
```

---

## 🗺 Visualization

The project generates maps showing the location of public WiFi zones in Bucaramanga using GeoPandas and OpenStreetMap tiles.

---

## 🎯 Learning Goals

This project focuses on developing skills in:

* Data engineering pipelines
* Geospatial data processing
* Database integration with Python
* Structuring production-like data projects

---

## 👨‍💻 Author

Physics graduate from Universidad Industrial de Santander (UIS) working in data analysis and data engineering projects.
