import java.util.*;
import java.io.*;
import java.util.concurrent.*;
class Blackjackke{
	
	public static void main(String[] args) throws InterruptedException {
		
		int partite = 1000000;
		double vittorie = 0;
		double sconfitte = 0;
		
	for(; partite >= 0; partite--){	
		Scanner input = new Scanner(System.in);
		String s = null;
		// pulisci();
		int x = prendicarta();
		int y = prendicarta();
		if(x == 1 || y == 1){
			if(x+y == 11)
				vittorie++;
		}
		else{
			int sg = x + y;
			// System.out.println("\nLe carte pescate sono " + x + " e " + y + "\n\nTU  -----------------> " + sg);
			int k = prendicarta();
			// System.out.println("\nBANCO  -------------->  " + k);
			int h = prendicarta();
			
		//	System.out.println("\nVuoi un' altra carta?");
		//	s = input.next();		
		//	while((s.equals("si") || s.equals("s")) && sg < 21){
			while(sg < 17){
				x = prendicarta();
				sg += x;
				// pulisci();
				// System.out.println("\nLa carta pescate e' " + x + "\nTU  -----------------> " + sg);
				// System.out.println("\nBANCO  -------------->   " + k);
			/*	if(sg < 21){
					System.out.println("\nVuoi un' altra carta?");
					s = input.next();
				}
			*/
			}
			
			if(sg > 21)
			//	System.out.println("SCONFITTA :'(");
				sconfitte++;
			else{
				//TimeUnit.SECONDS.sleep(1);
				// pulisci();
				int sb = k + h;
				// System.out.println("\nTU  -----------------> " + sg);
				// System.out.println("\nBANCO  -------------->  " + sb);
				if(k == 1 || h == 1){
					if(k+h == 11)
						sconfitte++;
				}
				else{
				while(sb < 17){
					k = prendicarta();
					sb += k;
				//	TimeUnit.SECONDS.sleep(1);
					// pulisci();
					// System.out.println("\nTU  -----------------> " + sg);
					// System.out.println("\nBANCO  --------------> " + sb);
				}
				// pulisci();
				// System.out.println("\nTU  -----------------> " + sg);
				// System.out.println("\nBANCO  --------------> " + sb);
				if(sb > 21 || sg > sb)
					vittorie++;
				//	System.out.println("\nCOMPLIMENTONI!");
				else if(sg == sb)
					partite++;
				else
					sconfitte++;
				//	System.out.println("\nSCONFITTA :'(");
			}
			}
		}
	}
	System.out.println("win rate: " + ((vittorie/(sconfitte+vittorie))*100) + "%");
			
	}
	
	
	static int prendicarta(){
		Random random = new Random();
		int a = 1; // numero minimo
		int b = 13; // numero massimo
		int c = ((b-a) + 1);
		int x = random.nextInt(c) + a;
		if(x > 10)
			x = 10;
		
		return x;
	}
	
	static void pulisci(){
		for(int i = 0; i < 25; i++)
			System.out.println();
	}
	
	
}