/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Modelo;

import java.awt.Image;
import javax.swing.ImageIcon;

/**
 *
 * @author Danii
 */
public class Pez {

    private int x;
    private int y;
    private int tipo;
    private int sentido;
    private Image imagen;

    public Pez() {
    }

    public Pez(int x, int y, int tipo, int sentido) {
        this.x = x;
        this.y = y;
        this.tipo = tipo;
        this.sentido = sentido;
        String ruta = "../Vista/Images/"+tipo+"-"+sentido+".png";
        this.imagen = new ImageIcon(getClass().getResource(ruta)).getImage();
    }

    /**
     * @return the x
     */
    public int getX() {
        return x;
    }

    /**
     * @param x the x to set
     */
    public void setX(int x) {
        this.x = x;
    }

    /**
     * @return the y
     */
    public int getY() {
        return y;
    }

    /**
     * @param y the y to set
     */
    public void setY(int y) {
        this.y = y;
    }

    /**
     * @return the tipo
     */
    public int getTipo() {
        return tipo;
    }

    /**
     * @param tipo the tipo to set
     */
    public void setTipo(int tipo) {
        this.tipo = tipo;
    }

    /**
     * @return the sentido
     */
    public int getSentido() {
        return sentido;
    }

    /**
     * @param sentido the sentido to set
     */
    public void setSentido(int sentido) {
        this.sentido = sentido;
    }

    /**
     * @return the imagen
     */
    public Image getImagen() {
        return imagen;
    }

    /**
     * @param imagen the imagen to set
     */
    public void setImagen(Image imagen) {
        this.imagen = imagen;
    }

}
