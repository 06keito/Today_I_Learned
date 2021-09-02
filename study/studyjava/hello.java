import jdk.jfr.Timestamp;

//Reference : Java本格入門
//https://github.com/acroquest/javabook-support

class HelloWorld {
    public static void main(String[] args) {
        String comment = "Hello World!";
        System.out.println(comment);
    }
}

class Basic_Arithmetic_Operations{
    public static void main(String[] args) {
        int numberA = 10;
        int numberB = 20;
        int numberC = numberA + numberB;
        System.out.println(numberC);
        Test_for_loop();
    }
    void Test_for_loop(){
        for(int i=0; i<5; i++){
            System.out.print(i);
        }
    }
}

class Bool_Check{
    public static void main(String[] args) {
        boolean conditionA = true;
        boolean conditionB = false;
        System.out.println(conditionA);
    }
}

class Student{
    String name;
    int score;
    static final int MAX_SCORE = 100;
    Student(String name, int score){
        this.name = name;
        this.score = score;
    }
    Student(String name){
        this(name,0);
    }
    String GetName(){
        return name;
    }
    void SetName(String name){
        this.name = name;
    }
    int GetScore(){
        return score;
    }
    void SetScore(int score){
        this.score = score;
    }
    void PrintScore(String[] args){
        System.out.println(name+":"+score+"/"+MAX_SCORE);
    }
}

