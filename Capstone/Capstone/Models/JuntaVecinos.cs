using System;
namespace Capstone.Models
{
    public class JuntaVecinos
    {
        public Int64 Junta_vecino_id { get; set; }
        public string Nombre_sector { get; set; }
        public TextWriter Direccion { get; set; }
        public JuntaVecinos(Int64 Junta_vecino_id, string Nombre_sector, TextWriter Direccion)
        {
            this.Junta_vecino_id = Junta_vecino_id;
            this.Nombre_sector = Nombre_sector;
            this.Direccion = Direccion;
        }
    }
}
