using System;
namespace Capstone.Models
{
    public class Usuario
    {
        public Int64 Usuario_id { get; set; }
        public string Usuario { get; set; }
        public string Contraseña { get; set; }
        public string Cargo { get; set; }
        public string Perfil { get; set; }
        public DateTime Fecha_registro { get; set; }
        public Usuario(Int64 Usuario_id, string Usuario, string Contraseña, string Cargo, string Perfil, DateTime Fecha_registro)
        {
            this.Usuario_id = Usuario_id;
            this.Usuario = Usuario;
            this.Contraseña = Contraseña;
            this.Cargo = Cargo;
            this.Perfil = Perfil;
            this.Fecha_registro = Fecha_registro;

        }
    }
}
