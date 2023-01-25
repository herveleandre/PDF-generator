import pandas as pd
import streamlit as st
from fpdf import FPDF

pdf = FPDF(orientation='P', unit="mm", format="A4")

df = pd.read_csv('topics.csv')

# Master Page Adding
for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=20)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # adding a line
    pdf.line(10, 21, 200, 21)


    # Iterate on Ranges
    for i in range(row["Pages"]-1):
        pdf.add_page()
pdf.output("Output.pdf")
