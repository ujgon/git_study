public class Sort {
    public static void sortBySelectionSort(int[] arr) {
        int n = arr.length;
        for(int i=0 ; i<n-1 ; i++){
            boolean change = false;
            for(int j=0 ; j<n-1-j ; j++) {
                if(arr[j] > arr[j+1]) {
                    change = true;
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }    
            }
            if(change == false) break;
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 4, 9, 3, 10};
        sortBySelectionSort(arr);
        System.out.println(arr);
    }
}
