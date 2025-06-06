# Data races

**Framework**: Xcode

Detects unsynchronized access to mutable state across multiple threads.

#### Overview

Use this check to detect when multiple threads access the same memory without synchronization, and at least one access is a write. Available in Xcode 8 and later.

##### Data Race with Producer and Consumer Functions

In the following example, the `producer()` function sets the global variable `message`, and the `consumer()` function waits for a flag to set before printing the message. Because `producer()` executes on one thread and `consumer()` executes on another thread, their execution can be concurrent, creating a data race.

```swift
var message: String? = nil
var messageIsAvailable: Bool = false
// Executed on Thread #1
func producer() {
    message = "hello!"
    messageIsAvailable = true
}
// Executed on Thread #2
func consumer() {
    repeat {
        usleep(1000)
    } while !messageIsAvailable
    print(message)
}
```

###### Solution

Use [`Dispatch`](https://developer.apple.com/documentation/Dispatch) APIs to coordinate access to `message` across multiple threads.

## See Also

- [Swift access races](swift-access-races.md)
  Detects unsynchronized access to mutable state across multiple threads in Swift.
- [Races on collections and other APIs](races-on-collections-and-other-apis.md)
  Detects when one thread accesses a mutable object while another thread is writing to it.
- [Uninitialized mutexes](uninitialized-mutexes.md)
  Detects when you use an uninitialized mutex.
- [Thread leaks](thread-leaks.md)
  Detects when you don’t close threads after use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/data-races)*