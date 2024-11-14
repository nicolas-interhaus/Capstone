using Capstone.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace Capstone.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
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