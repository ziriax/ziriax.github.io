"""Make a 1:1 scale PDF (Portable Document Format) drilling template:
a 50 mm square with 4 holes, 40 mm apart, each marked with a cross."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

SQUARE = 50 * mm        # edge length of the square
SPACING = 40 * mm       # distance between hole centers
HOLE_D = 3 * mm         # hole diameter (change this if you need another size)
CROSS = 8 * mm          # total length of each cross arm (line through the hole)

def make(path):
    w, h = A4
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle("50 mm square drill template")

    # square centered on the page
    x0, y0 = (w - SQUARE) / 2, (h - SQUARE) / 2
    c.setLineWidth(0.3 * mm)
    c.rect(x0, y0, SQUARE, SQUARE)

    # hole centers: 5 mm from each edge, 40 mm apart
    m = (SQUARE - SPACING) / 2
    c.setLineWidth(0.15 * mm)
    for cx in (x0 + m, x0 + m + SPACING):
        for cy in (y0 + m, y0 + m + SPACING):
            c.circle(cx, cy, HOLE_D / 2)
            c.line(cx - CROSS / 2, cy, cx + CROSS / 2, cy)
            c.line(cx, cy - CROSS / 2, cx, cy + CROSS / 2)

    # labels
    c.setFont("Helvetica", 9)
    c.drawCentredString(w / 2, y0 - 8 * mm,
        f"Square 50 x 50 mm - holes {HOLE_D/mm:g} mm, 40 mm apart (5 mm from edges)")
    c.drawCentredString(w / 2, y0 - 13 * mm,
        "Print at 100% / 'Actual size' (no 'Fit to page'). Check: the square must measure 50 mm.")

    # 100 mm scale check line
    sx, sy = (w - 100 * mm) / 2, y0 - 30 * mm
    c.line(sx, sy, sx + 100 * mm, sy)
    for i in range(0, 101, 10):
        t = 3 * mm if i % 50 == 0 else 1.5 * mm
        c.line(sx + i * mm, sy, sx + i * mm, sy + t)
    c.drawCentredString(w / 2, sy - 5 * mm, "Scale check: 100 mm")
    c.showPage()
    c.save()

if __name__ == "__main__":
    import os
    make(os.path.join(os.path.dirname(os.path.abspath(__file__)), "square-50mm-holes-40mm.pdf"))
