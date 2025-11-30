# Stack_overflow — Programming Language Frequency Dashboard (2022–2024)

A small web-app that analyzes a dataset of Stack Overflow questions and visualizes the frequency of top programming languages over time (2022–2024) using a line chart.

---

## 🚀 What is this

- Back-end built with Flask (Python)  
- Front-end: plain HTML + Chart.js for visualization  
- Dataset: a CSV file containing Stack Overflow questions with timestamps and tags  
- Function: reads the CSV, counts how many questions per language per year, normalizes the frequency (in percentage), and exposes it via a REST API  
- The front-end fetches this JSON data from the API, then plots a line chart showing how the popularity of certain languages changed from 2022 to 2024  

---

## 📂 Project Structure
```bash
Stack_overflow/
│
├── app.py
├── updated_stackoverflow_questions.csv ← dataset (questions + tags + timestamps)
├── frontend/
│ └── index.html ← front-end dashboard
└── README.md ← this file
```

- `app.py`: Flask application — loads and processes the CSV, defines an API route to serve data.  
- `updated_stackoverflow_questions.csv`: The dataset you analyze.  
- `frontend/index.html`: HTML page that uses Chart.js to fetch data and draw the chart.  

---

## 🧑‍💻 Languages tracked

In this project, the following languages/tags are tracked:

- python  
- javascript  
- java  
- ruby  
- go  
- rust  
- sql  
- react  
- flutter  
- android  

You can modify this list in `app.py` under `languages_to_track` array, if you want to add or remove languages/tags.  

---

## 📊 What You See

On the webpage, you will see a line chart titled:

**“Top 10 Programming Language Frequency (2022–2024)”**

- **X-axis:** Years (2022, 2023, 2024)  
- **Y-axis:** Percentage of questions tagged with each language (normalized)  
- **Each line:** Represents one programming language — allowing you to easily compare popularity trends over time  

---

## ✅ Why This Approach?

- Using a **REST API** to serve data keeps the **backend and frontend decoupled** and modular  
- **JSON + Chart.js** → Easy visualization and flexible for future improvements  
- **Python + CSV processing** enables full control over data extraction and cleaning  
- Standard architecture used in modern data apps:  

## 📄 License / Data

- You are free to use, modify, or extend this project.
- If published publicly, please give credit 🙌

> (No formal license included yet — you may add one such as MIT if required.)
