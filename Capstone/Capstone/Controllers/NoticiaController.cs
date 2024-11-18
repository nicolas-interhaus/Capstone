using Microsoft.AspNetCore.Mvc;
using Capstone.Models;

namespace Capstone.Controllers
{
    public class NoticiasController : Controller
    {
        private readonly ApplicationDbContext _context;

        public NoticiasController(ApplicationDbContext context)
        {
            _context = context;
        }

        

        [HttpPost]
        public IActionResult PublicarNoticia(long id)
        {
            var noticia = _context.Noticias.Find(id);
            if (noticia != null)
            {
                // Aquí puedes agregar lógica para marcar la noticia como publicada
                // Por ejemplo, agregar una columna `Estado` en la base de datos
                _context.SaveChanges();
            }
            return RedirectToAction("Admin_noticias");
        }

        [HttpPost]
        public IActionResult InsertarNoticiasPrueba()
        {
            var noticiasPrueba = new List<Noticias>
    {
            new Noticias
            {
                Titulo = "Primera Noticia",
                Noticia_id = 1,
                Detalle = "Este es un detalle de prueba.",
                Autor = "Admin",
                Fecha_publicacion = DateTime.UtcNow
            },
            new Noticias
            {
                Titulo = "Segunda Noticia",
                Noticia_id = 2,
                Detalle = "Este es otro detalle de prueba.",
                Autor = "Admin2",
                Fecha_publicacion = DateTime.UtcNow
            }
        };


            _context.Noticias.AddRange(noticiasPrueba);
            _context.SaveChanges();

            return RedirectToAction("Admin_noticias");
        }
        public IActionResult Admin_noticias()
        {
            var noticias = _context.Noticias.ToList();
            return View(noticias);
        }


        [HttpPost]
        public IActionResult RechazarNoticia(long id)
        {
            var noticia = _context.Noticias.Find(id);
            if (noticia != null)
            {
                // Lógica para rechazar la noticia (puede incluir eliminarla o marcarla como rechazada)
                _context.Noticias.Remove(noticia);
                _context.SaveChanges();
            }
            return RedirectToAction("Admin_noticias");
        }
    }
}
