# Uninitialized mutexes

**Framework**: Xcode

Detects when you use an uninitialized mutex.

#### Overview

Use this check to detect when you call `pthread_mutex_lock(_:)` or `pthread_mutex_unlock(_:)` with an uninitialized `pthread_mutex_t` variable. Attempting to use an uninitialized mutex results in an error, and bypasses ordering conditions that exist on a locked mutex. Available in Xcode 8 and later.

##### Use of Uninitialized Mutex in C

In the following example, the `pthread_mutex_lock(_:)` function executes with an uninitialized `pthread_mutex_t` variable:

```occ
static pthread_mutex_t mutex;
void performWork() {
    pthread_mutex_lock(&mutex); // Error: uninitialized mutex
    // ...
    pthread_mutex_unlock(&mutex);
}
```

###### Solution

Use the `pthread_once(_:_:)` function to initialize a mutex before you use it.

```occ
static pthread_once_t once = PTHREAD_ONCE_INIT;
static pthread_mutex_t mutex;
void init() {    
    pthread_mutex_init(&mutex, NULL);
}
void performWork() {
    pthread_once(&once, init); // Correct
    pthread_mutex_lock(&mutex);
    // ...
    pthread_mutex_unlock(&mutex);
}
```

## See Also

- [Data races](data-races.md)
  Detects unsynchronized access to mutable state across multiple threads.
- [Swift access races](swift-access-races.md)
  Detects unsynchronized access to mutable state across multiple threads in Swift.
- [Races on collections and other APIs](races-on-collections-and-other-apis.md)
  Detects when one thread accesses a mutable object while another thread is writing to it.
- [Thread leaks](thread-leaks.md)
  Detects when you don’t close threads after use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/uninitialized-mutexes)*