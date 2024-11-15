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
