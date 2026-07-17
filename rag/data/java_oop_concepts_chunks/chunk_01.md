# Java OOP: Classes and Objects

A class defines state and behavior. An object is a runtime instance of that class.
The `new` keyword constructs an object, and the dot operator accesses its members.

```java
class Car {
    String model;

    void displayModel() {
        System.out.println("Model: " + model);
    }
}

public class Main {
    public static void main(String[] args) {
        Car car = new Car();
        car.model = "Civic";
        car.displayModel();
    }
}
```

```output
Model: Civic
```
