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
        public DbSet<Usuario> Usuarios { get; set; }
    }
}
