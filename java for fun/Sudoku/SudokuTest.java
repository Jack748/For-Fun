class SudokuTest{

public static void main(String[] args){
int[][] x = new int [9][9];
Sudoku s = new Sudoku(x);
s.riempi();
s.scriviout();
System.out.println();
s.risolvi();
System.out.println();
s.scriviout();
}
}