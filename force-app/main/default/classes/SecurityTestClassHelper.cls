public class SecurityTestClassHelper {
    public static void dangerousDebug() {
        System.debug('aaaaaaa');
    }
    public static void uselessMethod() {
        Integer number5 = 5;
    }
    public static void usingUselessMethod() {
        uselessMethod();
    }
}