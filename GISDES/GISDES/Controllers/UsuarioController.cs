using GisDes.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace GisDes.Controllers
{
    public class UsuarioController : Controller
    {
        // GET: Usuario
        //Método que lista los Usuarios
        public ActionResult User()
        {
            using (GISDESEntity bd = new GISDESEntity())
            {
                List<Usuarios> lista = bd.Usuarios.ToList();
                return View(lista);
            }

        }

        // Método que crea un Usuario, adicionandolo a la base de datos, recibiendo como parámetro 
        //el objeto usuario

        public ActionResult CrearU(Usuarios u)
        {
            if (!ModelState.IsValid)
                return View();
            try
            {
                using (GISDESEntity bd = new GISDESEntity())
                {
                    bd.Usuarios.Add(u);
                    bd.SaveChanges();
                    return RedirectToAction("User");
                }
            }

            catch (Exception ex)
            {
                ModelState.AddModelError("Error al agregar el Usuario", ex);
                return View();
            }
        }


        //Método que modifica los datos de un usuario

        public ActionResult ModificarU(int Id)
        {
            try
            {
                using (GISDESEntity bd = new GISDESEntity())
                {
                    Usuarios u = bd.Usuarios.Find(Id);
                    return View(u);
                }

            }
            catch (Exception ex)
            {
                ModelState.AddModelError("Error al modificar el Usuario", ex);
                return View();
            }
        }



        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult ModificarU(Usuarios usuario)
        {
            try
            {
                using (GISDESEntity bd = new GISDESEntity())
                {
                    Usuarios usuarioNuevo = bd.Usuarios.Find(usuario.Id);
                    usuarioNuevo.NombreUsuario = usuario.NombreUsuario;
                    usuarioNuevo.Contraseña = usuario.Contraseña;
                    usuarioNuevo.Rol = usuario.Rol;
                    usuarioNuevo.Estado = usuario.Estado;
                    bd.SaveChanges();

                    return RedirectToAction("User");
                }
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("Error al almacenar el usuario modificado", ex);
                return View();
            }

        }


        //Método que elimina los datos de un usuario seleccionado
        public ActionResult EliminarU(int id)
        {
            try
            {
                using (GISDESEntity bd = new GISDESEntity())
                {
                    Usuarios u = bd.Usuarios.Find(id);
                    bd.Usuarios.Remove(u);
                    bd.SaveChanges();

                    return RedirectToAction("User");
                }
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("Error al almacenar el evento modificado", ex);
                return View();
            }
        }


    }
}