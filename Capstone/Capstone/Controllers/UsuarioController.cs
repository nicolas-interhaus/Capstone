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

        // Método para mostrar el formulario de creación de usuario
        [HttpGet]
        public IActionResult Create()
        {
            return View();
        }

        // Método para recibir datos y guardarlos en la base de datos
        [HttpPost]
        public IActionResult Create(Usuario usuario)
        {
            if (ModelState.IsValid)
            {
                _context.Usuarios.Add(usuario);
                _context.SaveChanges();
                return RedirectToAction("Index"); // Puedes redirigir a una vista de éxito
            }
            return View(usuario);
        }
    }
}
