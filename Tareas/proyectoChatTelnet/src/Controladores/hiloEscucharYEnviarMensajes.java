/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Controladores;

import VistasCliente.JFCliente;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.DefaultListModel;
import javax.swing.JList;
import static VistasCliente.JFCliente.leersocket;
import java.util.LinkedList;
import java.util.List;

/**
 *
 * @author Andres
 */
public class hiloEscucharYEnviarMensajes implements Runnable {

    private Socket SoketAnalisis;
    private JList<String> ListaMensaje;
    private JList<String> ListaClientes;
    
    private LinkedList<String> ListaIDMensaje;

    private final Thread hilo;

    private PrintWriter theOut;
    private BufferedReader theIn;
    private JFCliente cliente;

    DefaultListModel modeloMensajes;
    DefaultListModel modeloClientes = new DefaultListModel();

    public hiloEscucharYEnviarMensajes() {
        this.hilo = new Thread(this);
    }

    public hiloEscucharYEnviarMensajes(JList ListaMensaje, JList ListaClientes, DefaultListModel modelo, LinkedList IDMensaje) {
        this.hilo = new Thread(this);
        this.ListaMensaje = ListaMensaje;
        this.ListaClientes = ListaClientes;
        this.modeloMensajes = modelo;
        this.ListaIDMensaje = IDMensaje;
    }

    public void iniciar() {
        this.hilo.start();
    }

    public JFCliente getCliente() {
        return cliente;
    }

    public JList<String> getListaMostrar() {
        return ListaMensaje;
    }

    public Socket getSoketAnalisis() {
        return SoketAnalisis;
    }

    public BufferedReader getTheIn() {
        return theIn;
    }

    public PrintWriter getTheOut() {
        return theOut;
    }

    /**
     * @param SoketAnalisis the SoketAnalisis to set
     */
    public void setSoketAnalisis(Socket SoketAnalisis) {
        this.SoketAnalisis = SoketAnalisis;
    }

    /**
     * @param ListaMostrar the ListaMensaje to set
     */
    public void setListaMostrar(JList<String> ListaMostrar) {
        this.ListaMensaje = ListaMostrar;
    }

    /**
     * @param theOut the theOut to set
     */
    public void setTheOut(PrintWriter theOut) {
        this.theOut = theOut;
    }

    /**
     * @param theIn the theIn to set
     */
    public void setTheIn(BufferedReader theIn) {
        this.theIn = theIn;
    }

    /**
     * @param cliente the cliente to set
     */
    public void setCliente(JFCliente cliente) {
        this.cliente = cliente;
    }

    @Override
    public void run() {
        
        while (true) {
            String datos = leersocket();
            System.out.println(datos);
            if (!datos.equals("")) {
                if (datos.startsWith("MSG:")) {
                    String datos2 = datos.substring(4, 21);
                   //System.err.println(datos2 + "Tamaño");
                   datos = "MSG:" + datos.substring(22);
//                    if (!modeloMensajes.contains(datos)) {
                        this.modeloMensajes.addElement(datos);
                        this.ListaIDMensaje.add(datos2);
                        this.ListaMensaje.setModel(this.modeloMensajes);
//                    }
                } else if (datos.startsWith("106 ")) {
                    datos = datos.replace("106 LISTA DE USUARIOS:", "");
                    for (String user : datos.split(";")) {
                        if (!this.modeloClientes.contains(user.split(" ")[1].toUpperCase())) {
                            this.modeloClientes.addElement(user.split(" ")[1]);
                            this.ListaClientes.setModel(this.modeloClientes);
                        }
                    }
                } else if (datos.startsWith("ADDUSER ")) {
                    datos = datos.substring(8);
                    if (!this.modeloClientes.contains(datos.toUpperCase())) {
                        this.modeloClientes.addElement(datos.toUpperCase());
                        this.ListaClientes.setModel(this.modeloClientes);
                    }
                } else if (datos.startsWith("RMVUSER ")) {
                    datos = datos.substring(8);
                    if (this.modeloClientes.contains(datos.toUpperCase())) {
                        this.modeloClientes.removeElement(datos.toUpperCase());
                        this.ListaClientes.setModel(this.modeloClientes);
                    }
                } else if(datos.startsWith("104 ")){
                    datos = datos.substring(31);
                    if(this.ListaIDMensaje.contains(datos.toUpperCase())){
                        //int temp = this.modeloMensajes.indexOf(datos);
                        int temp = this.ListaIDMensaje.indexOf(datos);
                        this.ListaIDMensaje.remove(datos);
                       // this.modeloMensajes.remove(temp);
                        this.modeloMensajes.removeElementAt(temp);
                        this.ListaMensaje.setModel(this.modeloMensajes);
                    }
                  }
                }
            }
    }


}
