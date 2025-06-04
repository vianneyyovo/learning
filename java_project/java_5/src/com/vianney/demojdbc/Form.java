package com.vianney.demojdbc;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;

public class Form extends JFrame {

    private JTextField titleField;
    private JTextField authorField;
    private JTextField isbnField;
    private JTextField resumField;
    private JButton addButton;

    DemoJdbc db = new DemoJdbc();

    public Form() {
        super("Ajouter un Livre");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1000, 400);
        setLocationRelativeTo(null);


        setLayout(new GridLayout(5, 2, 10, 10));


        add(new JLabel("Titre:"));
        titleField = new JTextField();
        add(titleField);

        add(new JLabel("Auteur:"));
        authorField = new JTextField();
        add(authorField);

        add(new JLabel("ISBN:"));
        isbnField = new JTextField();
        add(isbnField);

        add(new JLabel("Résumé:"));
        resumField = new JTextField();
        add(resumField);


        addButton = new JButton("Ajouter");
        add(addButton);


        add(new JLabel("by vianney"));

        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addBook();
            }
        });

        setVisible(true);
        readData();

    }

    public void addBook() {
        String title = titleField.getText();
        String author = authorField.getText();
        String isbn = isbnField.getText();
        String resum = resumField.getText();

        try {
            db.getConnection();
            db.createStatement(title, author, isbn, resum);

            JOptionPane.showMessageDialog(this, "Livre ajouté avec succès !");
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "Erreur : " + ex.getMessage(), "Erreur", JOptionPane.ERROR_MESSAGE);
        }
    }


    public void readData() {
        db.getConnection();
        db.readData();

    }

}
