# Reflection on Domain Modeling and Class Diagram Development

## 1. Challenges Faced in Designing the Domain Model and Class Diagram:

When designing the domain model and class diagram for the library system, I encountered several challenges. One of the primary difficulties was ensuring a clear and accurate representation of entities and their relationships. Initially, I struggled with abstracting real-world concepts into manageable entities and determining their precise attributes and methods. For example, deciding how detailed the `User` class should be was tricky. Should it just include basic information like name and email, or should it also capture details like borrowing history or a user’s preferences? Striking the right balance between simplicity and completeness was key.

Another challenge was defining the relationships between classes, particularly between `Loan` and `Book`. Since one loan can involve multiple books (if a user borrows several books at once), while each book can only be associated with one loan at a time, understanding and accurately representing these relationships was a complex task. I had to carefully consider multiplicity to ensure it was meaningful and accurate, leading to the realization that I needed a clearer understanding of how entities interact within the system.

Additionally, defining methods for each class presented its own set of problems. Some methods were straightforward, such as `borrowBook()` for the `User` class, but others, like `calculateFine()` for the `Loan` class, required deeper thinking about the system’s rules. How do fines accrue? What triggers the calculation? Establishing clear and correct methods was essential to avoid confusion in the system’s behavior later.

## 2. Alignment with Prior Assignments (Use Cases, State Diagrams, and Requirements):

The class diagram and domain model I developed align closely with the work done in earlier assignments. The **requirements** (from Assignment 4) identified the core entities and their interactions, which directly influenced the design of the domain model. The **use cases** (from Assignment 5) were also integral in defining the system’s behavior, particularly in terms of how `User` interacts with `Book` through `Loan`. For example, the use case for borrowing a book was mirrored in the `borrowBook()` method in the `User` class and the relationship between `Loan` and `Book`.

The **state diagrams** (from Assignment 8) helped inform the behavior of various entities, particularly the `Loan` class. For instance, understanding the different states of a loan (e.g., "active," "overdue," or "closed") provided insights into how the `Loan` class should function, particularly with methods like `closeLoan()` and `calculateFine()`. This alignment ensures that the domain model is consistent with the behaviors and interactions defined in earlier stages of the project.

## 3. Trade-offs Made (Simplifying Inheritance vs. Composition):

While developing the class diagram, I had to make trade-offs between inheritance and composition. Initially, I considered using inheritance to model the relationship between different types of users (e.g., `Student` and `Faculty` subclasses of `User`). However, I ultimately chose to avoid complex inheritance hierarchies in favor of **composition**. The decision was made to keep the model simpler and more flexible. By using composition, I allowed for the possibility of adding specific behaviors or attributes to different user types later on without the need for deep inheritance chains.

For instance, if a `Student` needs to borrow books for a longer period than a regular user, I can add that functionality via composition by introducing a `Student` class that contains a `User` object and overrides methods like `borrowBook()` when necessary. This trade-off was made in the interest of maintainability and flexibility, avoiding the rigidity that deep inheritance can introduce.

## 4. Lessons Learned About Object-Oriented Design:

Through this assignment, I gained valuable insights into **object-oriented design principles**. One major lesson was the importance of **defining clear responsibilities** for each class. Initially, I had some overlap between the responsibilities of `User` and `Loan`, but refining the model helped me understand that each class should focus on a single responsibility. This helped me avoid "fat" classes that did too much and made the system more modular and easier to maintain.

Another key takeaway was the concept of **encapsulation**. By ensuring that attributes like `bookId`, `loanId`, and `fineAmount` were private and providing appropriate methods to access and modify them, I improved the safety and clarity of the design. It became clear how encapsulation not only promotes security but also makes the system more adaptable, as it reduces the chance of unintended modifications.

Finally, the process highlighted the importance of **refining and iterating** on models. Designing a domain model and class diagram is an iterative process, where you may need to revise and adjust relationships and responsibilities as the system’s scope becomes clearer.

## Conclusion:

Overall, this assignment reinforced several key concepts of **object-oriented design**, particularly around modeling entities and their interactions. While there were challenges in abstracting real-world behaviors and defining relationships, the alignment with prior assignments and the trade-offs between inheritance and composition helped create a more flexible and maintainable system. The insights gained will be valuable as I continue working with class and domain models in future projects.

---

