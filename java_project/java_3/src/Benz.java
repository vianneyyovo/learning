public class Benz implements Voiture {
    @Override
    public void demarrer() {
        System.out.println("Benz is starting");
    }

    @Override
    public void arreter() {
        System.out.println("Benz is stopping");
    }

}
