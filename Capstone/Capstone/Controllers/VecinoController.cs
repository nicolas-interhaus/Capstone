using Capstone.Modelo;
using Capstone.Models;
using Microsoft.AspNetCore.Mvc;

namespace Capstone.Controllers
{
    public class VecinoController : Controller
    {
        private readonly ApplicationDbContext _context;

        public VecinoController(ApplicationDbContext context)
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
                _context.SaveChanges();
                return RedirectToAction("Registro_usuario", "Home");
            }
            return View(vecinos);
        }
    }
}
