# 📡 Bucaramanga Public WiFi Zones – Data Pipeline & Geospatial Analysis

This project builds a small **data engineering and analysis pipeline** to process and visualize public WiFi zones in Bucaramanga, Colombia.

The goal of the project is to practice:

* Python ETL pipelines
* PostgreSQL database integration
* Data analysis with Pandas
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
   Processing
    (Pandas)
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
│   ├── __init__.py
│   ├── database.py
│   ├── extract.py
│   ├── load.py
│   ├── paths.py
│   └── transform.py
│
├── data
│   ├── maps
│   ├── outputs
│   ├── processed
│   └── raw
│
├── .env
├── main.py
├── visualizer_png.py
├── visualizer_html.py
├── README.MD
└── requirements.txt
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
* folium

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

The project generates maps showing the location of public WiFi zones in Bucaramanga. It implements two visualizers, one static using PyPlot (PNG) and one interactive using folium (html).

---

## 🎯 Learning Goals

This project focuses on developing skills in:

* Data engineering pipelines
* Data processing
* Database integration with Python
* Structuring production-like data projects

---

## 👨‍💻 Author

Marcos Marcelino Carrillo Garcia
Physics graduate from Universidad Industrial de Santander (UIS) building data pipelines and geospatial analytics projects with Python and PostgreSQL.
