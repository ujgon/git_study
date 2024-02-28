import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class hello {
    public static void main(String[] args) {
        int[] grade = {2, 2, 1};

        int[] sortGrade = grade;
        Arrays.sort(sortGrade);

        Map<Integer, Integer> answerMap = new HashMap<>();

        for(int i=0 ; i<grade.length ; i++) {
            answerMap.put(sortGrade[i], grade.length-i);
        }

        int[] answer = new int[grade.length];
        for(int i=0 ; i<grade.length ; i++) {
            answer[i] = answerMap.get(grade[i]);
        }

        for (int i = 0; i < answer.length; i++) {
            System.out.println(answer[i]);
        }
    }
}