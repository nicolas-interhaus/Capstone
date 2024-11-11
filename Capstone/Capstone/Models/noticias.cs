using System;

namespace Capstone.Modelo
{
    public class Noticias
    {
        public string Titulo { get; set; }
        public string Id { get; set; }
        public string Subtitulo { get; set; }
        public string Detalle { get; set; }
        public string Autor { get; set; }
        public DateTime FechaPublicacion { get; set; }

        // Constructor
        public Noticias(string titulo, string id, string subtitulo,  string contenido, string autor, DateTime fechaPublicacion)
        {
            Titulo = titulo;
            id = id;
            Subtitulo = subtitulo;
            Detalle = contenido;
            Autor = autor;
            FechaPublicacion = fechaPublicacion;
        }

        // Método para representar el objeto como una cadena de texto
        public override string ToString()
        {
            return $"{Titulo} - {Autor} ({FechaPublicacion.ToString("dd/MM/yyyy")})";
        }
    }
}
