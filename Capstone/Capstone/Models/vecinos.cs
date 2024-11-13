using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
namespace Capstone.Modelo
{
    [Table("vecinos")]
    public class Vecinos
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }

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
        public string Rut { get; set; }

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
        [StringLength(100)]
        public string? Email { get; set; }
        public Vecinos(int id, string? nombres, string? apellidoPaterno, string? apellidoMaterno, DateTime fechaNacimiento, string rut, int edad, string? genero, string? direccion, string? comuna, string? email)
        {
            Id = id;
            Nombres = nombres;
            ApellidoPaterno = apellidoPaterno;
            ApellidoMaterno = apellidoMaterno;
            FechaNacimiento = fechaNacimiento;
            Rut = rut;
            Edad = edad;
            Genero = genero;
            Direccion = direccion;
            Comuna = comuna;
            Email = email;
        }

        public override string ToString()
        {
            return $"{Nombres} {ApellidoPaterno}";
        }
    }
}
