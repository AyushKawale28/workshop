# Java OOP: Runtime Polymorphism

An overridden method is selected from the object's runtime type, even when the
reference uses a superclass type. This behavior is dynamic method dispatch.

```java
class Animal {
    void speak() {
        System.out.println("Animal sound");
    }
}

class Cat extends Animal {
    @Override
    void speak() {
        System.out.println("Meow");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Cat();
        animal.speak();
    }
}
```

```output
Meow
```
