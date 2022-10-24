
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class TellerGUI implements ActionListener {

    private JFrame fr;
    private JButton Deposit, Withdraw, Exit;
    private JPanel panel;
    private JTextField Balance, Amount;
    private JLabel label_Balance, label_Amount;
    Account n = new Account(6000,"");

    public TellerGUI() {
        fr = new JFrame("TellerGUI");
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.setLayout(new FlowLayout());
        
        //top
        label_Balance = new JLabel("Balance             ");
        Balance = new JTextField(String.valueOf(n.getBalance()), 15);
        Balance.setEditable(false);
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
        
        Deposit.addActionListener(this);
        Withdraw.addActionListener(this);
    }

    public static void main(String[] args) {
        new TellerGUI();
    }
    
    @Override
    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource().equals(Deposit)) {
            n.deposit(Double.parseDouble(Amount.getText()));
            Balance.setText(String.valueOf((int)(n.getBalance())));
        } else if (ae.getSource().equals(Withdraw)) {
            n.withdraw(Double.parseDouble(Amount.getText()));
            Balance.setText(String.valueOf((int)(n.getBalance())));
        }
    }
}

