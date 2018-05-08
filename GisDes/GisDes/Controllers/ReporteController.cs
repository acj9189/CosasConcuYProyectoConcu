using GisDes.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace GisDes.Controllers
{
    public class ReporteController : Controller
    {
        // GET: Reporte
        public ActionResult Index()
        {
            return View();
        }

        /// <summary>
        /// Reporte de semilleros por numero de estudiantes en rango de fecha a partir de los datos capturados desde la vista
        /// Caso de uso: CD-01
        /// Fecha: 06/05/2018
        /// </summary>
        /// <returns></returns>
        // GET: Reporte
        public ActionResult ReporteSemillerosNumeroEstudianteRangoFecha()
        {
            using(GisdesEntity bd = new GisdesEntity())
            {
                DateTime fechaInicial = new DateTime();
                DateTime fechaFinal = new DateTime();
                string parametroReporte = "año";

                List<IntegranteSemilleroInvestigacion> listaSemillerosIntegrantes = bd.IntegranteSemilleroInvestigacion.Where(
                                                       integrante => 
                                                       integrante.FechaIngreso >= fechaInicial 
                                                       && integrante.FechaIngreso < fechaFinal 
                                                       && integrante.Estado == 1).ToList();

                switch (parametroReporte.ToLower())
                {
                    case "año":
                        break;
                    case "mes":
                        break;
                    case "dia":
                        break;
                    case "DIA":
                        break;
                }
 

            }
            return View();
        }

    }
}