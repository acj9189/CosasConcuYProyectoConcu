using GisDes.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace GisDes.Controllers
{
    public class PersonaExternaController : Controller
    {
        // GET: PersonaExterna
        public ActionResult Index()
        {
            using (GISDESEntity bd = new Models.GISDESEntity())
            {
                List<PersonaExterna> lista = bd.PersonaExterna.Where(ev => ev.Estado == true).ToList();
                return View(lista);
            }
        }


        public ActionResult Agregar(PersonaExterna e)
        {
            if (!ModelState.IsValid)
                return View();
            try
            {
                using (GISDESEntity bd = new GISDESEntity())
                {
                    e.Estado = true;
                    bd.PersonaExterna.Add(e);
                    bd.SaveChanges();
                    return RedirectToAction("Index");
                }
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("Error al agregar a la persona externa", ex);
                return View();
            }

        }


        public ActionResult Modificar(int id)
        {
            try
            {
                using (GISDESEntity db = new GISDESEntity())
                {
                    PersonaExterna personaExterna = db.PersonaExterna.Find(id);
                    return View(personaExterna);

                }
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("Error al modificar la persona externa", ex);
                return View();
            }
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Modificar(PersonaExterna persona)
        {
            try
            {
                using (GISDESEntity db = new GISDESEntity())
                {
                    PersonaExterna personaExternaNuevo = db.PersonaExterna.Find(persona.Id);
                    personaExternaNuevo.Nombre = persona.Nombre;
                    personaExternaNuevo.Fechaingreso = persona.Fechaingreso;
                    personaExternaNuevo.Ocupacion = persona.Ocupacion;
                    personaExternaNuevo.Apellido = persona.Apellido;
                    personaExternaNuevo.Estado = persona.Estado;
                    personaExternaNuevo.Cedula = persona.Cedula;

                    db.SaveChanges();

                    return RedirectToAction("Index");
                }
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("Error al modificar a la persona externa", ex);
                return View();
            }
        }

        public ActionResult Detalles(int id)
        {
            try
            {
                using (GISDESEntity db = new GISDESEntity())
                {
                    PersonaExterna personaExterna = db.PersonaExterna.Find(id);
                    return View(personaExterna);

                }
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("Error al modificar el evento", ex);
                return View();
            }
        }

        public ActionResult Eliminar(int id)
        {
            using (GISDESEntity db = new GISDESEntity())
            {
                PersonaExterna personaExterna = db.PersonaExterna.Find(id);
                db.PersonaExterna.Remove(personaExterna);
                db.SaveChanges();
                return RedirectToAction("Index");

            }

        }
    }
}
