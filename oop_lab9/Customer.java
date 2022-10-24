import java.util.*;

public class Customer {

    private String firstName;
    private String lastName;
    ArrayList acct;
    private int numOfAccount;

    public Customer() {
        this.firstName = "";
        this.lastName = "";
        acct = new ArrayList();
    }

    public Customer(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
        acct = new ArrayList();
    }
    
        public void addAccount(Account acct) {
        this.acct.add(acct);
    }

    public Account getAccount(int index) {
        return (Account) acct.get(index);
    }

    public int getNumOfAccount() {
        return acct.size();
    }

    @Override
    public String toString() {
        return (firstName + " " + lastName + " has " + this.getNumOfAccount() + " accounts.");
    }

    public static void main(String[] args) {
        Customer cust = new Customer("Somsri", "Boonjing");
        Account acct1 = new Account(5000, "Somsri01");
        Account acct2 = new Account(3000, "Somsri02");
        cust.addAccount(acct1);
        cust.addAccount(acct2);
        // 
        cust.getAccount(0).withdraw(3000);
        cust.getAccount(1).deposit(3000);
        // 
        System.out.println(cust);
        //
        for (int i = 0; i < cust.getNumOfAccount(); i++) {
            cust.getAccount(i).showAccount();
        }
    }
}
