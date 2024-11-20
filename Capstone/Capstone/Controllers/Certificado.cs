using Microsoft.AspNetCore.Mvc;
using PdfSharp.Drawing;
using PdfSharp.Pdf;
using System.IO;

namespace Capstone.Controllers
{
    public class CertificadosController : Controller
    {
        [HttpGet]
        public IActionResult GenerarCertificado()
        {
            return View(); // Asegúrate de que la vista "GenerarCertificado.cshtml" exista.
        }
        [HttpPost]
        public IActionResult GenerarCertificado(string nombre, string rut, string direccion, string comuna, string fecha)
        {
            // Crear un documento PDF
            PdfDocument documento = new PdfDocument();
            documento.Info.Title = "Certificado de Residencia";

            // Crear una página
            PdfPage pagina = documento.AddPage();

            // Crear un gráfico para dibujar texto en la página
            XGraphics gfx = XGraphics.FromPdfPage(pagina);

            // Configurar fuente básica
            XFont fuente = new XFont("Arial", 12);

            // Dibujar contenido (datos en bruto)
            gfx.DrawString("Certificado de Residencia", fuente, XBrushes.Black, new XPoint(40, 40));
            gfx.DrawString($"Nombre: {nombre}", fuente, XBrushes.Black, new XPoint(40, 80));
            gfx.DrawString($"RUT: {rut}", fuente, XBrushes.Black, new XPoint(40, 100));
            gfx.DrawString($"Dirección: {direccion}", fuente, XBrushes.Black, new XPoint(40, 120));
            gfx.DrawString($"Comuna: {comuna}", fuente, XBrushes.Black, new XPoint(40, 140));
            gfx.DrawString($"Fecha de emisión: {fecha}", fuente, XBrushes.Black, new XPoint(40, 160));

            // Guardar el PDF en un MemoryStream
            using (MemoryStream stream = new MemoryStream())
            {
                documento.Save(stream);
                stream.Position = 0;

                // Retornar el archivo PDF como respuesta
                return File(stream.ToArray(), "application/pdf", "Certificado_Residencia.pdf");
            }

        }
    }
}
