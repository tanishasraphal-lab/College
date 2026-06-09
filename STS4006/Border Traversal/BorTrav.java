import java.util.*;

public class BorTrav {
    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) {
            this.val = val;
        }
    }
    public static TreeNode buildTree(String[] values) {
        if (values.length == 0 || values[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(values[0]));
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (!q.isEmpty() && i < values.length) {
            TreeNode curr = q.poll();
            if (i < values.length && !values[i].equals("null")) {
                curr.left = new TreeNode(Integer.parseInt(values[i]));
                q.add(curr.left);
            }
            i++;
            if (i < values.length && !values[i].equals("null")) {
                curr.right = new TreeNode(Integer.parseInt(values[i]));
                q.add(curr.right);
            }
            i++;
        }
        return root;
    }
    private static void Left(TreeNode node) {
        if (node == null || (node.left == null && node.right == null)) return;
        System.out.print(node.val + " ");
        Left(node.left != null ? node.left : node.right);
    }
    private static void Leaves(TreeNode node) {
        if (node == null) return;
        if (node.left == null && node.right == null) {
            System.out.print(node.val + " ");
            return;
        }
        Leaves(node.left);
        Leaves(node.right);
    }
    private static void Right(TreeNode node) {
        if (node == null || (node.left == null && node.right == null)) return;
        Right(node.right != null ? node.right : node.left);
        System.out.print(node.val + " ");
    }
    public static void boundaryTraversal(TreeNode root) {
        if (root == null) return;
        System.out.print(root.val + " ");
        Left(root.left);
        if (!(root.left == null && root.right == null)) Leaves(root);
        Right(root.right);
    }
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter tree nodes in level order (use null for missing nodes):");
        String[] tree = sc.nextLine().split(" ");
        TreeNode root = buildTree(tree);
        System.out.print("Boundary Traversal: ");
        boundaryTraversal(root);
        sc.close();
    }
}