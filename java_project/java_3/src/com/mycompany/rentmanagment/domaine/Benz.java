package com.mycompany.rentmanagment.domaine;

public class Benz implements Voiture {
    @Override
    public void demarrer() {
        System.out.println("com.mycompany.rentmanagment.domaine.Benz is starting");
    }

    @Override
    public void arreter() {
        System.out.println("com.mycompany.rentmanagment.domaine.Benz is stopping");
    }

}
