using iText.Kernel.Pdf;
using iText.Layout;
using iText.Layout.Element;
using Microsoft.AspNetCore.Mvc;
using System.IO;

namespace Capstone.Controllers
{
    public class CertificadosController : Controller
    {
        [HttpPost]
        public IActionResult GenerarCertificado(string nombre, string rut, string direccion, string comuna, DateTime fecha)
        {
            // Ruta temporal para guardar el archivo PDF
            string pdfPath = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "certificados", $"Certificado_{rut}.pdf");

            // Crea el directorio si no existe
            Directory.CreateDirectory(Path.GetDirectoryName(pdfPath));

            // Generar el PDF
            using (var writer = new PdfWriter(pdfPath))
            {
                var pdf = new PdfDocument(writer);
                var document = new Document(pdf);

                // Añadir contenido al PDF
                document.Add(new Paragraph("Certificado de Residencia").SetFontSize(18));
                document.Add(new Paragraph($"Nombre: {nombre}"));
                document.Add(new Paragraph($"RUT: {rut}"));
                document.Add(new Paragraph($"Dirección: {direccion}"));
                document.Add(new Paragraph($"Comuna: {comuna}"));
                document.Add(new Paragraph($"Fecha de emisión: {fecha.ToString("dd/MM/yyyy")}"));

                document.Close();
            }

            // Mensaje de éxito
            ViewBag.Message = "El certificado se ha generado exitosamente.";
            ViewBag.PdfUrl = $"/certificados/Certificado_{rut}.pdf";

            return View();
        }
    }
}
