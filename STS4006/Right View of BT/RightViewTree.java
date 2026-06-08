import java.util.*;

class Node {
    int data;
    Node left, right;

    Node(int data) {
        this.data = data;
        left = right = null;
    }
}

public class RightViewTree {

    static void rightView(Node root) {
        if (root == null)
            return;

        Queue<Node> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int size = q.size();

            for (int i = 1; i <= size; i++) {
                Node curr = q.poll();

                // Print last node of each level
                if (i == size) System.out.print(curr.data + " ");

                if (curr.left != null) q.add(curr.left);

                if (curr.right != null) q.add(curr.right);
            }
        }
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.right = new Node(5);
        root.right.right = new Node(4);

        System.out.print("Right View: ");
        rightView(root);
    }
}