using GISDES.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace GISDES.Controllers
{
    public class PersonaExternaController : Controller
    {
        // GET: PersonaExterna
        public ActionResult Index()
        {
            using (GISDESEntities bd = new Models.GISDESEntities())
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
                using (GISDESEntities bd = new GISDESEntities())
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
                using (GISDESEntities db = new GISDESEntities())
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
                using (GISDESEntities db = new GISDESEntities())
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
                using (GISDESEntities db = new GISDESEntities())
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
            using (GISDESEntities db = new GISDESEntities())
            {
                PersonaExterna personaExterna = db.PersonaExterna.Find(id);
                db.PersonaExterna.Remove(personaExterna);
                db.SaveChanges();
                return RedirectToAction("Index");

            }
          
        }
    }
}
