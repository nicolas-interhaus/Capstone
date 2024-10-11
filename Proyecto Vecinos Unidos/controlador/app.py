from flask import Flask, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route('/generar-certificado', methods=['POST'])
def generar_certificado():
    nombre = request.form['nombre']
    rut = request.form['rut']
    direccion = request.form['direccion']
    comuna = request.form['comuna']
    fecha = request.form['fecha']

    # Crear un PDF con FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Agregar contenido al PDF
    pdf.cell(200, 10, txt="Certificado de Residencia", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Nombre: {nombre}", ln=True)
    pdf.cell(200, 10, txt=f"RUT: {rut}", ln=True)
    pdf.cell(200, 10, txt=f"Dirección: {direccion}", ln=True)
    pdf.cell(200, 10, txt=f"Comuna: {comuna}", ln=True)
    pdf.cell(200, 10, txt=f"Fecha de emisión: {fecha}", ln=True)

    # Generar el PDF en memoria
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    # Devolver el archivo PDF al usuario
    return send_file(pdf_output, as_attachment=True, download_name="certificado_residencia.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
