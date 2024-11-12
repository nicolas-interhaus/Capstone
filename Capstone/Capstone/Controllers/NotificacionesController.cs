using Microsoft.AspNetCore.Mvc;

namespace Capstone.Controllers
{
    public class NotificacionesController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
