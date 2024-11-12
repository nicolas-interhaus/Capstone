using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
namespace Capstone.Models
{
    public class Resumen_pendientes
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public Int64 Resumen_id { get; set; }
        [Required]
        public DateTime Fecha_ingreso { get; set; }
        public TextWriter Periodo { get; set; }
        [Required]
        [StringLength(200)]
        public string Rut { get; set; }
        [Required]
        public BinaryWriter Aprobacion { get; set; }
        public Resumen_pendientes(Int64 Resumen_id, DateTime Fecha_ingreso, TextWriter Periodo, string Rut, BinaryWriter Aprobacion)
        {
            this.Resumen_id = Resumen_id;
            this.Fecha_ingreso = Fecha_ingreso;
            this.Periodo = Periodo;
            this.Rut = Rut;
            this.Aprobacion = Aprobacion;
        }
    }
}
