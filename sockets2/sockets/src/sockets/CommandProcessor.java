/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sockets;

import java.text.SimpleDateFormat;
import java.util.Date;

/**
 *
 * @author Danii
 */
public class CommandProcessor {

    public String responseCommand(String command) {
        command = command.trim().toUpperCase();
        String response = "";
        SimpleDateFormat sdf = null;

        switch (command) {
            case "TIME":
                sdf = new SimpleDateFormat("hh:mm:ss");
                response = "100 " + sdf.format(new Date());
                break;
            case "DATE":
                sdf = new SimpleDateFormat("YYYY/MM/DD");
                response = "100 " + sdf.format(new Date());
                break;
            case "DATETIME":
                sdf = new SimpleDateFormat("YYYY/MM/DD hh:mm:ss");
                response = "100 " + sdf.format(new Date());
                break;
            default:
                response = "200";
        }

        return response;
    }

  
}
