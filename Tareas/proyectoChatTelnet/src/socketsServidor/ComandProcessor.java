/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package socketsServidor;

import static socketsServidor.SocketListener.clients;

/**
 *
 * @author santiguzman
 */
public class ComandProcessor {

    private SocketController socket;

    public ComandProcessor() {
    }

    public ComandProcessor(SocketController socket) {
        this.socket = socket;
    }

    public boolean writeText(String name, String text) {
        for (SocketController client : clients) {
            if (client.getName().equalsIgnoreCase(name)) {
                client.getListMsg().put(getSocket().getIdMessage(), text);
                client.writeText(text);
                return true;
            }
        }
        return false;
    }

    public void removeMessage(String idMessage) {
        for (SocketController client : clients) {
            if (client.getListMsg().containsKey(idMessage)) {
                client.getListMsg().remove(idMessage);
            }
        }
    }

    public boolean checkName(String name) {
        try {
            for (SocketController socket : clients) {
                if (socket.getName().equalsIgnoreCase(name)) {
                    return false;
                }
            }
        } catch (Exception e) {
            System.err.println("Error " + e);
        }
        return true;
    }

    public boolean writeTextAll(SocketController sender, String text) {
        if (clients.size() > 1) {
            for (SocketController client : clients) {
                if (sender != client) {
                    client.writeText(getSocket().getName() + "-> " + text);
                }
            }
            return true;
        }
        return false;
    }

    public int getNumofUsers() {
        return clients.size();
    }

    public boolean remove(SocketController remove) {
        return clients.remove(remove);
    }

    public String responseCommand(SocketController sender, String aCommand) {
        aCommand = aCommand.trim().toUpperCase();
        String response = "200 CODIGO INVALIDO";

        if (aCommand.startsWith("SENDALL ")) {
            if (writeTextAll(sender, aCommand.substring(8))) {
                response = "100 MENSAJE ENVIADO CON EXITO";
            } else {
                response = "200 MENSAJE SIN ENVIAR";
            }
        } else if (aCommand.equals("NUMOFUSERS")) {
            response = "100 NUMERO DE USUARIOS:" + this.getNumofUsers();
        } else if (aCommand.equals("GETUSERS")) {
            response = "100 LISTA DE USUARIOS:";
            for (SocketController socket : clients) {
                response += socket.getId() + " " + socket.getName() + ";";
            }
            response = response.substring(0, response.length() - 1);
        } else if (aCommand.startsWith("SEND ")) {
            String userName = aCommand.substring(5).substring(0, aCommand.substring(5).indexOf(" "));
            String msg = aCommand.substring(5 + userName.length());
            if (writeText(userName, getSocket().getName() + "->" + msg)) {
                response = "100 MENSAJE ENVIADO CON EXITO";
            } else {
                response = "200 MENSAJE SIN ENVIAR";
            }
        } else if (aCommand.startsWith("REMOVEMSG ")) {
            String idMessage = aCommand.substring(10);
            removeMessage(idMessage);
            response = "100 MENSAJE BORRADO CON EXITO";
        }

        return response;
    }

    /**
     * @return the socket
     */
    public SocketController getSocket() {
        return socket;
    }

    /**
     * @param socket the socket to set
     */
    public void setSocket(SocketController socket) {
        this.socket = socket;
    }

}
