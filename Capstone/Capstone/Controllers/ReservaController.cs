using Capstone.Models;
using Microsoft.AspNetCore.Mvc;
namespace Capstone.Controllers
{
    public class ReservaController : Controller
    {
        public ApplicationDbContext Context { get; }

        public ReservaController(ApplicationDbContext context)
        {
            Context = context;
        }

        // Cargar todas las reservas
        public IActionResult Index()
        {
            var reservas = Context.Reservas.ToList(); // Suponiendo que tienes una entidad "Reserva"
            return View(reservas);
        }

        

        // GET: ReservaController/Create
        public ActionResult Create()
        {
            return View();
        }
        // Crear reserva
        [HttpPost]
        public IActionResult CrearReserva(string nombre, bool semanal, string rut_usuario, bool aprobacion)
        {
            var reserva = new Reserva { Nombre = nombre, Semanal = semanal, Rut_usuario = rut_usuario, Aprobacion = aprobacion};
            Context.Reservas.Add(reserva);
            Context.SaveChanges();

            return RedirectToAction("Index");
        }

        // Editar reserva
        [HttpPost]
        public IActionResult EditarReserva(int id, string nombre, bool semanal, string rut_usuario, bool aprobacion)
        {
            var reserva = Context.Reservas.Find(id);
            if (reserva != null)
            {
                reserva.Nombre = nombre;
                reserva.Semanal = semanal;
                Context.SaveChanges();
            }
            return RedirectToAction("Index");
        }

        // Eliminar reserva
        [HttpPost]
        public IActionResult EliminarReserva(int id)
        {
            var reserva = Context.Reservas.Find(id);
            if (reserva != null)
            {
                Context.Reservas.Remove(reserva);
                Context.SaveChanges();
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
