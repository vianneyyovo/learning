package com.orsys.demotestu.services.test;

import static org.junit.Assert.*;


import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import com.orsys.demotestu.services.Calculatrice;

public class CalculatriceTest {

	private Calculatrice calculatrice;

	//Arrange
	@Before
	public void initialiserDonneestest() {
		calculatrice = new Calculatrice();
	}

	@Test
	public void testAddition() {
		//Act
		// R�sultat de Additionner 3 et 4 
		long resultat = calculatrice.addition(3, 4);

		//Assert
		// Verifier que le resultat correspond � attente --> 7
		assertEquals(7, resultat,0);
		
		//fail("Not yet implemented");
	}

	@Test
	public void testSoustraction() {
		long resultat = calculatrice.soustraction(10, 5);

		assertEquals(5, resultat,0);
	}

	
	@After
	public void supprimerDonneestest() {
		calculatrice = null ;
	}

}
