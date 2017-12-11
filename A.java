import java.util.*;
public class A {
   public static boolean compare(String s1, String s2) {
      return s1.charAt(s1.length()-1)==s2.charAt(0);
   }
   
   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      Set<String> set = new HashSet<String>();
      ArrayList<String> r = new ArrayList<String>();
   
      int n = in.nextInt();
      String a;
      for (int i=0;i<n;i++) {
         a = in.next();
         if (set.add(a) == false) {
            System.out.println((i%2 == 0)? "Player 1 lost":"Player 2 lost");
            return;
         }
         r.add(a);
      }
      int i =0;
      while(i+1 < n && compare(r.get(i),r.get(i+1)))
      { 
         i++;
      }
      if (i == n - 1)
         System.out.println("Fair Game");
      else if(i % 2 == 0)
         System.out.println("Player 2 lost");
      else if(i%2 == 1)
         System.out.println("Player 1 lost"); 
   }
}
