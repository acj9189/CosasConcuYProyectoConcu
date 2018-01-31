/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Modelo;

import java.awt.Dimension;
import java.awt.Graphics;
import javax.swing.ImageIcon;


/**
 *
 * @author Andrés
 */
public class Imagen extends javax.swing.JPanel {

String Ruta;

    public void setRuta(String Ruta) {
        this.Ruta = Ruta;
    }

    public String getRuta() {
        return Ruta;
    }
    
    
public Imagen() {
this.setSize(1000, 1000); //se selecciona el tamaño del panel
}

//Se crea un método cuyo parámetro debe ser un objeto Graphics

public void paint(Graphics grafico) {
Dimension height = getSize();

//Se selecciona la imagen que tenemos en el paquete de la //ruta del programa

//ImageIcon Img = new ImageIcon(getClass().getResource("/Images/Diagrama.png")); 
ImageIcon Img = new ImageIcon(getClass().getResource(this.Ruta));

//se dibuja la imagen que tenemos en el paquete Images //dentro de un panel

grafico.drawImage(Img.getImage(), 0, 0, 100, 50, null);

setOpaque(false);
super.paintComponent(grafico);
}
}