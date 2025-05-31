package com.mycompany.rentmanagment.domaine;

public class Directeur extends Employer {

    public Directeur(String nom, String prenom, int age) {
        super(nom, prenom, age);
    }

    @Override
    public String prendreConger() {
        return this.getNom() + " " + this.getPrenom() + " " + this.getAge() + " " + "Veut  prendre un congé";
    }

}
