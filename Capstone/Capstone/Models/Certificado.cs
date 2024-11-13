using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Capstone.Modelo
{
    [Table("certificado_residencia")]
    public class Certificado
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public Int32 Id_certificado { get; set; }
        [Required]
        [StringLength(200)]
        public string Cert_nombre { get; set; }
        [Required]
        [StringLength(200)]
        public string Cert_rut { get; set; }
        [Required]
        [StringLength(200)]
        public string Cert_direccion { get; set; }
        [Required]
        [StringLength(200)]
        public string Cert_comuna { get; set; }
        [Required]

        public DateTime Cert_Fecha_emision { get; set; }
        [Required]

        public FileAccess Documentos { get; set; }
        public Certificado(int id_certificado, string cert_nombre, string cert_rut, string cert_direccion, string cert_comuna, DateTime cert_Fecha_emision, FileAccess documentos)
        {
            Id_certificado = id_certificado;
            Cert_nombre = cert_nombre;
            Cert_rut = cert_rut;
            Cert_direccion = cert_direccion;
            Cert_comuna = cert_comuna;
            Cert_Fecha_emision = cert_Fecha_emision;
            Documentos = documentos;
        }
    }
}
