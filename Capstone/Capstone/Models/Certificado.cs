using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Capstone.Models
{
    public class Certificado
    {
        public Int32 Id_certificado { get; set; }
        public string Cert_nombre { get; set; }
        public string Cert_rut { get; set; }
        public string Cert_direccion { get; set; }
        public string Cert_comuna { get; set; }

        public DateTime Cert_Fecha_emision { get; set; }

        public FileAccess Documentos { get; set; }

    }
}
