/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sockets;

/**
 *
 * @author Danii
 */
public class Sockets {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        SocketListener socketListener = new SocketListener(1107);
        socketListener.run();

        

    }

}
