namespace Capstone.Models
{
    internal class Reserva
    {
        public string? Nombre { get; set; }
        public DateTime Fecha { get; set; }
        public Reserva() { }
        public Reserva(string? nombre, DateTime fecha)
        {
            Nombre = nombre;
            Fecha = fecha;
        }
    }
}