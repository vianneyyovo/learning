//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Employer employer = new Employer("YOVO", "Vianney", 27 );
        Directeur directeur = new Directeur("KODJO", "Komlan", 31);

        Benz benz = new Benz();

        System.out.println(employer.prendreConger());
        System.out.println(directeur.prendreConger());
        benz.demarrer();
        benz.arreter();
    }
}