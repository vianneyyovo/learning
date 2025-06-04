package com.vianney.demojdbc;

import java.sql.*;


public class DemoJdbc {

    private Connection connection;
    Object data;

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
                System.out.println("Connexion établie !");
            }
        } catch (SQLException e) {
            System.err.println("Échec de la connexion : " + e.getMessage());
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
                System.out.println("Livre ajouté avec succès !");
            }
        } catch (SQLException e) {
            System.err.println("Echec de l'inserssion : " + e.getMessage());
        }
    }

    public void readData() {
        String sql = "SELECT * FROM livres";

        try  {
            PreparedStatement pst = connection.prepareStatement(sql);
            ResultSet rs = pst.executeQuery();

            System.out.println("📚 Liste des livres :");
            while (rs.next()) {
                String title = rs.getString("title");
                String author = rs.getString("author");
                String isbn = rs.getString("isbn");
                String resum = rs.getString("resum");

                System.out.println("- " + title + " | " + author + " | " + isbn + " | " + resum);
            }

        } catch (SQLException e) {
            System.err.println("❌ Échec de lecture : " + e.getMessage());
        }
    }

    public void closeConnection() {
        try {
            if (connection != null && !connection.isClosed()) {
                connection.close();

                System.out.println("Connexion fermée.");
            }
        } catch (SQLException e) {
            System.err.println("Erreur lors de la fermeture : " + e.getMessage());
        }
    }
}
