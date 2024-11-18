using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Capstone.Migrations
{
    public partial class ActualizacionNoticias2 : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Subtitulo",
                table: "noticia");

            migrationBuilder.RenameColumn(
                name: "FechaPublicacion",
                table: "noticia",
                newName: "Fecha_publicacion");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "Fecha_publicacion",
                table: "noticia",
                newName: "FechaPublicacion");

            migrationBuilder.AddColumn<string>(
                name: "Subtitulo",
                table: "noticia",
                type: "character varying(100)",
                maxLength: 100,
                nullable: false,
                defaultValue: "");
        }
    }
}
