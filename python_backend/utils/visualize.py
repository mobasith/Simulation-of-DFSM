from automata.fa.dfa import DFA
from graphviz import Digraph

def generate_pdf(dfa: DFA, filename="dfa_output.pdf"):
    dot = Digraph(format='pdf')
    dot.attr(rankdir='LR')

    # Draw states
    for state in dfa.states:
        shape = 'doublecircle' if state in dfa.final_states else 'circle'
        dot.node(state, shape=shape)

    # Start arrow
    dot.node('', shape='none')
    dot.edge('', dfa.initial_state)

    # Transitions
    for from_state, paths in dfa.transitions.items():
        for symbol, to_state in paths.items():
            label = symbol
            dot.edge(from_state, to_state, label=label)

    dot.render(filename, cleanup=True)
    return f"/pdf/{filename}"
