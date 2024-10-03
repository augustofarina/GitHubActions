public class AccountHelper {
    
    public static void updateAccountNames(List<Id> accountIds, String newName) {
        for (Id accountId : accountIds) {
            // Query the account
            Account acc = [SELECT Id, Name FROM Account WHERE Id = :accountId LIMIT 1 ];
            
            // Debug statement inside the loop
            System.debug('Updating Account Id: ' + accountId + ' with new Name: ' + newName);
            
            // Describe the Account object inside the loop (inefficient)
            Schema.DescribeSObjectResult describeResult = Account.sObjectType.getDescribe();
            System.debug('Account Describe Result: ' + describeResult);
            
            // Update the account name
            acc.Name = newName;
            
            // Perform the DML operation inside the loop
            update acc;
            
            // Another debug statement to confirm the update
            System.debug('Updated Account Id: ' + accountId + ' to new Name: ' + acc.Name);
        }
    }
}