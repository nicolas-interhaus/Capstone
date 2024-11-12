using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
namespace Capstone.Models
{
    public class JuntaVecinos
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public Int64 Junta_vecino_id { get; set; }
        [Required]
        [StringLength(200)]
        public string Nombre_sector { get; set; }
        [Required]
        public TextWriter Direccion { get; set; }
        public JuntaVecinos(Int64 Junta_vecino_id, string Nombre_sector, TextWriter Direccion)
        {
            this.Junta_vecino_id = Junta_vecino_id;
            this.Nombre_sector = Nombre_sector;
            this.Direccion = Direccion;
        }
    }
}
