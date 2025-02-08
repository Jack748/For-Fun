import java.util.*;
class Sudoku{

private int[][] celle;
Scanner tastiera = new Scanner(System.in);

public Sudoku(int[][] celle){
this.celle = celle;
}

public void riempi(){
for(int x = 0; x < celle.length; x++)
    for (int y = 0; y < celle[0].length; y++){
        celle[x][y] = tastiera.nextInt();
        scriviout();
    }
}

public void scriviout(){
for(int x = 0; x < celle.length; x++){
     System.out.println();
    for (int y = 0; y < celle[0].length; y++)
        System.out.print(celle[x][y] + " ");        
}
}

public boolean finito(){
for(int x = 0; x < celle.length; x++)
        for (int y = 0; y < celle[0].length; y++)
            if(celle[x][y] == 0)
                return false;
return true;
}

public void risolvi(){
while(!finito()){
scriviout();
System.out.println();
  for(int x = 0; x < celle.length; x++)
        for (int y = 0; y < celle[0].length; y++){
         if(celle[x][y] == 0){ 
          if(controlla(1,x,y) && !controlla(2,x,y) && !controlla(3,x,y) && !controlla(4,x,y) && !controlla(5,x,y) && !controlla(6,x,y) && !controlla(7,x,y) && !controlla(8,x,y) && !controlla(9,x,y))
             celle[x][y] = 1;
          if(!controlla(1,x,y) && controlla(2,x,y) && !controlla(3,x,y) && !controlla(4,x,y) && !controlla(5,x,y) && !controlla(6,x,y) && !controlla(7,x,y) && !controlla(8,x,y) && !controlla(9,x,y))
             celle[x][y] = 2;   
          if(!controlla(1,x,y) && !controlla(2,x,y) && controlla(3,x,y) && !controlla(4,x,y) && !controlla(5,x,y) && !controlla(6,x,y) && !controlla(7,x,y) && !controlla(8,x,y) && !controlla(9,x,y))
             celle[x][y] = 3;   
          if(!controlla(1,x,y) && !controlla(2,x,y) && !controlla(3,x,y) && controlla(4,x,y) && !controlla(5,x,y) && !controlla(6,x,y) && !controlla(7,x,y) && !controlla(8,x,y) && !controlla(9,x,y))
             celle[x][y] = 4;   
          if(!controlla(1,x,y) && !controlla(2,x,y) && !controlla(3,x,y) && !controlla(4,x,y) && controlla(5,x,y) && !controlla(6,x,y) && !controlla(7,x,y) && !controlla(8,x,y) && !controlla(9,x,y))
             celle[x][y] = 5;   
          if(!controlla(1,x,y) && !controlla(2,x,y) && !controlla(3,x,y) && !controlla(4,x,y) && !controlla(5,x,y) && controlla(6,x,y) && !controlla(7,x,y) && !controlla(8,x,y) && !controlla(9,x,y))
             celle[x][y] = 6;   
          if(!controlla(1,x,y) && !controlla(2,x,y) && !controlla(3,x,y) && !controlla(4,x,y) && !controlla(5,x,y) && !controlla(6,x,y) && controlla(7,x,y) && !controlla(8,x,y) && !controlla(9,x,y))
             celle[x][y] = 7;   
          if(!controlla(1,x,y) && !controlla(2,x,y) && !controlla(3,x,y) && !controlla(4,x,y) && !controlla(5,x,y) && !controlla(6,x,y) && !controlla(7,x,y) && controlla(8,x,y) && !controlla(9,x,y))
             celle[x][y] = 8;   
          if(!controlla(1,x,y) && !controlla(2,x,y) && !controlla(3,x,y) && !controlla(4,x,y) && !controlla(5,x,y) && !controlla(6,x,y) && !controlla(7,x,y) && !controlla(8,x,y) && controlla(9,x,y))
             celle[x][y] = 9;
        }
    }
}
}


public boolean controlla(int n, int x, int y){
if(controllariga(n,y) && controllacolonna(n,x) && controllacella(n,x,y))
    return true;
return false;    
}

public boolean controllacella(int n, int x, int y){
int cellan = appartiene(x,y);

if(cellan == 1)
for(int a = 0; a < 3; a++)
        for (int i = 0; i < 3; i++)
            if(celle[i][a] == n)
                return false;

if(cellan == 2)
for(int a = 0; a < 3; a++)
        for (int i = 3; i < 6; i++)
            if(celle[i][a] == n)
                return false;

if(cellan == 3)
for(int a = 0; a < 3; a++)
        for (int i = 6; i < 9; i++)
            if(celle[i][a] == n)
                return false;

if(cellan == 4)
for(int a = 3; a < 6; a++)
        for (int i = 0; i < 3; i++)
            if(celle[i][a] == n)
                return false;

if(cellan == 5)
for(int a = 3; a < 6; a++)
        for (int i = 3; i < 6; i++)
            if(celle[i][a] == n)
                return false;

if(cellan == 6)
for(int a = 3; a < 6; a++)
        for (int i = 6; i < 9; i++)
            if(celle[i][a] == n)
                return false;

if(cellan == 7)
for(int a = 6; a < 8; a++)
        for (int i = 0; i < 3; i++)
            if(celle[i][a] == n)
                return false;

if(cellan == 8)
for(int a = 6; a < 8; a++)
        for (int i = 3; i < 6; i++)
            if(celle[i][a] == n)
                return false;

if(cellan == 9)
for(int a = 6; a < 8; a++)
        for (int i = 6; i < 8; i++)
            if(celle[i][a] == n)
                return false;

return true;
}


public int appartiene(int x, int y){
if(x < 3 && y < 3)
    return 1;

if(2 < x && x < 6 && y < 3)
    return 2;

if(5 < x && x < 9 && y < 3)
    return 3;

if(x < 3 && 2 < y && y < 6)
    return 4;

if(2 < x && x < 6 && 2 < y && y  < 6)
    return 5;

if(5 < x && x < 9 && 2 < y && y  < 6)
    return 6;

if(x < 3 && 5 < y && y  < 9)
    return 7;

if(2 < x && x < 6 && 5 < y && y  < 9)
    return 8;

if(5 < x && x < 9 && 5 < y && y  < 9)
    return 9;
return 0;
}



public boolean controllariga(int x, int c){
for(int r = 0; r < celle.length; r++)
    if(celle[r][c] == x)
        return false;
return true;
}

public boolean controllacolonna(int x, int r){
for(int c = 0; c < celle[0].length; c++)
    if(celle[r][c] == x)
        return false;
return true;
}

public void costruiscivuoto(){
for(int x = 0; x < celle.length; x++)
        for (int y = 0; y < celle[0].length; y++)
            celle[x][y] = 0;
}



}
