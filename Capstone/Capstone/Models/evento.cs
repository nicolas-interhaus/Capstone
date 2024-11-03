using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Capstone.Modelo
{
    [Table("eventos")]
    public class Evento
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int IdEvento { get; set; }

        [Required]
        [StringLength(200)]
        public  string? NombreEvento { get; set; }

        [Required]
        public DateTime FechaEvento { get; set; }

        [StringLength(200)]
        public string? Patrocinadores { get; set; }

        [Required]
        [StringLength(200)]
        public string? DireccionEvento { get; set; }

        [Required]
        public float PrecioEvento { get; set; }

        [Required]
        public int CapacidadEvento { get; set; }

        public override string ToString()
        {
            return $"{NombreEvento}";
        }
    }
}
