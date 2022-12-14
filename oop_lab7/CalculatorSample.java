
import java.awt.*;
import javax.swing.*;

public class CalculatorSample {

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
        multiply = new JButton("X");
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
    }

    public static void main(String[] args) {
        new CalculatorSample();

    }

}
