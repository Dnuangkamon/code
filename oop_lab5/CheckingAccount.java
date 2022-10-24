
public class CheckingAccount extends Account{
    private double credit;
    
    public CheckingAccount() {
        super(0, "");
        credit = 0;
    }
    
    public CheckingAccount (double balance, String name, double credit) {
        super(balance, name);
        this.credit = credit;
    }
    
    public void setCredit(double credit) {
        if (credit > 0) {
            this.credit = credit;
        }
        else {
            System.out.println("Input number must be a positive integer.");
        }
    }
    
    public double getCredit() {
        return credit;
    }
    
    
    @Override
    public void withdraw(double a) {
        double ans = balance - a;
        if (a > 0 && ans >= 0) {
            balance = balance - a;
            System.out.println(a+" baht is withdrawn from " + name + " and your credit balance is " + credit + ".");
        }
        else if (ans < 0 && (ans + credit) >= 0) {
            balance = 0;
            credit = credit - a;
            System.out.println(a+" baht is withdrawn from " + name + " and your credit balance is " + credit + ".");
        }
        else {
            System.out.println("Not enough money!");
        }
    }
    
    public void withdraw(String a) {
        double ans = Double.parseDouble(a);
        withdraw(ans);
    }
    
    @Override
    public String toString() {
        return ("The" + (" " + name + " ") + "account has "+balance+" baht and "+credit+" credits.");
    } 
}
