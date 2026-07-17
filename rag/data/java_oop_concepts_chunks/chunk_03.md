# Java OOP: Inheritance

Inheritance lets a subclass reuse and specialize accessible behavior from a superclass.
Java uses `extends` for class inheritance and supports one direct superclass per class.

```java
class Animal {
    void eat() {
        System.out.println("Animal is eating");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Dog is barking");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();
        dog.bark();
    }
}
```

```output
Animal is eating
Dog is barking
```
