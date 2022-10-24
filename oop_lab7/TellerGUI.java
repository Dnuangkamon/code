
import java.awt.*;
import javax.swing.*;

public class TellerGUI {

    private JFrame fr;
    private JButton Deposit, Withdraw, Exit;
    private JPanel panel;
    private JTextField Balance, Amount;
    private JLabel label_Balance, label_Amount;

    public TellerGUI() {
        fr = new JFrame("TellerGUI");
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.setLayout(new FlowLayout());
        
        //top
        label_Balance = new JLabel("Balance             ");
        Balance = new JTextField("6000", 15);
        fr.add(label_Balance);
        fr.add(Balance);
        
        //center
        label_Amount = new JLabel("Amount             ");
        Amount = new JTextField(15);
        fr.add(label_Amount);
        fr.add(Amount);
        
        //low
        Deposit = new JButton("Deposit");
        Withdraw = new JButton("Withdraw");
        Exit = new JButton("Exit");

        panel = new JPanel();

        panel.add(Deposit);
        panel.add(Withdraw);
        panel.add(Exit);
        
        fr.pack();
        fr.add(panel, BorderLayout.SOUTH);
        fr.setSize(300, 150);
        fr.setVisible(true);
    }

    public static void main(String[] args) {
        new TellerGUI();
    }
}
