import java.util.*;

public class Recover {

    static class Node {
        int data;
        Node left, right;

        Node(int d) {
            data = d;
            left = right = null;
        }
    }

    static Node first, middle, last, prev;

    static void correctBST(Node root) {
        first = middle = last = prev = null;
        correctBSTUtil(root);

        if (first != null && last != null)
            swap(first, last);
        else if (first != null && middle != null)
            swap(first, middle);
    }

    static void correctBSTUtil(Node root) {
        if (root == null)
            return;

        correctBSTUtil(root.left);

        if (prev != null && root.data < prev.data) {
            if (first == null) {
                first = prev;
                middle = root;
            } else {
                last = root;
            }
        }

        prev = root;

        correctBSTUtil(root.right);
    }

    static void swap(Node a, Node b) {
        int temp = a.data;
        a.data = b.data;
        b.data = temp;
    }

    // Traversals
    static void printInorder(Node root) {
        if (root == null) return;
        printInorder(root.left);
        System.out.print(root.data + " ");
        printInorder(root.right);
    }

    static void printPreorder(Node root) {
        if (root == null) return;
        System.out.print(root.data + " ");
        printPreorder(root.left);
        printPreorder(root.right);
    }

    static void printPostorder(Node root) {
        if (root == null) return;
        printPostorder(root.left);
        printPostorder(root.right);
        System.out.print(root.data + " ");
    }

    static Node buildTree(String[] values) {
        if (values.length == 0 || values[0].equals("null"))
            return null;

        Node root = new Node(Integer.parseInt(values[0]));
        Queue<Node> q = new LinkedList<>();
        q.add(root);

        int i = 1;
        while (!q.isEmpty() && i < values.length) {
            Node curr = q.poll();

            if (i < values.length && !values[i].equals("null")) {
                curr.left = new Node(Integer.parseInt(values[i]));
                q.add(curr.left);
            }
            i++;

            if (i < values.length && !values[i].equals("null")) {
                curr.right = new Node(Integer.parseInt(values[i]));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }

    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter level order traversal (space separated, use null for missing nodes):");
        String[] values = sc.nextLine().split(" ");

        Node root = buildTree(values);

        System.out.print("Inorder before recovery: ");
        printInorder(root);
        System.out.println();

        System.out.print("Preorder before recovery: ");
        printPreorder(root);
        System.out.println();

        System.out.print("Postorder before recovery: ");
        printPostorder(root);
        System.out.println();

        correctBST(root);

        System.out.print("\nInorder after recovery: ");
        printInorder(root);
        System.out.println();

        System.out.print("Preorder after recovery: ");
        printPreorder(root);
        System.out.println();

        System.out.print("Postorder after recovery: ");
        printPostorder(root);
        System.out.println();

        sc.close();
    }
}
