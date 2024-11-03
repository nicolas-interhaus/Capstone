using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Capstone.Modelo
{
    public class Usuario
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }

        [Required]
        [StringLength(12)]
        public string? Rut { get; set; }

        [Required]
        [StringLength(100)]
        public string? Nombres { get; set; }

        [Required]
        [StringLength(100)]
        public string? ApellidoPaterno { get; set; }

        [Required]
        [StringLength(100)]
        public string? ApellidoMaterno { get; set; }

        [Required]
        public DateTime FechaNacimiento { get; set; }

        [Required]
        public int Edad { get; set; }

        [Required]
        [StringLength(10)]
        public string? Genero { get; set; }

        [Required]
        [StringLength(200)]
        public string? Direccion { get; set; }

        [Required]
        [StringLength(100)]
        public string? Comuna { get; set; }

        [Required]
        [StringLength(50)]
        public string? Cargo { get; set; }

        [Required]
        [StringLength(100)]
        public string? Email { get; set; }

        public override string ToString()
        {
            return $"{Nombres} {ApellidoPaterno}";
        }
    }
}
