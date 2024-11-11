using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Capstone.Models
{
    public class Certificado
    {
        public Int32 Id { get; set; }
        public string Nombre { get; set; }
        public string Direccion { get; set; }

        public DateTime Fecha_emision { get; set; }

        public FileAccess Documentos { get; set; }

    }
}
