using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Capstone.Models
{
    [Table("noticia")]
    public class Noticias
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public long Noticia_id { get; set; }

        [Required]
        public string Titulo { get; set; }


        [Required]
        [StringLength(100)]
        public string Detalle { get; set; }

        [Required]
        [StringLength(100)]
        public string Autor { get; set; }

        [Required]
        public DateTime Fecha_publicacion { get; set; }

        // Constructor vacío (necesario para Entity Framework y otros usos)
        public Noticias() { }

        // Constructor parametrizado
        public Noticias(string titulo, long noticia_id,  string detalle, string autor, DateTime Fecha_publicacion)
        {
            Titulo = titulo;
            Noticia_id = noticia_id;
            Detalle = detalle;
            Autor = autor;
            this.Fecha_publicacion = Fecha_publicacion;
        }

        // Método para representar el objeto como una cadena de texto
        public override string ToString()
        {
            return $"{Titulo} - {Autor} ({Fecha_publicacion:dd/MM/yyyy})";
        }
    }
}
