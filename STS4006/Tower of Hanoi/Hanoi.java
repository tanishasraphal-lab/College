import java.util.Scanner;

public class Hanoi {

    static void towerOfHanoi(int n, char src, char aux, char dest) {
        if (n == 1) {
            System.out.println("Move disk 1 from " + src + " to " + dest);
            return;
        }

        towerOfHanoi(n - 1, src, dest, aux);

        System.out.println("Move disk " + n + " from " + src + " to " + dest);

        towerOfHanoi(n - 1, aux, src, dest);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of disks: ");
        int n = sc.nextInt();

        towerOfHanoi(n, 'A', 'B', 'C');

        sc.close();
    }
}