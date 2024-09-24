@isTest
private class SecurityHandler {
    @isTest
    static void thisTest() {
        SecurityTestClassHelper.usingUselessMethod();
        SecurityTestClassHelper.dangerousDebug();
        System.assertEquals(1, 1);
    }
}