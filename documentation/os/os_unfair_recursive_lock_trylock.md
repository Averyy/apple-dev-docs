# os_unfair_recursive_lock_trylock

**Framework**: os  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```c
extern bool os_unfair_recursive_lock_trylock(os_unfair_recursive_lock_t lock);
```

## Return Value

Returns true if the lock was successfully locked and false if the lock was already locked by another thread

## Discussion

Locks an os_unfair_recursive_lock if it is not already locked by another thread.

It is invalid to surround this function with a retry loop, if this function returns false, the program must be able to proceed without having acquired the lock, or it must call os_unfair_recursive_lock_lock() directly (a retry loop around os_unfair_recursive_lock_trylock() amounts to an inefficient implementation of os_unfair_recursive_lock_lock() that hides the lock waiter from the system and prevents resolution of priority inversions).


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_unfair_recursive_lock_trylock)*