/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package socketsServidor;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.LinkedList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author santiguzman
 */
public class SocketListener {

    private int thePort = 0;
    public static final List<SocketController> clients = new LinkedList<>();

    public SocketListener(int newPort) {
        thePort = newPort;
    }

    public static void publicarUsuarios(String usuario, int operacion) {
        if (operacion == 0) {
            for (SocketController client : clients) {
                client.writeText("ADDUSER " + usuario);
            }
        } else {
            for (SocketController client : clients) {
                client.writeText("RMVUSER " + usuario);
            }
        }

    }

    public void run() {
        ServerSocket serverSocket = null;
        Socket socket = null;
        boolean quit = false;
        SocketController socketController = null;
        try {
            serverSocket = new ServerSocket(thePort);
        } catch (IOException ex) {
            Logger.getLogger(SocketListener.class.getName()).log(Level.SEVERE, null, ex);
        }

        if (serverSocket != null) {
            while (!quit) {
                try {
                    socket = serverSocket.accept();
                    socketController = new SocketController(socket);
                } catch (IOException ex) {
                    Logger.getLogger(SocketListener.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
        }
    }

}
