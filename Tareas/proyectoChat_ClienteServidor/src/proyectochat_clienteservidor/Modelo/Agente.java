/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyectochat_clienteservidor.Modelo;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import proyectochat_clienteservidor.Controlador.SocketController;


public class Agente implements Runnable{

    private int thePort = 0;
    private Thread hilo;
    public static String name;
    public static final LinkedList<SocketController> clients = new LinkedList<>();

    public Agente(int newPort, String name) {
        this.thePort = newPort;
        this.name = name;
        this.hilo = new Thread(this);
        this.hilo.start();
    }

    public void run() {
        ServerSocket serverSocket = null;
        Socket socket = null;
        boolean quit = false;
        try {
            serverSocket = new ServerSocket(thePort);
            System.out.println("Servidor iniciado");
        } catch (IOException ex) {
            Logger.getLogger(Agente.class.getName()).log(Level.SEVERE, null, ex);
        }

        if (serverSocket != null) {
            System.out.println("Iniciando modo listener del servidor por el puerto:"+thePort);
            while (!quit) {
                try {
                    socket = serverSocket.accept();
                    clients.add(new SocketController(socket));
                    System.out.println("Cliente conectado");
                    
                } catch (IOException ex) {
                    Logger.getLogger(Agente.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
        }
    }

}
