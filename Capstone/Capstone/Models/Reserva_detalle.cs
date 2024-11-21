using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Capstone.Models
{
    public class Reserva_detalle
    {
        [Required]
        public DateTime Fecha { get; set; }
        public string? Bloque { get; set; }
        public Reserva_detalle() { }
        public Reserva_detalle(DateTime fecha, string bloque)
        {
            this.Fecha = fecha;
            this. Bloque = bloque;
        }
    }
}
