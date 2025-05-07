public class DemoOnject {
    public static void main(String[] args) {
        Employer employe = new Employer("YOVO", "Vianney", 27 );
        System.out.println("FIRST" + " " + employe);

        employe.setAge(25);
        employe.setNom("GOZO");
        employe.setPrenom("Adjoavi");

        System.out.println("SECOND" + " " + employe);
        //Directeur directeur = new Directeur("KODJO", "Komlan", 31);


    }
}
