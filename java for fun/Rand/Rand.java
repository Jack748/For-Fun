import java.lang.*;
public class Rand{
    public static void main (String[]args){
		long startTime = System.nanoTime();
		
	    int tot = 0;
    double media = 0;
    while(tot < 1000){
        int x = (int) (Math.random()*100);
        int n = (int) (Math.random()*100);
        int i = 1;
        while(x != n){
            x = (int) (Math.random()*100);
            i++;
        }
        media = media + i;
        tot++;
    }
    media = media/(double)tot;
   // System.out.println(media);

    tot = 0;
    media = 0;
    while(tot < 1000){
		
		int quante = 1;
		int k = (int) (Math.random()*100);
		int h = (int) (Math.random()*100);
		while(k != h){
			k = (int) (Math.random()*100);
			h = (int) (Math.random()*100);
			quante++;
		}
		
		int troppe = 1;
		int tante = 1;
		//System.out.println(quante);
		while(quante != tante){
			k = (int) (Math.random()*100);
			h = (int) (Math.random()*100);
			tante = 1;
			while(k != h){
				k = (int) (Math.random()*100);
				h = (int) (Math.random()*100);
				tante++;
			}
			//System.out.println(tante);
			troppe++;
		}
	media = media + troppe;
    tot++;
    }
    media = media/(double)tot;
    System.out.println(media);
	
/*	long endTime = System.nanoTime();
	long duration = (endTime - startTime) / 1000000;  //divide by 1000000 to get milliseconds.
	System.out.println("\n\n" + duration);
*/

    

    }
}
