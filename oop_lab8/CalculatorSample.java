
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class CalculatorSample implements ActionListener {

    private JFrame fr;
    private JButton bn0, bn1, bn2, bn3, bn4, bn5, bn6, bn7, bn8, bn9, plus, delete, multiply, divide,
            equal, bnC;
    private JPanel p1, p2;
    private JTextField text;

    public CalculatorSample() {
        fr = new JFrame("My Calculator");
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        bn0 = new JButton("0");
        bn1 = new JButton("1");
        bn2 = new JButton("2");
        bn3 = new JButton("3");
        bn4 = new JButton("4");
        bn5 = new JButton("5");
        bn6 = new JButton("6");
        bn7 = new JButton("7");
        bn8 = new JButton("8");
        bn9 = new JButton("9");
        plus = new JButton("+");
        delete = new JButton("-");
        multiply = new JButton("x");
        divide = new JButton("/");
        bnC = new JButton("c");
        equal = new JButton("=");

        text = new JTextField();
        p1 = new JPanel();
        p2 = new JPanel();

        //creat (1,1)
        text.setEnabled(false);
        p1.setLayout(new GridLayout(1, 1));
        p1.add(text);

        //creat (4,4)
        p2.setLayout(new GridLayout(4, 4));
        p2.add(bn7);
        p2.add(bn8);
        p2.add(bn9);
        p2.add(plus);
        p2.add(bn4);
        p2.add(bn5);
        p2.add(bn6);
        p2.add(delete);
        p2.add(bn1);
        p2.add(bn2);
        p2.add(bn3);
        p2.add(multiply);
        p2.add(bn0);
        p2.add(bnC);
        p2.add(equal);
        p2.add(divide);

        //BorderLayout
        fr.add(p1, BorderLayout.NORTH);
        fr.add(p2);

        fr.setSize(270, 250);
        fr.setVisible(true);

        bn0.addActionListener(this);
        bn1.addActionListener(this);
        bn2.addActionListener(this);
        bn3.addActionListener(this);
        bn4.addActionListener(this);
        bn5.addActionListener(this);
        bn6.addActionListener(this);
        bn7.addActionListener(this);
        bn8.addActionListener(this);
        bn9.addActionListener(this);
        plus.addActionListener(this);
        delete.addActionListener(this);
        multiply.addActionListener(this);
        divide.addActionListener(this);
        bnC.addActionListener(this);
        equal.addActionListener(this);
    }

    public static void main(String[] args) {
        new CalculatorSample();

    }

    public double num1, num2;
    public String sign;

    @Override
    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource().equals(bn0)) {
            text.setText(text.getText() + "0");
        } else if (ae.getSource().equals(bn1)) {
            text.setText(text.getText() + "1");
        } else if (ae.getSource().equals(bn2)) {
            text.setText(text.getText() + "2");
        } else if (ae.getSource().equals(bn3)) {
            text.setText(text.getText() + "3");
        } else if (ae.getSource().equals(bn4)) {
            text.setText(text.getText() + "4");
        } else if (ae.getSource().equals(bn5)) {
            text.setText(text.getText() + "5");
        } else if (ae.getSource().equals(bn6)) {
            text.setText(text.getText() + "6");
        } else if (ae.getSource().equals(bn7)) {
            text.setText(text.getText() + "7");
        } else if (ae.getSource().equals(bn8)) {
            text.setText(text.getText() + "8");
        } else if (ae.getSource().equals(bn9)) {
            text.setText(text.getText() + "9");
            //operator
        } else if (ae.getSource().equals(plus)) {
            num1 = Double.parseDouble(text.getText());
            sign = "+";
            text.setText("");
        } else if (ae.getSource().equals(delete)) {
            num1 = Double.parseDouble(text.getText());
            sign = "-";
            text.setText("");
        } else if (ae.getSource().equals(multiply)) {
            num1 = Double.parseDouble(text.getText());
            sign = "*";
            text.setText("");
        } else if (ae.getSource().equals(divide)) {
            num1 = Double.parseDouble(text.getText());
            sign = "/";
            text.setText("");
        } else if (ae.getSource().equals(bnC)) {
            text.setText("");
        } else if (ae.getSource().equals(equal)) {
            num2 = Integer.parseInt(text.getText());
            double ans_plus = num1 + num2;
            double ans_minus = num1 - num2;
            double ans_multipy = num1 * num2;
            double ans_divide = num1 / num2;
            switch (sign) {
                case "+":
                    text.setText(String.valueOf(ans_plus));
                    break;
                case "-":
                    text.setText(String.valueOf(ans_minus));
                    break;
                case "*":
                    text.setText(String.valueOf(ans_multipy));
                    break;
                case "/":
                    text.setText(String.valueOf(ans_divide));
                    break;
            }
        }
    }
}
