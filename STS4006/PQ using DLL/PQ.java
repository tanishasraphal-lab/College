import java.util.Scanner;

public class PQ {

    class Node {
        int data, pri;
        Node next, prev;

        Node(int d, int p) {
            data = d;
            pri = p;
            next = prev = null;
        }
    }

    Node front = null, rear = null;

    void insert(int d, int p) {
        Node newNode = new Node(d, p);

        if (front == null) {
            front = rear = newNode;
        } else if (p < front.pri) {
            newNode.next = front;
            front.prev = newNode;
            front = newNode;
        } else {
            Node temp = front;

            while (temp.next != null && temp.next.pri <= p) {
                temp = temp.next;
            }

            if (temp.next == null) {
                temp.next = newNode;
                newNode.prev = temp;
                rear = newNode;
            } else {
                newNode.next = temp.next;
                temp.next.prev = newNode;
                newNode.prev = temp;
                temp.next = newNode;
            }
        }
    }

    void traverse() {
        Node temp = front;

        while (temp != null) {
            System.out.print("(" + temp.data + ", " + temp.pri + ") ");
            temp = temp.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        PQ pq = new PQ();

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            System.out.print("Enter data and priority: ");
            int d = sc.nextInt();
            int p = sc.nextInt();

            pq.insert(d, p);
        }

        System.out.println("Elements in the Priority Queue:");
        pq.traverse();

        sc.close();
    }
}