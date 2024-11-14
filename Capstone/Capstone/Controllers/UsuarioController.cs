using Capstone.Models;
using Microsoft.AspNetCore.Mvc;
using Capstone.Modelo;

namespace Capstone.Controllers
{
    public class UsuarioController : Controller
    {
        private readonly ApplicationDbContext _context;

        public UsuarioController(ApplicationDbContext context)
        {
            _context = context;
        }

        // Acción para crear un nuevo usuario (GET)
        public IActionResult Create()
        {
            return View();
        }

        // Acción para crear un nuevo usuario (POST)
        [HttpPost]
        public IActionResult Create(Usuario usuario)
        {
            if (ModelState.IsValid)
            {
                _context.Usuarios.Add(usuario);
                _context.SaveChanges();
                return RedirectToAction("Admin_vista", "Home");
            }
            return View(usuario);
        }

        // Acción para editar un usuario (GET)
        public IActionResult Edit(int id)
        {
            var usuario = _context.Usuarios.Find(id);
            if (usuario == null)
            {
                return NotFound();
            }
            return View(usuario);
        }

        // Acción para editar un usuario (POST)
        [HttpPost]
        public IActionResult Edit(Usuario usuario)
        {
            if (ModelState.IsValid)
            {
                _context.Usuarios.Update(usuario);
                _context.SaveChanges();
                return RedirectToAction("Admin_Vista","Home");
            }
            return View(usuario);
        }

        // Acción para eliminar un usuario
        [HttpPost]
        public IActionResult Delete(int id)
        {
            var usuario = _context.Usuarios.Find(id);
            if (usuario != null)
            {
                _context.Usuarios.Remove(usuario);
                _context.SaveChanges();
            }
            return RedirectToAction("Admin_Vista","Home");
        }

        // Acción que redirige a la vista de administración
        public IActionResult AdminVista()
        {
            var usuarios = _context.Usuarios.ToList();
            return View("Admin_vista", usuarios);
        }
    }
}
