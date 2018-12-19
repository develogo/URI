import java.io.IOException;
import java.util.Scanner;
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
        String [] valores;
		int a1,b1,c1,d1;
		Scanner in = new Scanner(System.in);
		
		 valores = in.nextLine().split(" ");
		 
	
		 a1 = Integer.parseInt(valores[0]);
		 b1 = Integer.parseInt(valores[1]);
		 c1 = Integer.parseInt(valores[2]);
		 d1 = Integer.parseInt(valores[3]);
		 
		 
	
		if(b1 > c1 && d1>a1 && ((c1+d1) >(a1+b1)) && (c1 >=0 && d1>=0) && a1%2 == 0) {
			System.out.println("Valores aceitos");
		}
		
		else {
			System.out.println("Valores nao aceitos");
		}
 
    }
 
}