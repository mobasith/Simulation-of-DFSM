import os
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

def generate_pdf(dfa, input_string=None, is_accepted=None):
    # Create output paths
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    image_path = f"pdf/dfa_{timestamp}.png"
    pdf_path = f"pdf/dfa_{timestamp}.pdf"
    os.makedirs("pdf", exist_ok=True)

    # Create DFA graph with NetworkX
    G = nx.MultiDiGraph()

    for state in dfa.states:
        G.add_node(state)

    for from_state, transitions in dfa.transitions.items():
        for symbol, to_state in transitions.items():
            G.add_edge(from_state, to_state, label=symbol)

    # Layout the graph
    pos = nx.circular_layout(G)

    # Node colors based on role
    node_colors = []
    for state in G.nodes():
        if state == dfa.initial_state:
            node_colors.append("limegreen")  # Start
        elif state in dfa.final_states:
            node_colors.append("dodgerblue")  # Accept
        else:
            node_colors.append("lightgray")  # Normal

    # Draw the graph
    plt.figure(figsize=(8, 6))
    nx.draw(
        G, pos, with_labels=True,
        node_color=node_colors, node_size=1500,
        font_size=12, font_weight='bold',
        arrows=True, edgecolors="black"
    )
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(image_path, bbox_inches='tight')
    plt.close()

    # Create PDF
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # Logo (optional - replace with your own image if available)
    # c.drawImage("logo.png", 440, 720, width=100, height=100)

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 760, "📘 DFA Simulation Result")

    y = 730
    c.setFont("Helvetica", 12)

    # Input string + acceptance result
    if input_string is not None:
        c.drawString(50, y, f"Input String: {input_string}")
        y -= 20
    if is_accepted is not None:
        verdict = "✅ Accepted" if is_accepted else "❌ Rejected"
        c.drawString(50, y, f"Result: {verdict}")
        y -= 20

    # DFA Info
    c.drawString(50, y, f"Start State: {dfa.initial_state}")
    y -= 20
    c.drawString(50, y, f"Accept States: {', '.join(sorted(dfa.final_states))}")
    y -= 20
    c.drawString(50, y, f"Alphabet: {', '.join(sorted(dfa.input_symbols))}")
    y -= 20
    c.drawString(50, y, f"States: {', '.join(sorted(dfa.states))}")
    y -= 30
    c.drawString(50, y, "Transitions:")
    y -= 20

    # Transitions
    # for from_state, paths in dfa.transitions.items():
    #     for symbol, to_state in paths.items():
    #         c.drawString(70, y, f"{from_state} --[{symbol}]--> {to_state}")
    #         y -= 15
    #         if y < 100:
    #             c.showPage()
    #             y = height - 50

    # Embed DFA graph image
    if y < 300:
        c.showPage()
        y = height - 100

    img = ImageReader(image_path)
    c.drawImage(img, 50, 100, width=500, preserveAspectRatio=True, mask='auto')

    c.save()
    return f"/pdf/dfa_{timestamp}.pdf"
