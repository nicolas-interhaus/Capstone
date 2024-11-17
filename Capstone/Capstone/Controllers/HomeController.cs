using Capstone.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace Capstone.Controllers
{
    public class HomeController : Controller
    {

        private readonly ApplicationDbContext _context;
        public IActionResult TestDatabaseConnection()
        {
            try
            {
                // Intenta ejecutar una consulta simple para verificar la conexión
                var test = _context.Database.CanConnect();
                if (test)
                {
                    return Content("Conexión a la base de datos exitosa");
                }
                else
                {
                    return Content("No se pudo conectar a la base de datos");
                }
            }
            catch (Exception ex)
            {
                return Content($"Error de conexión: {ex.Message}");
            }
        }
        public IActionResult Index()
        {
            return View();
        }
        public IActionResult Inicio_sesion()
        {
            return View();
        }
        public IActionResult Certificado()
        {
            return View();
        }
        public IActionResult Registro()
        {
            return View();
        }
        public IActionResult Registro_usuario()
        {
            return View();
        }
        public IActionResult Notificaciones()
        {
            return View();

        }
        public IActionResult Admin_contacto()
        {
            return View();
        }

        public IActionResult Admin_certificado()
        {
            return View();
        }
        public IActionResult Admin_notificaciones()
        {
            return View();
        }
        public IActionResult Admin_noticias()
        {
            return View();
        }
        public IActionResult Admin_usuarios()
        {
            return View();
        }
        public IActionResult Admin_vista()
        {
            return View();
        }
        public IActionResult Contacto()
        {
            return View();
        }
        public IActionResult Noticias()
        {
            return View();
        }


        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}