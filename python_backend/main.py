import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
#from dfa import DFA
from automata.fa.dfa import DFA
from fastapi.staticfiles import StaticFiles
from utils.visualize import generate_pdf

app = FastAPI()

# Allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class DFARequest(BaseModel):
    states: list[str]
    alphabet: list[str]
    transitions: dict[str, dict[str, str]]
    start: str
    accept: list[str]
    input_string: str

@app.post("/simulate")
def simulate_dfa(data: DFARequest):
    try:
        dfa = DFA(
            states=set(data.states),
            input_symbols=set(data.alphabet),
            transitions=data.transitions,
            initial_state=data.start,
            final_states=set(data.accept),
        )
        result = dfa.accepts_input(data.input_string)

        # 🔹 Pass extra info to PDF generator
        pdf_path = generate_pdf(dfa, data.input_string, result)

        return {"accepted": result, "pdf_path": pdf_path}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    
# ✅ Ensure the pdf directory exists
os.makedirs("pdf", exist_ok=True)

# ✅ Serve PDFs at http://localhost:8000/pdf/dfa_output.pdf
app.mount("/pdf", StaticFiles(directory="pdf"), name="pdf")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
