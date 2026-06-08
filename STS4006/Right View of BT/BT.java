import java.util.*; 
public class BT  { 
    static class Node { 
        int data; 
        Node left, right; 
        Node(int d) { 
            data = d; 
            left = right = null; 
        } 
    } 
    public static Node buildTree(String[] values)  { 
        if (values.length == 0 || values[0].equals("null"))  return null; 
        Node root = new Node(Integer.parseInt(values[0])); 
        Queue<Node> queue = new LinkedList<>(); 
        queue.add(root); 
        int i = 1; 
        while (!queue.isEmpty() && i < values.length)  { 
        Node current = queue.poll(); 
        if (i < values.length && !values[i].equals("null"))  { 
            current.left = new Node(Integer.parseInt(values[i])); 
            queue.add(current.left); 
        } 
        i++; 
        if (i < values.length && !values[i].equals("null"))  { 
            current.right = new Node(Integer.parseInt(values[i])); 
            queue.add(current.right); 
        } 
        i++; 
        } 
        return root; 
    } 
    public static List<Integer> rightView(Node root) { 
    List<Integer> result = new ArrayList<>(); 
            if (root == null) return result; 
            Queue<Node> queue = new LinkedList<>(); 
            queue.add(root); 
            while (!queue.isEmpty())  { 
                int size = queue.size(); 
                for (int i = 0; i < size; i++){ 
                    Node current = queue.poll(); 
                    if (i == size - 1) result.add(current.data); 
                    if (current.left != null)  queue.add(current.left); 
                    if (current.right != null)  queue.add(current.right); 
            } 
      } 
        return result; 
    } 
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter tree nodes in level order (use 'null' for empty nodes):");

        if (!sc.hasNextLine()) {
            System.out.println("No input provided.");
            return;
        }

        String[] tree = sc.nextLine().trim().split(" ");
        Node root = buildTree(tree);

        List<Integer> view = rightView(root);
        System.out.print("Right View: ");
        for (int val : view) {
            System.out.print(val + " ");
        }
    }
}
