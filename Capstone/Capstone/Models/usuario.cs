using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
namespace Capstone.Models
{
    public class Usuario
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public Int64 Usuario_id { get; set; }
        [Required]
        [StringLength(200)]
        public string User { get; set; }
        [Required]
        [StringLength(200)]
        public string Contraseña { get; set; }
        [Required]
        [StringLength(200)]
        public string Cargo { get; set; }
        [Required]
        [StringLength(200)]
        public string Perfil { get; set; }
        [Required]
        public DateTime Fecha_registro { get; set; }
        public Usuario(Int64 Usuario_id, string Usuario, string Contraseña, string Cargo, string Perfil, DateTime Fecha_registro)
        {
            this.Usuario_id = Usuario_id;
            this.User = Usuario;
            this.Contraseña = Contraseña;
            this.Cargo = Cargo;
            this.Perfil = Perfil;
            this.Fecha_registro = Fecha_registro;

        }
    }
}
