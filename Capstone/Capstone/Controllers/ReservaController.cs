using Microsoft.AspNetCore.Mvc;
using Capstone.Models;

namespace Capstone.Controllers
{
    public class ReservaController : Controller
    {
        private readonly ApplicationDbContext _context;

        public ReservaController(ApplicationDbContext context)
        {
            _context = context;
        }

        // Cargar todas las reservas
        public IActionResult Index()
        {
            var reservas = _context.Reserva.ToList(); // Suponiendo que tienes una entidad "Reserva"
            return View(reservas);
        }

        // Crear reserva
        [HttpPost]
        public IActionResult CrearReserva(string nombre, bool semanal, string rut_usuario, bool aprobacion)
        {
            var reserva = new Reserva { Nombre = nombre, Semanal = semanal, Rut_usuario = rut_usuario, Aprobacion = aprobacion};
            _context.Reserva.Add(reserva);
            _context.SaveChanges();

            return RedirectToAction("Index");
        }

        // Editar reserva
        [HttpPost]
        public IActionResult EditarReserva(int id, string nombre, bool semanal, string rut_usuario, bool aprobacion)
        {
            var reserva = _context.Reserva.Find(id);
            if (reserva != null)
            {
                reserva.Nombre = nombre;
                reserva.Semanal = semanal;
                reserva.Rut_usuario = rut_usuario;
                reserva.Aprobacion = aprobacion;
                _context.SaveChanges();
            }
            return RedirectToAction("Index");
        }

        // Eliminar reserva
        [HttpPost]
        public IActionResult EliminarReserva(int id)
        {
            var reserva = _context.Reserva.Find(id);
            if (reserva != null)
            {
                _context.Reserva.Remove(reserva);
                _context.SaveChanges();
            }
            return RedirectToAction("Index");
        }
    }
}
