/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Modelo;

import java.awt.Image;

/**
 *
 * @author Danii
 */
public class Pez {
    private int x;
    private int y;
    private Image imagen;

    public Pez() {
    }

    public Pez(int x, int y, Image imagen) {
        this.x = x;
        this.y = y;
        this.imagen = imagen;
    }

    public int getX() {
        return x;
    }

    public Image getImagen() {
        return imagen;
    }

    public int getY() {
        return y;
    }

    public void setImagen(Image imagen) {
        this.imagen = imagen;
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }
    
    

}
