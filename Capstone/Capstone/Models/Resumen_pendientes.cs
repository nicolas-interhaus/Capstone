using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
namespace Capstone.Models
{
    public class Resumen_pendientes
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public long Resumen_id { get; set; }
        [Required]
        public DateTime Fecha_ingreso { get; set; }
        public DateTime FechaInicio { get; set; } // Inicio del período
        public DateTime FechaFin { get; set; }
        [Required]
        [StringLength(200)]
        public string Rut { get; set; }
        [Required]
        public byte[] Aprobacion { get; set; }
        public Resumen_pendientes(long Resumen_id, DateTime Fecha_ingreso, DateTime FechaInicio, DateTime FechaFin, string Rut, byte[] Aprobacion)
        {
            this.Resumen_id = Resumen_id;
            this.Fecha_ingreso = Fecha_ingreso;
            this.FechaInicio = FechaInicio;
            this.FechaFin = FechaFin;
            this.Rut = Rut;
            this.Aprobacion = Aprobacion;
        }
    }
}
