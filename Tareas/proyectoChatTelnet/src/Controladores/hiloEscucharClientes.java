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
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.DefaultListModel;
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
   
   
   private int numeroConectadosActual = 0;
   
   private boolean esperaBolean = true;
   
   
   
    public hiloEscucharClientes(PrintWriter out, BufferedReader in,  JList<String> ListaMostrar, JFCliente cliente){
        
        //this.SoketAnalisis = SoketAnalisis;
        this.ListaMostrar = ListaMostrar;
        this.theOut = out;
        this.theIn = in;
        this.cliente = cliente;
    }
    
     public hiloEscucharClientes(PrintWriter out, BufferedReader in,  JList<String> ListaMostrar){
        
        //this.SoketAnalisis = SoketAnalisis;
        this.ListaMostrar = ListaMostrar;
        this.theOut = out;
        this.theIn = in;
      //  this.cliente = cliente;
    }

    public JList getListaMostrar() {
        return ListaMostrar;
    }

    public void setListaMostrar(JList ListaMostrar) {
        this.ListaMostrar = ListaMostrar;
    }

    public void setEsperaBolean(boolean esperaBolean) {
        this.esperaBolean = esperaBolean;
    }

    public boolean isEsperaBolean() {
        return esperaBolean;
    }

    

    public Socket getSoketAnalisis() {
        return SoketAnalisis;
    }

    public void setSoketAnalisis(Socket SoketAnalisis) {
        this.SoketAnalisis = SoketAnalisis;
    }
 
    @Override
    public void run() {
        
        while(this.esperaBolean){
          //  System.out.println("qqqq");
           agregarLista();
        }
        
        
    }
    
    private synchronized void agregarLista(){
       try { 
          this.theOut.println("NUMOFUSERS");
          String Res = this.theIn.readLine();
          if(Res.startsWith("105")){
              Res = Res.substring(23);
              System.out.println(Res);
    //          String[] c = Res.split(":");
    //          int temp2 = (Integer.valueOf(c[0]));
              int temp = Integer.valueOf(Res);
              if(this.numeroConectadosActual != temp){
                    this.getTheOut().println("GETUSERS");  
                    String Datos = this.getTheIn().readLine();
                    // " id:nombre ; id nombre"
    //                System.out.println(Datos);
                    Datos = Datos.substring(22);
    //                System.out.println(Datos);
                    String [] a = Datos.split(";");
                    DefaultListModel modelo = new DefaultListModel();
                    String noRepetidos = "";
                     for (int i = 0; i < a.length; i++) {
                         String[]  b = a[i].split(" ");
    //                     if(!noRepetidos.contains(b[1])){
                           if(!modelo.contains(b[1])){
                             modelo.addElement(b[1]);
                             noRepetidos = noRepetidos + b[1];    
                         } 
                     }
                     this.numeroConectadosActual = a.length;
                     this.ListaMostrar.setModel(modelo);
              }
          
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
