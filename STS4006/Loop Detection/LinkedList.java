import java.util.Scanner;

public class LinkedList {
    //Node Structure
    static class Node{
        int data;
        Node next;
        Node(int d){
            data = d;
            next = null;
        }
    }
    Node head;
    //Push (insertion)
    void push(int newData){
        Node newNode = new Node(newData);
        newNode.next = head;
        head = newNode;
    }
    //Detect loop
    boolean detectLoop(){
        Node slow = head;
        Node fast = head;
        while(slow != null && fast != null && fast.next != null){
            slow = slow.next; //move by 1;
            fast = fast.next.next; //move by 2
            if(slow == fast) return true; //loop detected
        }
        return false;
    }
    //Print result
    void printLoot(){
        if(detectLoop()) System.out.println("Loop found");
        else System.out.println("Loop not found");
    }
    //Driver code
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList list = new LinkedList();
        System.out.print("Enter number of nodes: ");
        int n = sc.nextInt();
        System.out.println("Enter " + n + " node values:");
        for(int i=0; i<n; i++){
            int val = sc.nextInt();
            list.push(val);
        }
        System.out.print("Do you want to create a loop? ('y'/'n'): ");
        char choice = sc.next().charAt(0);
        if(choice == 'y' && list.head != null){
            System.out.print("Enter position to connect last node: ");
            int pos = sc.nextInt();
            //Find last node
            Node last = list.head;
            while(last.next != null) {
                last = last.next;
            }
            //Find target node at position
            Node target = list.head;
            for(int i=1; i<pos && target != null; i++){
                target = target.next;
            }
            if(target != null){
                last.next = target; //create loop
                System.out.println("Loop created at position " + pos);
            }
            else{
                System.out.println("Invalid position, no loop created");
            }
        }
        list.printLoot();
        sc.close();
    }
}
