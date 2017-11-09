/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Controladores;

import VistasCliente.JFCliente;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.DefaultListModel;
import javax.swing.JList;
import static VistasCliente.JFCliente.escribirsocket;
import static VistasCliente.JFCliente.leersocket;
import static VistasCliente.JFCliente.getSemaforoLectura;
/**
 *
 * @author Andres
 */
public class hiloEscucharYEnviarMensajes implements Runnable{
    
   private Socket SoketAnalisis;
   private JList<String> ListaMostrar;
   
   private PrintWriter theOut;
   private BufferedReader theIn;
   private JFCliente cliente;
   
   DefaultListModel modelo = new DefaultListModel();
   
   public hiloEscucharYEnviarMensajes(PrintWriter out, BufferedReader in,  JList ListaMostrar){
       
       // this.SoketAnalisis = SoketAnalisis;
       this.ListaMostrar = ListaMostrar;
       this.theOut = out;
       this.theIn = in;
      // this.cliente = cliente;  
   
   }
   
   public hiloEscucharYEnviarMensajes(JList ListaMostrar){
       
       // this.SoketAnalisis = SoketAnalisis;
       this.ListaMostrar = ListaMostrar;
      // this.cliente = cliente;  
   
   }


    public JFCliente getCliente() {
        return cliente;
    }

    public JList<String> getListaMostrar() {
        return ListaMostrar;
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
     * @param ListaMostrar the ListaMostrar to set
     */
    public void setListaMostrar(JList<String> ListaMostrar) {
        this.ListaMostrar = ListaMostrar;
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
        
        while(true){
            try {
                agregarListaEntradaSalida();
                Thread.sleep(100);
            } catch (InterruptedException ex) {
                Logger.getLogger(hiloEscucharYEnviarMensajes.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        
    }
    
    
    
     private void agregarListaEntradaSalida() throws InterruptedException {
          
         //               String Datos = this.getTheIn().readLine();
//         getSemaforoLectura().acquire();
//         System.out.println("Bloqueo lectura ES");
//         System.out.println("Desbloqueo lectura ES");
//         getSemaforoLectura().release();
         String Datos = leersocket();
         // System.err.println("Observacion de errores "+ Datos);
         if(Datos.startsWith("MSG")){
             //String Datos2 = this.getTheIn().readLine();
             if(!modelo.contains(Datos)){
                 this.modelo.addElement(Datos);
                 this.ListaMostrar.setModel(this.modelo);
             }
         }
//               else{if(Datos.startsWith("102")){
//                    String Datos2 = this.getTheIn().readLine();
//                    if(!modelo.contains(Datos)){
//                        this.modelo.addElement(Datos);
//                        this.ListaMostrar.setModel(this.modelo);
//                    }
//                   }
//               }

       
    }
    
    
}
