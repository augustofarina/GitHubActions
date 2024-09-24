public class SecurityTestClassHelper {
    public static void dangerousDebug() {
        List<OauthToken> tokenList = [SELECT AccessToken FROM OauthToken];
        if (tokenList[0] != null) {
        	System.debug(tokenList[0].AccessToken);
		}
    }
    public static void uselessMethod() {
        Integer number5 = 5;
    }
    public static void usingUselessMethod() {
        uselessMethod();
    }
}