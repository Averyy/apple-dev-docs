# os_unfair_recursive_lock_assert_owned_by_self

**Framework**: os  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```c
extern void os_unfair_recursive_lock_assert_owned_by_self(const os_unfair_recursive_lock *lock);
```

## Discussion

Asserts that the calling thread is the current owner of the specified lock.

If the lock is currently owned by the calling thread, this function returns.

If the lock is unlocked or owned by a different thread, this function asserts and terminates the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_unfair_recursive_lock_assert_owned_by_self)*