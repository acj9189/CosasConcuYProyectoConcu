/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package socketsServidor;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.SocketException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.logging.Level;
import java.util.logging.Logger;
import static socketsServidor.SocketListener.clients;
import static socketsServidor.SocketListener.publicarUsuarios;

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
    private boolean quit = false;
    public HashMap<String, String> listMsg = new HashMap<>();

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.setId((Integer) id);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getIdMessage() {
        SimpleDateFormat format = new SimpleDateFormat("YYYY-MM-dd hh:mm:ss");
        String time = format.format(new Date()).replace("-", "").replace(":", "").replace(" ", "");
        System.out.println(time);
        time = getId() + time;
        for (int i = time.length(); i < 17; i++) {
            time = "0" + time;
        }
        //System.err.println("idMessage->" + time + " generado por " + getName());
        System.err.println("Tamaño del mensaje " + time.length());
        return time;
    }

    public SocketController() {
    }

    public SocketController(Socket newSocket) {
        theSocket = newSocket;
        theCommandProcessor = new ComandProcessor(this);
        register = false;
        try {
            theOut = new PrintWriter(getTheSocket().getOutputStream(), true);
            theIn = new BufferedReader(new InputStreamReader(getTheSocket().getInputStream(), "UTF-8"));
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
        getTheOut().println(text);
    }

    public String readText() throws IOException {
        String text = "";
        try {
            text = getTheIn().readLine();
        } catch (SocketException ex) {
            System.out.println("Error readText() socketController "+ex);
            clients.remove(this);
            quit = true;
        }
        return text;
    }

    @Override
    public void run() {
        int timeout = 3;
        String command = null;
        
        writeText("W/Server");
        while (!quit) {
            try {
                command = readText();
            } catch (IOException ex) {
                Logger.getLogger(SocketController.class.getName()).log(Level.SEVERE, null, ex);
            }
            if (command != null) {
                if (command.trim().toUpperCase().equals("QUIT")) {
                    quit = true;
                    publicarUsuarios(this.name, 1);
                    getTheCommandProcessor().remove(this);
                    close();
                } else if (!isRegister()) {
                    timeout--;
                    if (command.toUpperCase().startsWith("REGISTER ")) {
                        setName(command.substring(9).toUpperCase());

                        if (getTheCommandProcessor().checkName(getName())) {
                            writeText("100 USUARIO REGISTRADO CON EXITO A: " + getName());
                            //System.out.println(getName());
                            timeout++;
                            clients.add(this);
                            this.setId((Integer) clients.size());
                            publicarUsuarios(this.name, 0);
                            setRegister(true);
                        } else {
                            writeText("200 USUARIO NO SE PUDO REGISTRAR NICKNAME YA EN USO");
                        }
                    } else {
                        writeText("200 USUARIO SIN REGISTRAR");
                    }
                    if (timeout < 1) {
                        writeText("200 NUMERO DE INTENTOS SUPERADOS");
                        quit = true;
                        getTheCommandProcessor().remove(this);
                        close();
                    }
                } else {
                    writeText(getTheCommandProcessor().responseCommand(this, command));
                }
            } else {
                publicarUsuarios(this.name, 1);
                getTheCommandProcessor().remove(this);
                quit = true;
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

    /**
     * @return the theCommandProcessor
     */
    public ComandProcessor getTheCommandProcessor() {
        return theCommandProcessor;
    }

    /**
     * @param theCommandProcessor the theCommandProcessor to set
     */
    public void setTheCommandProcessor(ComandProcessor theCommandProcessor) {
        this.theCommandProcessor = theCommandProcessor;
    }

    /**
     * @return the register
     */
    public boolean isRegister() {
        return register;
    }

    /**
     * @param register the register to set
     */
    public void setRegister(boolean register) {
        this.register = register;
    }

    /**
     * @return the listMsg
     */
    public HashMap<String, String> getListMsg() {
        return listMsg;
    }

    /**
     * @param listMsg the listMsg to set
     */
    public void setListMsg(HashMap<String, String> listMsg) {
        this.listMsg = listMsg;
    }

}
