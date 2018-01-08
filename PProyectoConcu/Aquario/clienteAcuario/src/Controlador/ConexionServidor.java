/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Controlador;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Andres
 */
public class ConexionServidor {
    
    private Socket Socket;
    private int Port;
    private String Address;
    
    public PrintWriter theOut;
    public BufferedReader theIn;

    public ConexionServidor() {
    }

    public ConexionServidor(String Address ,int Port) {
        
        this.Port = Port;
        this.Address = Address;
        try {
            this.Socket = new Socket(this.Address, this.Port);
            this.theOut = new PrintWriter(this.Socket.getOutputStream(), true);
            this.theIn = new BufferedReader(new InputStreamReader(this.Socket.getInputStream(), "UTF-8"));
        } catch (IOException ex) {
            Logger.getLogger(ConexionServidor.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    public String Write(String Comando){
        String Retorno ="";
        try {
            this.theOut.println(Comando);
            Retorno = this.theIn.readLine();
        } catch (IOException ex) {
            Logger.getLogger(ConexionServidor.class.getName()).log(Level.SEVERE, null, ex);
        }
        return Retorno;
    }
    
    public String Read(){
        String Retorno ="";
        try {
            Retorno = this.theIn.readLine();
        } catch (IOException ex) {
            Logger.getLogger(ConexionServidor.class.getName()).log(Level.SEVERE, null, ex);
        }
        return Retorno;
    }
    
    
    
    
    
    
}
