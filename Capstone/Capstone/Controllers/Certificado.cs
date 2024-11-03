using Microsoft.AspNetCore.Mvc;
using Npgsql;
using System;

namespace Capstone.Controllers
{
    public class CertificadosController : Controller
    {
        // Método para mostrar el formulario
        public IActionResult GenerarCertificado()
        {
            return View();
        }

        // Método para manejar la petición POST
        [HttpPost]
        public IActionResult GenerarCertificado(string nombre, string rut, string direccion, string comuna, DateTime fecha)
        {
            string connectionString = "Host=localhost;Database=capstone;Username=Postgres;Password=admin";

            using (var conn = new NpgsqlConnection(connectionString))
            {
                try
                {
                    conn.Open();
                    string query = "INSERT INTO certificados_residencia (nombre, rut, direccion, comuna, fecha_emision) VALUES (@nombre, @rut, @direccion, @comuna, @fecha)";

                    using (var cmd = new NpgsqlCommand(query, conn))
                    {
                        cmd.Parameters.AddWithValue("nombre", nombre);
                        cmd.Parameters.AddWithValue("rut", rut);
                        cmd.Parameters.AddWithValue("direccion", direccion);
                        cmd.Parameters.AddWithValue("comuna", comuna);
                        cmd.Parameters.AddWithValue("fecha", fecha);

                        cmd.ExecuteNonQuery();
                    }

                    ViewBag.Message = "Certificado generado exitosamente";
                }
                catch (Exception ex)
                {
                    ViewBag.Message = $"Error al generar el certificado: {ex.Message}";
                }
            }

            return View();
        }
    }
}
