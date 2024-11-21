
import java.util.*;
class Pracs1b {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
       
       
        System.out.println("Enter number of data for list1:");
        int number = sc.nextInt();
        sc.nextLine();
       
        ArrayList<String> list1 = new ArrayList<>();
        for (int i = 0; i < number; i++) {
            list1.add(sc.nextLine());
        }
       
       
        System.out.println("Enter number of data for list2:");
        int head = sc.nextInt();
        sc.nextLine();
       
        ArrayList<String> list2 = new ArrayList<>();
        for (int i = 0; i < head; i++) {
            list2.add(sc.nextLine());
        }
       
       
        System.out.println("Enter number of data for list3:");
        int tail = sc.nextInt();
        sc.nextLine();
       
        ArrayList<String> list3 = new ArrayList<>();
        for (int i = 0; i < tail; i++) {
            list3.add(sc.nextLine());
        }
       
        ArrayList<String>finalList=new ArrayList<>();
        for (int i = 0; i < list1.size(); i++) {
            String str = list1.get(i);
           
            if (list2.contains(str) ) {
                String modifiedString =  " [$]";
                finalList.add(modifiedString);
            }
            else if(list3.contains(str)){
                 String modifiedString =  " [$]";
                finalList.add(modifiedString);
            }
            finalList.add(str);
        }
       
         ArrayList<String> mergedList = new ArrayList<>();
       mergedList.addAll(list2);
       mergedList.addAll(finalList);
        mergedList.addAll(list3);
       
        System.out.println(mergedList);
       
    }
}