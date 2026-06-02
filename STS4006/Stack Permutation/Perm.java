import java.util.*;
public class Perm {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter number of elements: ");
		int n = sc.nextInt();
		int[] a = new int[n];
		int[] b = new int[n];
		System.out.println("Enter elements of a:");
		for(int i=0; i<n; i++) a[i] = sc.nextInt();
		System.out.println("Enter elements of b:");
		for(int i=0; i<n; i++) b[i] = sc.nextInt();
		Stack <Integer> st = new Stack<>();
		int j = 0;
		for(int i=0; i<n; i++) {
			st.push(a[i]);
			while (!st.isEmpty() && st.peek()==b[j]) {
				st.pop();
				j++;
			}
		}
		System.out.println("Result: " + st.isEmpty());
	}
}