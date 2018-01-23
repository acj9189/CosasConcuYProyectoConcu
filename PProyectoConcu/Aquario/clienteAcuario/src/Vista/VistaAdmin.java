/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Vista;

import Controlador.ConexionServidor;

/**
 *
 * @author Danii
 */
public class VistaAdmin extends javax.swing.JFrame {

    /**
     * Creates new form VistaAdmin
     */
    static ConexionServidor cnx;
    int TipoFish = 0;
    int Direccon = 0;
    public VistaAdmin(ConexionServidor cnx) {
        initComponents();
        this.cnx = cnx;
        
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jCboxTipoFish = new javax.swing.JComboBox<>();
        jBtnCrearFish = new javax.swing.JToggleButton();
        jLabel1 = new javax.swing.JLabel();
        jBtnPermiterCreacion = new javax.swing.JToggleButton();
        jCboxDireccion = new javax.swing.JComboBox<>();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowActivated(java.awt.event.WindowEvent evt) {
                formWindowActivated(evt);
            }
        });

        jCboxTipoFish.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Fish 1", "Fish 2", "Fish 3", "Fish 4", "Fish 5", "Fish 6" }));
        jCboxTipoFish.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                jCboxTipoFishItemStateChanged(evt);
            }
        });

        jBtnCrearFish.setText("Crear Fish");
        jBtnCrearFish.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jBtnCrearFishMouseClicked(evt);
            }
        });

        jLabel1.setText("Interface Admin");

        jBtnPermiterCreacion.setText("Nuevo Fish");
        jBtnPermiterCreacion.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jBtnPermiterCreacionMouseClicked(evt);
            }
        });

        jCboxDireccion.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Todo Izquierda", "Todo Derecha" }));
        jCboxDireccion.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                jCboxDireccionItemStateChanged(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(49, 49, 49)
                        .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 131, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(23, 23, 23)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(jCboxDireccion, 0, 175, Short.MAX_VALUE)
                            .addComponent(jCboxTipoFish, 0, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jBtnCrearFish, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jBtnPermiterCreacion, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))))
                .addContainerGap(83, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(29, 29, 29)
                .addComponent(jLabel1)
                .addGap(33, 33, 33)
                .addComponent(jBtnPermiterCreacion)
                .addGap(56, 56, 56)
                .addComponent(jCboxTipoFish, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(29, 29, 29)
                .addComponent(jCboxDireccion, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(jBtnCrearFish)
                .addContainerGap(41, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void formWindowActivated(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_formWindowActivated
        
        jBtnCrearFish.setEnabled(false);
        jCboxTipoFish.setEnabled(false);
        jCboxDireccion.setEnabled(false);
        
    }//GEN-LAST:event_formWindowActivated

    private void jBtnPermiterCreacionMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_jBtnPermiterCreacionMouseClicked
        
        jBtnCrearFish.setEnabled(true);
        jCboxTipoFish.setEnabled(true);
        jCboxDireccion.setEnabled(true);
        
    }//GEN-LAST:event_jBtnPermiterCreacionMouseClicked

    private void jBtnCrearFishMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_jBtnCrearFishMouseClicked
        
        String Commando = "<Add Fish>" + this.TipoFish + "&100&" + this.Direccon;
        cnx.Write(Commando);
        
        this.TipoFish = 0;
        this.Direccon = 0;
        
        jBtnCrearFish.setEnabled(false);
        jCboxTipoFish.setEnabled(false);
        jCboxDireccion.setEnabled(false);
        
    }//GEN-LAST:event_jBtnCrearFishMouseClicked

    private void jCboxTipoFishItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_jCboxTipoFishItemStateChanged
        int seleccion = (jCboxTipoFish.getSelectedIndex());
        
        switch (seleccion){
            case 0:
                this.TipoFish = 0;
                break;
                
             case 1:
                this.TipoFish = 1;
                break;
                
             case 2:
                this.TipoFish = 2;
                break;
                
             case 3:
                this.TipoFish = 3;
                break;
                
             case 4:
                this.TipoFish = 4;
                break;
                
              case 5:
                this.TipoFish = 5;
                break;
            
        
        }
        
    }//GEN-LAST:event_jCboxTipoFishItemStateChanged

    private void jCboxDireccionItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_jCboxDireccionItemStateChanged

         int seleccion = (jCboxDireccion.getSelectedIndex());
        
        switch (seleccion){
            case 0:
                this.Direccon = 0;
                break;
                
             case 1:
                this.Direccon = 1;
                break;
                
        }
        
        
    }//GEN-LAST:event_jCboxDireccionItemStateChanged

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(VistaAdmin.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(VistaAdmin.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(VistaAdmin.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(VistaAdmin.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new VistaAdmin(cnx).setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JToggleButton jBtnCrearFish;
    private javax.swing.JToggleButton jBtnPermiterCreacion;
    private javax.swing.JComboBox<String> jCboxDireccion;
    private javax.swing.JComboBox<String> jCboxTipoFish;
    private javax.swing.JLabel jLabel1;
    // End of variables declaration//GEN-END:variables
}
