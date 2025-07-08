import os
from datetime import datetime
from graphviz import Digraph

def generate_pdf(dfa):
    dot = Digraph(format='pdf')
    dot.attr(rankdir='LR')

    for state in dfa.states:
        shape = 'doublecircle' if state in dfa.final_states else 'circle'
        dot.node(state, shape=shape)

    dot.node('', shape='none')
    dot.edge('', dfa.initial_state)

    for from_state, transitions in dfa.transitions.items():
        for symbol, to_state in transitions.items():
            dot.edge(from_state, to_state, label=symbol)

    # ✅ Generate unique filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"dfa_{timestamp}"

    # ✅ Ensure output directory exists
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'pdf')
    os.makedirs(output_dir, exist_ok=True)

    pdf_path = os.path.join(output_dir, filename)

    dot.render(pdf_path, cleanup=True)

    final_pdf_name = f"{filename}.pdf"
    print("✅ PDF saved as:", final_pdf_name)

    # Return the correct public-facing path
    return f"/pdf/{final_pdf_name}"
