using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Capstone.Modelo
{
    [Table("noticias")]
    public class Noticias
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]

        public Int64 Noticia_id { get; set; }
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

        // Constructor
        public Noticias(string titulo, Int64 Noticia_id, string subtitulo,  string contenido, string autor, DateTime fechaPublicacion)
        {
            this.Titulo = titulo;
            this.Noticia_id = Noticia_id;
            this.Subtitulo = subtitulo;
            this.Detalle = contenido;
            this.Autor = autor;
            this.FechaPublicacion = fechaPublicacion;
        }

        // Método para representar el objeto como una cadena de texto
        public override string ToString()
        {
            return $"{Titulo} - {Autor} ({FechaPublicacion.ToString("dd/MM/yyyy")})";
        }
    }
}
