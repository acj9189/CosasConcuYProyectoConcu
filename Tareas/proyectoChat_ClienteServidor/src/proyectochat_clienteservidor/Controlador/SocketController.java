/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyectochat_clienteservidor.Controlador;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.SocketException;
import java.util.logging.Level;
import java.util.logging.Logger;
import static proyectochat_clienteservidor.Modelo.Agente.clients;
import static proyectochat_clienteservidor.Modelo.Agente.name;

/**
 *
 * @author danii
 */
public class SocketController implements Runnable {

    private Integer id;
    private Thread theThread = null;
    private Socket theSocket = null;
    private PrintWriter theOut = null;
    private BufferedReader theIn = null;
    private String nameClient;
    private boolean quit = false;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.setId((Integer) id);
    }

    public String getName() {
        return nameClient;
    }

    public void setName(String nameClient) {
        this.nameClient = nameClient;
    }

    public SocketController() {
    }

    public SocketController(Socket newSocket) {
        theSocket = newSocket;
        try {
            theOut = new PrintWriter(this.theSocket.getOutputStream(), true);
            theIn = new BufferedReader(new InputStreamReader(this.theSocket.getInputStream(), "UTF-8"));
        } catch (IOException ex) {
            Logger.getLogger(SocketController.class.getName()).log(Level.SEVERE, null, ex);
        }
        theThread = new Thread(this);
        theThread.start();
    }

    public void close() {
        try {
            getTheOut().close();
            getTheIn().close();
            getTheSocket().close();
        } catch (Exception e) {
        }
    }

    public void writeText(String text) {
        try {
            getTheOut().println(text);
        } catch (Exception ex) {
            System.out.println("Error readText() socketController " + ex);
            clients.remove(this);
            quit = true;
        }
    }

    public String readText() {
        String text = "";
        try {
            text = getTheIn().readLine();
        } catch (IOException ex) {
            System.out.println("Error readText() socketController " + ex);
            clients.remove(this);
            quit = true;
        }
        return text;
    }

    @Override
    public void run() {
        String command = null;
              
        while (!quit) {
            command = readText();
            if (command != null) {
                if (command.startsWith("Connect ")) {
                    this.nameClient = command.substring(command.indexOf(" "),command.indexOf("*"));
                    String data = command.substring(command.indexOf("*") + 1);
                    try {
                        Socket client = new Socket(data.split("-")[0], Integer.parseInt(data.split("-")[1]));
                        PrintWriter theOut = new PrintWriter(client.getOutputStream(), true);
                        theOut.println("Name:"+name);
                    } catch (Exception e) {
                    }
                } else{
                    System.err.println(command);
                }
            }
        }
    }

    /**
     * @param id the id to set
     */
    public void setId(Integer id) {
        this.id = id;
    }

    /**
     * @return the theThread
     */
    public Thread getTheThread() {
        return theThread;
    }

    /**
     * @param theThread the theThread to set
     */
    public void setTheThread(Thread theThread) {
        this.theThread = theThread;
    }

    /**
     * @return the theSocket
     */
    public Socket getTheSocket() {
        return theSocket;
    }

    /**
     * @param theSocket the theSocket to set
     */
    public void setTheSocket(Socket theSocket) {
        this.theSocket = theSocket;
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

}
