import os
from graphviz import Digraph

def generate_pdf(dfa, filename="dfa_output.pdf"):
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

    # ✅ Save into backend/pdf/
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'pdf')
    os.makedirs(output_dir, exist_ok=True)

    pdf_path = os.path.join(output_dir, filename)

    # ✅ Save PDF and return path
    final_path = dot.render(pdf_path, cleanup=True)
    print("✅ PDF saved at:", final_path)

    return f"/pdf/{filename}"  # This is the public path for Angular
