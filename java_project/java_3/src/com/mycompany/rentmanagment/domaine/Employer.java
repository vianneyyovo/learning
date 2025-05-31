package com.mycompany.rentmanagment.domaine;

public class Employer extends Personne {
    public Employer(String nom, String prenom, int age) {
        super(nom, prenom, age);
    }

    public String prendreConger() {
        return this.getNom() + " " + this.getPrenom() + " " + "est en congé";
    }

}
