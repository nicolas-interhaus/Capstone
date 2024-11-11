using Microsoft.AspNetCore.Mvc;

using Capstone.Modelo; // Asegúrate de usar el espacio de nombres adecuado de tu modelo
using System.Linq;
using Capstone.Models;

namespace Capstone.Controllers
{
    public class NoticiasController : Controller
    {
        private readonly ApplicationDbContext _context; // Asegúrate de que esta sea tu clase de contexto de base de datos

        public NoticiasController(ApplicationDbContext context)
        {
            _context = context;
        }

        public IActionResult Index()
        {
            var noticias = _context.Noticias.ToList(); // Asegúrate de que 'Noticias' sea el nombre de la tabla o DbSet de noticias en tu contexto a
            return View(noticias);
        }
    }
}
