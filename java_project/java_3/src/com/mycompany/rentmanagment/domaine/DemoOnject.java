package com.mycompany.rentmanagment.domaine;

public class DemoOnject {
    public static void main(String[] args) {
        Employer employe = new Employer("YOVO", "Vianney", 27 );
        System.out.println("FIRST" + " " + employe);

        employe.setAge(25);
        employe.setNom("GOZO");
        employe.setPrenom("Adjoavi");

        System.out.println("SECOND" + " " + employe);
        //com.mycompany.rentmanagment.domaine.Directeur directeur = new com.mycompany.rentmanagment.domaine.Directeur("KODJO", "Komlan", 31);


    }
}
