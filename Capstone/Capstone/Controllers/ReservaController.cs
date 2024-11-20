using Capstone.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

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
            var reservas = _context.Reservas.ToList(); // Suponiendo que tienes una entidad "Reserva"
            return View(reservas);
        }

        // GET: ReservaController/Details/5
        public ActionResult Details(int id)
        {
            return View();
        }

        // GET: ReservaController/Create
        public ActionResult Create()
        {
            return View();
        }
        // Crear reserva
        [HttpPost]
        public IActionResult CrearReserva(string nombre, DateTime fecha)
        {
            var reserva = new Reserva { Nombre = nombre, Fecha = fecha };
            _context.Reservas.Add(reserva);
            _context.SaveChanges();

            return RedirectToAction("Index");
        }

        // Editar reserva
        [HttpPost]
        public IActionResult EditarReserva(int id, string nombre, DateTime fecha)
        {
            var reserva = _context.Reservas.Find(id);
            if (reserva != null)
            {
                reserva.Nombre = nombre;
                reserva.Fecha = fecha;
                _context.SaveChanges();
            }
            return RedirectToAction("Index");
        }

        // Eliminar reserva
        [HttpPost]
        public IActionResult EliminarReserva(int id)
        {
            var reserva = _context.Reservas.Find(id);
            if (reserva != null)
            {
                _context.Reservas.Remove(reserva);
                _context.SaveChanges();
            }
            return RedirectToAction("Index");
        }
        // POST: ReservaController/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(IFormCollection collection)
        {
            try
            {
                return RedirectToAction(nameof(Index));
            }
            catch
            {
                return View();
            }
        }

        // GET: ReservaController/Edit/5
        public ActionResult Edit(int id)
        {
            return View();
        }

        // POST: ReservaController/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(int id, IFormCollection collection)
        {
            try
            {
                return RedirectToAction(nameof(Index));
            }
            catch
            {
                return View();
            }
        }

        // GET: ReservaController/Delete/5
        public ActionResult Delete(int id)
        {
            return View();
        }

        // POST: ReservaController/Delete/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Delete(int id, IFormCollection collection)
        {
            try
            {
                return RedirectToAction(nameof(Index));
            }
            catch
            {
                return View();
            }
        }
    }
}
