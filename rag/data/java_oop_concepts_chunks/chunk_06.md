# Java OOP: Interfaces

An interface defines a contract that unrelated classes can implement. A class may
implement multiple interfaces, which enables polymorphism without class inheritance.

```java
interface Printable {
    void print();
}

class Invoice implements Printable {
    @Override
    public void print() {
        System.out.println("Printing invoice");
    }
}

public class Main {
    public static void main(String[] args) {
        Printable document = new Invoice();
        document.print();
    }
}
```

```output
Printing invoice
```
