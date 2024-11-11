using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Capstone.Modelo
{
    [Table("notificaciones")]
    public class notificaciones
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int IdEvento { get; set; }

        [Required]
        [StringLength(200)]
        public  string? NombreEvento { get; set; }

        [Required]
        public DateTime FechaRecepcion { get; set; }

        [StringLength(200)]
        public string? Detalle { get; set; }

        [Required]
        [StringLength(200)]
        public string? Correo { get; set; }

        [Required]
        public BinaryReader Aprobacion { get; set; }


        public override string ToString()
        {
            return $"{NombreEvento}";
        }
    }
}
