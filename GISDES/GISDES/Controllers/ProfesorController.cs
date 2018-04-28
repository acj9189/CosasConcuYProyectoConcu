using GisDes.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace GisDes.Controllers
{
    public class ProfesorController : Controller
    {
        // GET: Profesor
        public ActionResult Index()
        {
            using (GISDESEntity bd = new GISDESEntity())
            {
                List<Profesor> listaProfesores = bd.Profesor.ToList();
                return View(listaProfesores);
            }

        }

        public ActionResult Agregar(Profesor profesor)
        {
            if (!ModelState.IsValid)
                return View();
            try
            {
                using (GISDESEntity bd = new GISDESEntity())
                {
                    bd.Profesor.Add(profesor);
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

        public ActionResult Actualizar(int id)
        {
            try
            {
                using (GISDESEntity bd = new GISDESEntity())
                {
                    Profesor profe = bd.Profesor.Find(id);
                    return View(profe);
                }
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("Error al agregar el evento", ex);
                return View();
            }
        }


        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Actualizar(Profesor profesor)
        {
            try
            {
                using (GISDESEntity bd = new GISDESEntity())
                {
                    Profesor profeNuevo = bd.Profesor.Find(profesor.Id);
                    profeNuevo.Nombre = profesor.Nombre;
                    profeNuevo.Apellidos = profesor.Apellidos;
                    profeNuevo.Cvlac = profesor.Cvlac;
                    profeNuevo.Intereses = profesor.Intereses;
                    profeNuevo.Departamento = profesor.Departamento;

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

        public ActionResult Eliminar(int id)
        {
            try
            {
                using (GISDESEntity bd = new GISDESEntity())
                {
                    Profesor profesor = bd.Profesor.Find(id);
                    profesor.Estado = false;
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

    }
}