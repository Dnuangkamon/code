
public class Player {

    private String name;
    private String team;

    public static void main(String[] args) {
        Player p1 = new Player();
        p1.setName("Bank");
        p1.setTeam("Gate OR");
        Player p2 = new Player();
        p2.setName("Khim");
        p2.setTeam("Gate OR");
        if (p1.isSameTeam(p2)) {
            System.out.println(p1.getName() + " is a same team with " + p2.getName());
        } else {
            System.out.println(p1.getName() + " is not a same team with " + p2.getName());
        }
    }

    public void setName(String n) {
        name = n;
    }

    public void setTeam(String t) {
        team = t;
    }

    public String getName() {
        return name;
    }

    public String getTeam() {
        return team;
    }

    public boolean isSameTeam(Player p) {
        if (team.equals(p.team)) {
            return true;
        } else {
            return false;
        }
    }

}
