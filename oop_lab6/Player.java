
public abstract class Player {
    private double HP;
    private double MP;
    private double EXP;
    private double Money;
    private double ATK;
    
    //get return 
    //set set value
    
    
    public double getHP() {
        return HP;
    }
    
    public void setHP(double HP){
        if(HP < 0) {
            this.HP = 0;
        }
        else{
            this.HP = HP;
        }
    }
    
    public double getMP() {
        return MP;
    }
    
    public void setMP(double MP){
        if(MP < 0) {
            this.MP = 0;
        }
        else{
            this.MP = MP;
        }
    }
    
    public double getEXP() {
        return EXP;
    }
    
    public void setEXP(double EXP){
        if(EXP < 0) {
            this.EXP = 0;
        }
        else{
            this.EXP = EXP;
        }
    }
    
    public double getMoney() {
        return Money;
    }
    
    public void setMoney(double Money){
        if(Money < 0) {
            this.Money = 0;
        }
        else{
            this.Money = Money;
        }
    }
    
    public double getATK() {
        return ATK;
    }
    
    public void setATK(double ATK){
        if(ATK < 0) {
            this.ATK = 0;
        }
        else{
            this.ATK = ATK;
        }
    }
    
    @Override
    public String toString() {
        return ("HP : " + this.HP + " MP : " + this.MP + " ATK : " + this.ATK);
    }
    
    public abstract void attack(Player p);
    public abstract void attacked(double n);
}
