using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
namespace Capstone.Models
{
    public class JuntaVecinos
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public long Junta_vecino_id { get; set; }
        [Required]
        [StringLength(200)]
        public string Nombre_sector { get; set; }
        [Required]
        public string Direccion { get; set; }
        public JuntaVecinos(long Junta_vecino_id, string Nombre_sector, string Direccion)
        {
            this.Junta_vecino_id = Junta_vecino_id;
            this.Nombre_sector = Nombre_sector;
            this.Direccion = Direccion;
        }
    }
}
