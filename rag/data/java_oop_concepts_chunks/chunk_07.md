# Java OOP: Composition

Composition models a has-a relationship by storing one object inside another.
It keeps classes focused and is usually more flexible than inheriting implementation.

```java
class Engine {
    void start() {
        System.out.println("Engine started");
    }
}

class Car {
    private final Engine engine = new Engine();

    void start() {
        engine.start();
        System.out.println("Car is ready");
    }
}

public class Main {
    public static void main(String[] args) {
        Car car = new Car();
        car.start();
    }
}
```

```output
Engine started
Car is ready
```
