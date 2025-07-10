# DFSM Analyzer: Visual DFA Simulator & Verifier :
A full-stack web application that allows users to define a **Deterministic Finite State Machine (DFA)**, simulate input strings against it, and generate a **visual PDF representation** of the DFA. Built using **Angular** and **FastAPI**, with DFA logic powered by `automata-lib`.

## 🚀 Features
- Define DFA (states, alphabet, transitions, start/accept states)
- Input a string and check if it's accepted
- Visualize the DFA structure as a downloadable PDF
- Practical tool for automata theory

## 🛠️ Tech Stack
1. Frontend: Angular 17+
2. Backend: FastAPI (Python 3.10+)
3. DFA logic: automata-lib v1.0.0
4. Visualization: reportlab, matplotlib

## 🧑‍💻 Installation
## Backend:
1. Navigate to backend:
      ```bash
      cd backend
   
3. Create and activate virtual environment:
      ```bash
      python -m venv venv
      ```
   ```bash
   source venv/bin/activate
On Windows: venv\Scripts\activate
   
4. Install dependencies:
      ```bash
    pip install -r requirements.txt

6. Install Graphviz (Required for PDF output):
    - Linux/macOS:
         ```bash
       sudo apt install graphviz
    - Windows:
    Download from https://graphviz.org/download/

7. Run the FastAPI server:
      ```bash
   uvicorn main:app --reload

## Frontend: 
1. Navigate to frontend folder:
   ```bash
   cd Angular_frontend

2. Install dependencies:
   ```bash
   npm install

3. Run the frontend app:
   ```bash
   ng serve
   
Visit: http://localhost:4200

## 🧱 Dependencies:
- Backend (requirements.txt):
1. annotated-types==0.7.0
2. anyio==4.9.0
3. automata-lib==9.0.0
4. cached_method==0.1.0
5. charset-normalizer==3.4.2
6. click==8.2.1
7. colorama==0.4.6
8. contourpy==1.3.2
9. cycler==0.12.1
10. fastapi==0.115.14
11. fonttools==4.58.5
12. frozendict==2.4.6
13. graphviz==0.21
14. h11==0.16.0
16. idna==3.10
17. kiwisolver==1.4.8
18. matplotlib==3.10.3
19. networkx==3.5
20. numpy==2.3.1
21. packaging==25.0
22. pillow==11.3.0
23. pydantic==2.11.7
24. pydantic_core==2.33.2
25. pyparsing==3.2.3
26. python-dateutil==2.9.0.post0
27. reportlab==4.4.2
28. six==1.17.0
29. sniffio==1.3.1
30. starlette==0.46.2
31. typing-inspection==0.4.1
32. typing_extensions==4.14.1
33. uvicorn==0.35.0

- Frontend (Angular v17+):
 1. Angular CLI v17
 2. RxJS v7+
 3. TypeScript v5+

## 🧪 Example Input
States: q0,q1,q2

Alphabet: 0,1

Start State: q0

Accept States: q2

Input String: 010

Transitions:
- q0,0,q1
- q0,1,q0
- q1,0,q1
- q1,1,q2
- q2,0,q2
- q2,1,q2

## 📥 Output
String verdict: Accepted ✅ or Rejected ❌

DFA PDF: Downloadable file from /pdf/dfa_output.pdf


## 🙌 Author
Mohammed Basith
📫 LinkedIn: www.linkedin.com/in/mohammed-basith-97326321b



