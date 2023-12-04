//System.gc() 메서드를 실행했을 때의 시간 측정을 해보자.
public class SystemGcTest {
    public static void main(String[] args) {
        
        noSystemGc(); // 결과값 : 내 pc기준으로 125ns로 나온다.

        systemGc(); // 결과값 : 3835083ns


    }

    static void noSystemGc() {
        long startTime = System.nanoTime();
        long endTime = System.nanoTime();

        System.out.println(endTime - startTime + "ns");
    }

    static void systemGc() {
        long startTime = System.nanoTime(); 

        System.gc();

        long endTime = System.nanoTime();

        System.out.println(endTime - startTime + "ns"); 
    }
}


