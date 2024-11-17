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
        public string Subtitulo { get; set; }

        [Required]
        [StringLength(100)]
        public string Detalle { get; set; }

        [Required]
        [StringLength(100)]
        public string Autor { get; set; }

        [Required]
        public DateTime FechaPublicacion { get; set; }

        // Constructor vacío (necesario para Entity Framework y otros usos)
        public Noticias() { }

        // Constructor parametrizado
        public Noticias(string titulo, long noticia_id, string subtitulo, string detalle, string autor, DateTime fechaPublicacion)
        {
            Titulo = titulo;
            Noticia_id = noticia_id;
            Subtitulo = subtitulo;
            Detalle = detalle;
            Autor = autor;
            FechaPublicacion = fechaPublicacion;
        }

        // Método para representar el objeto como una cadena de texto
        public override string ToString()
        {
            return $"{Titulo} - {Autor} ({FechaPublicacion:dd/MM/yyyy})";
        }
    }
}
