using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Capstone.Models
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

    }
}
