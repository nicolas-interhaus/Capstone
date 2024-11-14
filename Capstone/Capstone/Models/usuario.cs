using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
namespace Capstone.Models
{
    [Table("usuario")]
    public class Usuario
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        [Column("usuario_id")]
        public long Usuario_id { get; set; }
        [Required]
        [StringLength(200)]
        [Column("usuario")]
        public string? User { get; set; }
        [Required]
        [StringLength(200)]
        [Column("contraseña")]
        public string? Contraseña { get; set; }
        [Required]
        [StringLength(200)]
        [Column("cargo")]
        public string? Cargo { get; set; }
        [Required]
        [StringLength(200)]
        [Column("perfil")]
        public string? Perfil { get; set; }
        [Required]
        [Column("fecha_registro")]
        public DateTime Fecha_registro { get; set; }
        public Usuario() { }
        public Usuario(long Usuario_id, string Usuario, string Contraseña, string Cargo, string Perfil, DateTime Fecha_registro)
        {
            this.Usuario_id = Usuario_id;
            User = Usuario;
            this.Contraseña = Contraseña;
            this.Cargo = Cargo;
            this.Perfil = Perfil;
            this.Fecha_registro = Fecha_registro;

        }
    }
}
