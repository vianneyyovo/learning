package com.orsys.demotestu.services.test;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import  org.junit.jupiter.api.*

import com.orsys.demotestu.services.Calculatrice;

public class Calculatrice2Test {

	private Calculatrice calculatrice;

	@Before
	public void initialiserDonneestest() {
		calculatrice = new Calculatrice();
	}

	@Test
	public void testAddition() {
		// R�sultat de Additionner 3 et 4 
		long resultat = calculatrice.addition(3, 4);
		
		// Verifier que le resultat correspond � attente --> 7
		assertEquals(7, resultat,0);
		
		//fail("Not yet implemented");
	}

	@Test
	public void testSoustraction() {
		long resultat = calculatrice.soustraction(10, 5);
		assertEquals(5, resultat,0);
	}
	
	@Test
	public void testDivisionNonEgaleAZero() {
		long resultat = calculatrice.division(10, 5);
		assertEquals(2, resultat,0);
	}
	
	@Test(expected=ArithmeticException.class,timeout=1)
	public void testDivisionZero() {
		long resultat = calculatrice.division(10, 0);
		assertEquals(2, resultat,0);
	}
	
	@After
	public void supprimerDonneestest() {
		calculatrice = null ;
	}

}
