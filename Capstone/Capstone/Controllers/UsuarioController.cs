using Capstone.Modelo;
using Capstone.Models;
using Microsoft.AspNetCore.Mvc;

namespace Capstone.Controllers
{
    public class UsuarioController : Controller
    {
        private readonly ApplicationDbContext _context;

        public UsuarioController(ApplicationDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Create(Vecinos vecinos)
        {
            vecinos.FechaNacimiento = DateTime.SpecifyKind(vecinos.FechaNacimiento, DateTimeKind.Utc);
            if (ModelState.IsValid)
            {
                _context.Usuarios.Add(vecinos);
                _context.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(vecinos);
        }
    }
}
