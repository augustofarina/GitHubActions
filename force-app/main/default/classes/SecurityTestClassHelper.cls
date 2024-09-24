public class SecurityTestClassHelper {
    public static void dangerousDebug() {
        List<OauthToken> tokenList = [SELECT AccessToken FROM OauthToken];
        System.debug(tokenList[0].AccessToken);
    }
    private static void uselessMethod() {
        Map<String, Schema.SObjectType> gd;
        for (Integer g = 0; g < 50; g = g + 1){
        	gd = Schema.getGlobalDescribe();
        }
    }
    public static void usingUselessMethod() {
        uselessMethod();
    }
}