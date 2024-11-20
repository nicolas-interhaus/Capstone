using Microsoft.EntityFrameworkCore;

namespace Capstone.Models // Usa el mismo namespace de tus modelos
{
    public class ApplicationDbContext : DbContext
    {
#pragma warning disable CS8618 // Un campo que no acepta valores NULL debe contener un valor distinto de NULL al salir del constructor. Considere la posibilidad de declararlo como que admite un valor NULL.
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
#pragma warning restore CS8618 // Un campo que no acepta valores NULL debe contener un valor distinto de NULL al salir del constructor. Considere la posibilidad de declararlo como que admite un valor NULL.
            : base(options)
        {
        }

        // Agrega DbSet para cada una de tus entidades, por ejemplo:
        public DbSet<Vecinos> Vecinos { get; set; }
        public DbSet<Noticias> Noticias { get; set; }
        public DbSet<JuntaVecinos> JuntaVecinos { get; set; }
        public DbSet<notificaciones> Notificaciones { get; set; }
        public DbSet<Resumen_pendientes> Resumen_Pendientes { get; set; }
        public DbSet<Usuario> Usuarios { get; set; }
        public DbSet<Certificado> Certificados { get; set; }
        public object Reservas { get; internal set; }

        //internal void SaveChanges()
        //{
        //    throw new NotImplementedException();
        //}
    }
}
