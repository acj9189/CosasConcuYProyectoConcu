/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Controlador;

import Modelo.Pez;
import Vista.VistaCliente;
import java.util.LinkedList;

/**
 *
 * @author Danii
 */
public class GestorCliente implements Runnable {

    public static ConexionServidor cnx;
    public static boolean controlHilo;
    public static LinkedList<Pez> listaPeces;
    private Thread hilo;
    private VistaCliente vista;

    public GestorCliente(ConexionServidor cnxn) {
        cnx = cnxn;
        listaPeces = new LinkedList<>();
        iniciarHilo();
    }

    private void iniciarHilo() {
        this.hilo = new Thread(this);
        hilo.start();
    }

    @Override
    public void run() {
        String read;
        this.vista = new VistaCliente();
        this.vista.setVisible(true);
        int ancho = (this.vista.getWidth()== 1366)?1366:1920;
        int alto = (this.vista.getHeight()== 768)?768:1080;
        this.vista.getPanelCliente1().alto = alto;
        this.vista.getPanelCliente1().ancho = ancho;
        this.cnx.Write("<Register>1234&"+ancho+"&"+alto);
        while (!controlHilo) {
            if ((read = this.cnx.Read()) != null) {
                if (read.startsWith("<Background>")) {
                    int sentido = 0;
                    if (read.equalsIgnoreCase("<Background>1")) {
                        sentido = 1;
                    }
                    this.vista.definirFondo(sentido);
                } else if (read.startsWith("<RemoveAllFishes>")) {
                    this.vista.repintar(false);
                    listaPeces.clear();
                    this.vista.repintar(true);
                } else if (read.startsWith("<Repaint>")) {
                    this.vista.repintar(true);
                } else if (read.startsWith("<Add Fish>")) {
                    String pez = read.replace("<Add Fish>", "");
                    //<Add Fish>0&374&128&0
                    listaPeces.add(new Pez(Integer.parseInt(pez.split("&")[1]),
                            Integer.parseInt(pez.split("&")[2]),
                            Integer.parseInt(pez.split("&")[0]),
                            Integer.parseInt(pez.split("&")[3])));
                }

            }

        }
    }

}
