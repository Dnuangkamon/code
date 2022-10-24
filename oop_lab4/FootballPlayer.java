
public class FootballPlayer extends Player {

    private int playerNumber;
    private String position;

    public static void main(String[] args) {

        FootballPlayer p1 = new FootballPlayer();

        p1.setName("Harry");

        p1.setTeam("Gryffindor");

        p1.setPlayerNumber(1);

        p1.setPosition("keeper");

        FootballPlayer p2 = new FootballPlayer();

        p2.setName("Jame");

        p2.setTeam("Gryffindor");

        p2.setPlayerNumber(1);

        p2.setPosition("keeper");

        System.out.println("We are same position : " + p1.isSamePosition(p2));

        System.out.println("We are same team : " + p1.isSameTeam(p2));

    }

    public void setPlayerNumber(int n) {
        playerNumber = n;
    }

    public void setPosition(String p) {
        position = p;
    }

    public int getPlayerNumber() {
        return playerNumber;
    }

    public String getPosition() {
        return position;
    }

    public boolean isSamePosition(FootballPlayer p) {
        if (getTeam().equals(p.getTeam()) && getPosition().equals(p.getPosition())) {
            return true;
        } else {
            return false;
        }
    }
}
