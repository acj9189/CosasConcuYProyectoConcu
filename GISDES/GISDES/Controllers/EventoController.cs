using GISDES.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace GISDES.Controllers
{
    public class EventoController : Controller
    {
        // GET: Evento
        public ActionResult Index()
        {
            using (GISDESEntity bd = new GISDESEntity())
            {
                List<Evento> lista = bd.Evento.Where(ev => ev.Estado == true).ToList();
                return View(lista);
            }
        }

        public ActionResult Crear(Evento e)
        {
            if (!ModelState.IsValid)
                return View();
            try
            {
                using (GISDESEntity bd = new GISDESEntity())
                {
                    e.Estado = true;
                    bd.Evento.Add(e);
                    bd.SaveChanges();
                    return RedirectToAction("Index");
                }
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("Error al agregar el evento", ex);
                return View();
            }

        }

        public ActionResult Modificar(int id)
        {
            try
            {
                using (GISDESEntity bd = new GISDESEntity())
                {
                    Evento evento = bd.Evento.Find(id);
                    return View(evento);
                }

            }
            catch (Exception ex)
            {
                ModelState.AddModelError("Error al modificar el evento", ex);
                return View();
            }
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Modificar(Evento evento)
        {
            try
            {
                using (GISDESEntity bd = new GISDESEntity())
                {
                    Evento eventoNuevo = bd.Evento.Find(evento.Id);
                    eventoNuevo.Nombre = evento.Nombre;
                    eventoNuevo.Tipo = evento.Tipo;
                    eventoNuevo.Fecha = evento.Fecha;
                    bd.SaveChanges();

                    return RedirectToAction("Index");
                }
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("Error al almacenar el evento modificado", ex);
                return View();
            }
            return View();
        }

        public ActionResult Eliminar(int id)
        {
            try
            {
                using (GISDESEntity bd = new GISDESEntity())
                {
                    Evento e = bd.Evento.Find(id);
                    e.Estado = false;
                    bd.SaveChanges();

                    return RedirectToAction("Index");
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