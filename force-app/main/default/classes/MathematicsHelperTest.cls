@isTest
private class MathematicsHelperTest {
	@isTest
    static void testThree() {
        Integer three = MathematicsHelper.getThree();
        System.assertEquals(three, 3);
    }
}