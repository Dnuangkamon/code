
import java.awt.*;
import javax.swing.*;

public class SimpleCalGUI {
    private JFrame fr;
    private JPanel panel;
    private JTextField text1, text2, text3;
    private JButton bn1, bn2, bn3, bn4;
    public SimpleCalGUI() {
        fr = new JFrame("เครื่องคิดเลข");
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        //
        text1 = new JTextField();
        fr.add(text1);
        
        //
        text2 = new JTextField();
        fr.add(text2);
        
        //
        panel = new JPanel();
        bn1 = new JButton("Plus");
        bn2 = new JButton("Minus");
        bn3 = new JButton("Multipy");
        bn4 = new JButton("Divide");
        panel.setLayout(new FlowLayout());
        panel.add(bn1);
        panel.add(bn2);
        panel.add(bn3);
        panel.add(bn4);
        fr.add(panel);
        
        //
        text3 = new JTextField();
        fr.add(text3);
        
        //
        fr.setLayout(new GridLayout(4,1));
        fr.pack();
        fr.setSize(400, 220);
        fr.setVisible(true);
    }
     public static void main(String[] args) {
        new SimpleCalGUI();
        } 
}
