# DFSM Analyzer: Visual DFA Simulator & Verifier :
A full-stack web application that allows users to define a **Deterministic Finite State Machine (DFA)**, simulate input strings against it, and generate a **visual PDF representation** of the DFA. Built using **Angular** and **FastAPI**, with DFA logic powered by `automata-lib` and Graphviz.

## 🚀 Features
- Define DFA (states, alphabet, transitions, start/accept states)
- Input a string and check if it's accepted
- Visualize the DFA structure as a downloadable PDF
- Practical tool for automata theory

## 🛠️ Tech Stack
Frontend: Angular 17+
Backend: FastAPI (Python 3.10+)
DFA logic: automata-lib v1.0.0
Visualization: graphviz

## 📂 Project Structure
project-root/
│
├── Angular_frontend/ # Angular UI app (DFSM form, results)
├── backend/ # FastAPI app (DFA logic + PDF generation)
│ └── utils/
│ └── visualize.py # Graphviz DFA rendering logic
└── pdf/ # Output folder for DFA PDFs

## 🧑‍💻 Installation
## Backend:
1. Navigate to backend:
   cd backend
   
2. Create and activate virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
   
3. Install dependencies:
    pip install -r requirements.txt

4. Install Graphviz (Required for PDF output):
     Linux/macOS:
      sudo apt install graphviz
     Windows:
       Download from https://graphviz.org/download/

5. Run the FastAPI server:
    uvicorn main:app --reload

## Frontend: 
1. Navigate to frontend folder:
    cd Angular_frontend

2. Install dependencies:
  npm install

3. Run the frontend app:
   ng serve
   
Visit: http://localhost:4200

## 🧱 Dependencies:
Backend (requirements.txt):
fastapi==0.111.0
uvicorn==0.30.1
automata-lib==1.0.0
graphviz==0.20.3
pydantic==2.7.1

Frontend (Angular v17+):
Angular CLI v17
RxJS v7+
TypeScript v5+

## 🙌 Author
Mohammed Basith
📫 LinkedIn: www.linkedin.com/in/mohammed-basith-97326321b



