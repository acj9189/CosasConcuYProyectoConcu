/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Controladores;
import Vistas.JFCliente;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import sockets.*;
import java.net.Socket;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JList;

/**
 *
 * @author Andrés
 */
public class hiloEscucharClientes implements Runnable{

    
    
   private Socket SoketAnalisis;
   private JList<String> ListaMostrar;
   
   private PrintWriter theOut;
   private BufferedReader theIn;
   private JFCliente cliente;

    public hiloEscucharClientes(Socket SoketAnalisis, JList ListaMostrar , JFCliente cliente){
        
        try {
            this.SoketAnalisis = SoketAnalisis;
            this.ListaMostrar = ListaMostrar;
            this.theOut = new PrintWriter(this.getSoketAnalisis().getOutputStream(),true);
            this.theIn = new BufferedReader(new InputStreamReader(this.getSoketAnalisis().getInputStream(), "UTF-8"));
            this.cliente = cliente;
       } catch (IOException ex) {
           Logger.getLogger(hiloEscucharClientes.class.getName()).log(Level.SEVERE, null, ex);
       }   
    }

    public JList getListaMostrar() {
        return ListaMostrar;
    }

    public void setListaMostrar(JList ListaMostrar) {
        this.ListaMostrar = ListaMostrar;
    }


    public Socket getSoketAnalisis() {
        return SoketAnalisis;
    }

    public void setSoketAnalisis(Socket SoketAnalisis) {
        this.SoketAnalisis = SoketAnalisis;
    }
   
   
 
    @Override
    public void run() {
        String Datos="";
        this.getTheOut().println("GETUSERS");
           
       try {
           Datos =  this.getTheIn().readLine();
          // " id:nombre ; id nombre"
          String [] a = Datos.split(";");
          
           for (int i = 0; i < a.length; i++) {
               String[]  b = a[i].split(" ");
               this.getListaMostrar().add(b[1], this.getCliente());
           }  
       } catch (IOException ex) {
           Logger.getLogger(hiloEscucharClientes.class.getName()).log(Level.SEVERE, null, ex);
       }
           
           
           
     
       
        
        
                
        
    }

    /**
     * @return the theOut
     */
    public PrintWriter getTheOut() {
        return theOut;
    }

    /**
     * @param theOut the theOut to set
     */
    public void setTheOut(PrintWriter theOut) {
        this.theOut = theOut;
    }

    /**
     * @return the theIn
     */
    public BufferedReader getTheIn() {
        return theIn;
    }

    /**
     * @param theIn the theIn to set
     */
    public void setTheIn(BufferedReader theIn) {
        this.theIn = theIn;
    }

    /**
     * @return the cliente
     */
    public JFCliente getCliente() {
        return cliente;
    }

    /**
     * @param cliente the cliente to set
     */
    public void setCliente(JFCliente cliente) {
        this.cliente = cliente;
    }
    
}
