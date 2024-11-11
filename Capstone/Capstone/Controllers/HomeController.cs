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
        public IActionResult Eventos()
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