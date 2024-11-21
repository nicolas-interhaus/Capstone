using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Capstone.Models
{
    public class Reserva
    {
        public string? Nombre { get; set; }
        public bool Semanal { get; set; }
        public string ? Rut_usuario { get; set; }
        public bool Aprobacion { get; set; }
        public Reserva() { }
        public Reserva(string Nombre, bool Semanal, string Rut_usuario, bool Aprobacion ) {
            this.Nombre = Nombre;
            this.Semanal = Semanal;
            this.Rut_usuario = Rut_usuario;
            this.Aprobacion = Aprobacion;

        }
    }
}