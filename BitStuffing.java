import java.util.*;
class BitStuffing{
    public static void main(String args[]){
        ArrayList<Integer>arr=new ArrayList<Integer>();
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter length of binary digit:");
        int number=sc.nextInt();
        sc.nextLine();
        int count=0;
        System.out.println("Enter binary digits:");
        for(int i=0;i<number;i++){
            arr.add(sc.nextInt());
        }
        System.out.println(arr);
        ArrayList<Integer>finalArr=new ArrayList<Integer>();
        for(int i=0;i<arr.size();i++){
            int value=arr.get(i);
            finalArr.add(value);
            if(value==1){
                count++;
            }
            if(value==0){
                count=0;
            }
            
            if(count==5){
                finalArr.add(0);
                count=0;
            }
        }
        
        System.out.println(finalArr);
    }
}