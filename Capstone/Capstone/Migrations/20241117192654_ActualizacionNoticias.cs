using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Capstone.Migrations
{
    public partial class ActualizacionNoticias : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropPrimaryKey(
                name: "PK_noticias",
                table: "noticias");

            migrationBuilder.RenameTable(
                name: "noticias",
                newName: "noticia");

            migrationBuilder.AddPrimaryKey(
                name: "PK_noticia",
                table: "noticia",
                column: "Noticia_id");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropPrimaryKey(
                name: "PK_noticia",
                table: "noticia");

            migrationBuilder.RenameTable(
                name: "noticia",
                newName: "noticias");

            migrationBuilder.AddPrimaryKey(
                name: "PK_noticias",
                table: "noticias",
                column: "Noticia_id");
        }
    }
}
