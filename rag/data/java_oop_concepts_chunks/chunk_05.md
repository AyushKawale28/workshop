# Java OOP: Abstraction

An abstract class can define shared behavior and require subclasses to implement
specific operations. An abstract class cannot be instantiated directly.

```java
abstract class Shape {
    abstract int area();
}

class Rectangle extends Shape {
    private final int width;
    private final int height;

    Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    @Override
    int area() {
        return width * height;
    }
}

public class Main {
    public static void main(String[] args) {
        Shape shape = new Rectangle(4, 3);
        System.out.println("Area: " + shape.area());
    }
}
```

```output
Area: 12
```
