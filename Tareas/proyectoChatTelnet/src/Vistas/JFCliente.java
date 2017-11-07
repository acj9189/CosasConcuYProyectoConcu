/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Vistas;
import Controladores.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;

/**
 *
 * @author Andrés
 */
public class JFCliente extends javax.swing.JFrame {

    /**
     * Creates new form JFCliente
     */
    
    private hiloEscucharClientes HiLoClientes;
    private Socket socketConeccion;
    public JFCliente inCliente;
    private String nombreUsuario;
    
    private PrintWriter theOut;
    private BufferedReader theIn;
    public int cont = 0;
    
    private boolean seleUsuEnviar = false;
    private String usuAEnviar = "";
    
    
    public JFCliente() {
        initComponents();  
        this.inCliente = this;
        
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        txtName = new javax.swing.JTextField();
        label1 = new java.awt.Label();
        txtPort = new javax.swing.JTextField();
        label2 = new java.awt.Label();
        label3 = new java.awt.Label();
        label4 = new java.awt.Label();
        jScrollPane1 = new javax.swing.JScrollPane();
        jList1 = new javax.swing.JList<>();
        jScrollPane2 = new javax.swing.JScrollPane();
        jLstUsuariosConectados = new javax.swing.JList<>();
        jLabel1 = new javax.swing.JLabel();
        label5 = new java.awt.Label();
        txtHost = new javax.swing.JTextField();
        btnEnviarMensaje = new javax.swing.JButton();
        btnConectarce = new javax.swing.JButton();
        txtEnviarMensaje = new javax.swing.JTextField();
        label6 = new java.awt.Label();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        label1.setText("Cliente");

        txtPort.setName("txtPort"); // NOI18N

        label2.setText("Ingrese el Puerto");

        label3.setText("Ingrese el Host");

        label4.setText("Mensajes Recibidos");

        jScrollPane1.setViewportView(jList1);

        jLstUsuariosConectados.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyPressed(java.awt.event.KeyEvent evt) {
                jLstUsuariosConectadosKeyPressed(evt);
            }
        });
        jLstUsuariosConectados.addListSelectionListener(new javax.swing.event.ListSelectionListener() {
            public void valueChanged(javax.swing.event.ListSelectionEvent evt) {
                jLstUsuariosConectadosValueChanged(evt);
            }
        });
        jScrollPane2.setViewportView(jLstUsuariosConectados);

        jLabel1.setText("Lista de Conectados");

        label5.setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        label5.setText("Enviar");

        txtHost.setName("txtHost"); // NOI18N

        btnEnviarMensaje.setText("Enviar Mensaje");
        btnEnviarMensaje.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnEnviarMensajeMouseClicked(evt);
            }
        });

        btnConectarce.setText("Conectarce");
        btnConectarce.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnConectarceMouseClicked(evt);
            }
        });

        label6.setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        label6.setText("UserName");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(20, 20, 20)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(btnConectarce)
                            .addComponent(txtName, javax.swing.GroupLayout.PREFERRED_SIZE, 132, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(label1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(label3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(txtHost, javax.swing.GroupLayout.PREFERRED_SIZE, 132, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addGap(30, 30, 30)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(txtPort, javax.swing.GroupLayout.PREFERRED_SIZE, 138, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(label2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                            .addComponent(label5, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(btnEnviarMensaje))
                        .addContainerGap(402, Short.MAX_VALUE))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                            .addComponent(txtEnviarMensaje, javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel1, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.PREFERRED_SIZE, 258, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(label4, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jScrollPane1, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 681, Short.MAX_VALUE)
                            .addComponent(jScrollPane2, javax.swing.GroupLayout.Alignment.LEADING))
                        .addGap(0, 0, Short.MAX_VALUE))))
            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(layout.createSequentialGroup()
                    .addGap(30, 30, 30)
                    .addComponent(label6, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addContainerGap(627, Short.MAX_VALUE)))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(label1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(label3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtPort, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(txtHost, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addComponent(label2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(40, 40, 40)
                .addComponent(txtName, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(btnConectarce)
                .addGap(18, 18, 18)
                .addComponent(label4, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 195, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(20, 20, 20)
                .addComponent(jLabel1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 119, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 30, Short.MAX_VALUE)
                .addComponent(label5, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(txtEnviarMensaje, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(btnEnviarMensaje)
                .addGap(28, 28, 28))
            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(layout.createSequentialGroup()
                    .addGap(110, 110, 110)
                    .addComponent(label6, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addContainerGap(588, Short.MAX_VALUE)))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnConectarceMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_btnConectarceMouseClicked
      
        try {
            
            String ip = this.txtHost.getText();
            int puerto = Integer.valueOf(this.txtPort.getText());
            this.nombreUsuario = this.txtName.getText();
            
            if(this.cont == 0){
                this.socketConeccion = new Socket(ip, puerto);
                this.theOut = new PrintWriter(this.socketConeccion.getOutputStream(),true);
                this.theIn = new BufferedReader(new InputStreamReader(this.socketConeccion.getInputStream(), "UTF-8"));
            }
            if(this.cont < 3){
                this.theOut.print("REGISTER " + this.nombreUsuario );
                this.cont++;
                String Res = this.theIn.readLine();
                if(Res.startsWith("100")){
                    JOptionPane.showInputDialog(this, "Usted se ha conectado con exito al servidor");
                    this.HiLoClientes = new hiloEscucharClientes(this.socketConeccion, this.jLstUsuariosConectados, this);
                    Thread Hilo = new Thread(this.HiLoClientes);
                    Hilo.start();  
                    this.txtName.setEditable(false);
                    this.btnConectarce.setEnabled(false);
                }
                else{
                    if(this.cont == 3){
                        JOptionPane.showInputDialog(this, "El numero maximo de intentos para el nombre de usuario es 3");
                        this.txtName.setText("");
                        this.socketConeccion = null; 
                        this.cont = 0;
                        this.nombreUsuario = "";
                        this.theIn = null;
                        this.theOut = null;
                    }
                    else{
                        JOptionPane.showInputDialog(this, "Porfavor Ingrece un nuevo nombre de usuario que el que escribio ya existe");
                        this.txtName.setText("");
                    }
                }
            }  
            
        } catch (IOException ex) {
            Logger.getLogger(JFCliente.class.getName()).log(Level.SEVERE, null, ex);
        }
    }//GEN-LAST:event_btnConectarceMouseClicked

    private void btnEnviarMensajeMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_btnEnviarMensajeMouseClicked
       String Mensaje = this.txtEnviarMensaje.getText();
       int dialogButton = JOptionPane.YES_NO_OPTION;
       int dialogResult = JOptionPane.showConfirmDialog (null, "Desea a enviar a todos los usuarios conectados ?","Warning",dialogButton);
       if(dialogResult == JOptionPane.YES_OPTION){
           sendAll(Mensaje);
       }
       else{
           JOptionPane.showInputDialog(this, "Debio previamnte seleccionar al usuario que quiere enviarle el mensaje");
           sendPersonal(Mensaje , this.usuAEnviar);
       }
        
        
    }//GEN-LAST:event_btnEnviarMensajeMouseClicked

    private void jLstUsuariosConectadosKeyPressed(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_jLstUsuariosConectadosKeyPressed
        // TODO add your handling code here:
    }//GEN-LAST:event_jLstUsuariosConectadosKeyPressed

    private void jLstUsuariosConectadosValueChanged(javax.swing.event.ListSelectionEvent evt) {//GEN-FIRST:event_jLstUsuariosConectadosValueChanged
        
        this.usuAEnviar = this.jLstUsuariosConectados.getSelectedValue();
        if(!this.usuAEnviar.equals(this.nombreUsuario)){
            this.seleUsuEnviar = true;
        }
        else{
            this.usuAEnviar = "";
        
        }
        
        
    }//GEN-LAST:event_jLstUsuariosConectadosValueChanged

    
    private void sendAll(String Mensaje){
        try {
            System.out.println("Entro por enviar a todos..");
            this.theOut.print("SENDALL " + Mensaje);
            String res = this.theIn.readLine();
            if(res.startsWith("100")){
                JOptionPane.showConfirmDialog(this, "Mensaje enviado con exito");
            }
            else{
                JOptionPane.showConfirmDialog(this, "Mensaje No se envio  ");
            }
        } catch (IOException ex) {
            Logger.getLogger(JFCliente.class.getName()).log(Level.SEVERE, null, ex);
        }     
    }
    
    private void sendPersonal(String Mensaje, String Destinatario){
        try {
            this.theOut.print("SEND " + Destinatario + " " + Mensaje);
            String res = this.theIn.readLine();
            if(res.startsWith("100")){
                JOptionPane.showConfirmDialog(this, "Mensaje enviado con exito al usuario " + Destinatario);
            }
            else{
                JOptionPane.showConfirmDialog(this, "Mensaje No se envio  ");
            }
        } catch (IOException ex) {
            Logger.getLogger(JFCliente.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
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
            java.util.logging.Logger.getLogger(JFCliente.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(JFCliente.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(JFCliente.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(JFCliente.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new JFCliente().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnConectarce;
    private javax.swing.JButton btnEnviarMensaje;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JList<String> jList1;
    private javax.swing.JList<String> jLstUsuariosConectados;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private java.awt.Label label1;
    private java.awt.Label label2;
    private java.awt.Label label3;
    private java.awt.Label label4;
    private java.awt.Label label5;
    private java.awt.Label label6;
    private javax.swing.JTextField txtEnviarMensaje;
    private javax.swing.JTextField txtHost;
    private javax.swing.JTextField txtName;
    private javax.swing.JTextField txtPort;
    // End of variables declaration//GEN-END:variables
}
