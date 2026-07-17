# Java OOP: Encapsulation

Encapsulation keeps an object's data private and exposes controlled operations.
Validation belongs in the method that changes the state so invalid values fail fast.

```java
class BankAccount {
    private int balance;

    void deposit(int amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Amount must be positive");
        }
        balance += amount;
    }

    int getBalance() {
        return balance;
    }
}

public class Main {
    public static void main(String[] args) {
        BankAccount account = new BankAccount();
        account.deposit(500);
        System.out.println("Balance: " + account.getBalance());
    }
}
```

```output
Balance: 500
```
