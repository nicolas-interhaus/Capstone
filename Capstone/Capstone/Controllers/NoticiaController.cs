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

        public IActionResult Admin_noticias()
        {
            // Recupera todas las noticias de la base de datos
            var noticias = _context.Noticias.ToList();
            return View(noticias); // Pasa la lista de noticias a la vista
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

        public IActionResult Admin_noticias()
        {
            var noticias = _context.Noticias.ToList();

            if (noticias == null || !noticias.Any())
            {
                Console.WriteLine("No se encontraron noticias.");
            }
            else
            {
                Console.WriteLine($"Se encontraron {noticias.Count} noticias.");
            }

            return View(noticias);
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
        public IActionResult InsertarNoticiasPrueba()
        {
            var noticiasPrueba = new List<Noticias>
    {
            new Noticias
            {
                Titulo = "Primera Noticia",
                Noticia_id = 1,
                Subtitulo = "Subtítulo de prueba",
                Detalle = "Este es un detalle de prueba.",
                Autor = "Admin",
                FechaPublicacion = DateTime.Now
            },
            new Noticias
            {
                Titulo = "Segunda Noticia",
                Noticia_id = 2,
                Subtitulo = "Otro subtítulo de prueba",
                Detalle = "Este es otro detalle de prueba.",
                Autor = "Admin2",
                FechaPublicacion = DateTime.Now
            }
        };

            _context.Noticias.AddRange(noticiasPrueba);
            _context.SaveChanges();

            return RedirectToAction("Admin_noticias");
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
