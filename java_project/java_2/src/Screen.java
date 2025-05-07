import javax.swing.*;
import java.util.ArrayList;
import java.util.List;

public class Screen {

    public void screen() {
        JFrame screen;

        screen = new JFrame("JFrame doc TP");

        screen.setSize(500, 500);

        screen.setLocationRelativeTo(null);

        screen.setVisible(true);

        screen.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        List<String> list = new ArrayList<String>();


    }
}
