/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sockets;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.logging.Level;
import java.util.logging.Logger;
import static sockets.SocketListener.clients;

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
    private ComandProcessor theCommandProcessor;
    private String name;
    private boolean register;
    public final HashMap<String,String> listMsg = new HashMap<>();

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    
    public String getIdMessage(){
        SimpleDateFormat format = new SimpleDateFormat("YYYY-MM-dd hh:mm:ss");
        String time = format.format(new Date()).replace("-", "").replace(":", "").replace(" ", "");
        System.out.println(time);
        time = id+time;
        for (int i = time.length(); i < 17; i++) {
            time = "0"+time;
        }
        System.err.println("idMessage->"+time+" generado por "+name);
        return time;
    }
    

    public SocketController(Socket newSocket) {
        theSocket = newSocket;
        theCommandProcessor = new ComandProcessor(this);
        register = false;
        try {
            theOut = new PrintWriter(theSocket.getOutputStream(), true);
            theIn = new BufferedReader(new InputStreamReader(theSocket.getInputStream(), "UTF-8"));
        } catch (IOException ex) {
            Logger.getLogger(SocketController.class.getName()).log(Level.SEVERE, null, ex);
        }
        theThread = new Thread(this);
        theThread.start();
    }

    public void close() {
        try {
            theOut.close();
            theIn.close();
            theSocket.close();
        } catch (Exception e) {
        }
    }

    public void writeText(String text) {
        theOut.println(text);
    }

    public String readText() {
        String text = null;
        try {
            text = theIn.readLine();
        } catch (IOException ex) {
            Logger.getLogger(SocketController.class.getName()).log(Level.SEVERE, null, ex);
        }
        return text;
    }

    @Override
    public void run() {
        int timeout = 3;
        String command = null;
        boolean quit = false;
        writeText("W/Server");
        while (!quit) {
            command = readText();
            if (command != null) {
                if (command.trim().toUpperCase().equals("QUIT")) {
                    quit = true;
                    theCommandProcessor.remove(this);
                    close();
                } else if (!register) {
                    timeout--;
                    if (command.toUpperCase().startsWith("REGISTER ")) {
                        name = command.substring(9).toUpperCase();
                        if (theCommandProcessor.checkName(name)) {
                            writeText("100 USUARIO REGISTRADO CON EXITO");
                            timeout++;
                            clients.add(this);
                            this.id = clients.size();
                            register = true;
                        } else {
                            writeText("200 USUARIO NO SE PUDO REGISTRAR NICKNAME YA EN USO");
                        }
                    } else {
                        writeText("200 USUARIO SIN REGISTRAR");
                    }
                    if (timeout < 1) {
                        writeText("200 NUMERO DE INTENTOS SUPERADOS");
                        quit = true;
                        theCommandProcessor.remove(this);
                        close();
                    }
                } else {
                    writeText(theCommandProcessor.responseCommand(this, command));
                }
            } else {
                theCommandProcessor.remove(this);
                quit = true;
            }
        }
    }

}
