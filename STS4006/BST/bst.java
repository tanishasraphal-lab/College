import java.util.*;

class bst {
    // Inner Node class
    static class Node {
        int data;
        Node left, right;
        Node(int s) {
            data = s;
            left = right = null;
        }
    }

    Node root = null;

    // Method to create tree from array of strings
    void create(String s[]) {
        if (s.length == 0 || s[0].equals("N")) return;
        Queue<Node> q = new LinkedList<>();
        root = new Node(Integer.parseInt(s[0]));
        q.add(root);

        int i = 1;
        while (!q.isEmpty() && i < s.length) {
            Node curr = q.poll();
            if (!s[i].equals("N")) {
                curr.left = new Node(Integer.parseInt(s[i]));
                q.add(curr.left);
            }
            i++;
            if (i >= s.length) break;
            if (!s[i].equals("N")) {
                curr.right = new Node(Integer.parseInt(s[i]));
                q.add(curr.right);
            }
            i++;
        }
    }

    // Inorder traversal
    void inorder(Node root) {
        if (root == null) return;
        inorder(root.left);
        System.out.print(root.data + " ");
        inorder(root.right);
    }

    // Main method
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the elements of the tree in level order (use 'N' for null nodes):");
        String s[] = sc.nextLine().split(" ");
        bst tree = new bst();
        tree.create(s);
        System.out.println("Inorder Traversal of the tree:");
        tree.inorder(tree.root);
        sc.close();
    }
}
