namespace Capstone.Models
{
    public class Resumen_pendientes
    {
        public Int64 Resumen_id { get; set; }
        public DateTime Fecha_ingreso { get; set; }
        public TextWriter Periodo { get; set; }
        public string Rut { get; set; }
        public BinaryWriter Aprobacion { get; set; }
        public Resumen_pendientes(Int64 Resumen_id, DateTime Fecha_ingreso, TextWriter Periodo, string Rut, BinaryWriter Aprobacion)
        {
            this.Resumen_id = Resumen_id;
            this.Fecha_ingreso = Fecha_ingreso;
            this.Periodo = Periodo;
            this.Rut = Rut;
            this.Aprobacion = Aprobacion;
        }
    }
}
