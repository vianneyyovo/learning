package com.vianney.demojdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.PreparedStatement;

public class DemoJdbc {

    private Connection connection;

    public DemoJdbc() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            System.err.println("❌ Driver JDBC non trouvé : " + e.getMessage());
        }
    }

    public void getConnection() {
        try {
            if (connection == null || connection.isClosed()) {
                String password = "0210";
                String user = "root";
                String url = "jdbc:mysql://localhost:3306/biblio_db?useSSL=false&serverTimezone=UTC";
                connection = DriverManager.getConnection(url, user, password);
                System.out.println("✅ Connexion établie !");
            }
        } catch (SQLException e) {
            System.err.println("❌ Échec de la connexion : " + e.getMessage());
        }
    }

    public void createStatement( String title, String author, String isbn, String resum) {
        String sql = "INSERT INTO livres (title, author, isbn, resum) VALUES (?, ?, ?, ?)";

        try {
            PreparedStatement pst = connection.prepareStatement(sql);
            pst.setString(1, title);
            pst.setString(2, author);
            pst.setString(3, isbn);
            pst.setString(4, resum);

            int rowsInserted = pst.executeUpdate();
            if (rowsInserted > 0) {
                System.out.println("✅ Livre ajouté avec succès !");
            }
        } catch (SQLException e) {
            System.err.println("Echec de l'inserssion : " + e.getMessage());
        }
    }

    public void closeConnection() {
        try {
            if (connection != null && !connection.isClosed()) {
                connection.close();

                System.out.println("🔒 Connexion fermée.");
            }
        } catch (SQLException e) {
            System.err.println("❌ Erreur lors de la fermeture : " + e.getMessage());
        }
    }
}
