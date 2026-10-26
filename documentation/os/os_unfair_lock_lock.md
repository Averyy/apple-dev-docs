# os_unfair_lock_lock

**Framework**: os  
**Kind**: func  
**Role**: Function

Performs a low-level lock that acquires a passed-in lock, and blocks if another thread currently holds that lock.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```c
extern void os_unfair_lock_lock(os_unfair_lock_t lock);
```

#### Discussion

Consider a lock’s data to be opaque and implementation-defined. Locks contain thread-ownership information that the system may use to attempt to resolve priority inversions.

A lock must be unlocked only from the same thread in which it was locked. Attempting to unlock from a different thread causes a runtime error.

A lock must not be accessed from multiple processes or threads via shared or multiply-mapped memory, because the lock implementation relies on the address of the lock value and owning process.

> **Note**:  This is a replacement for the deprecated `OSSpinLock`. This function doesn’t spin on contention, but instead waits in the kernel to be awoken by an unlock. Like `OSSpinLock`, this function does not enforce fairness or lock ordering—for example, an unlocker could potentially reacquire the lock immediately, before an awoken waiter gets an opportunity to attempt to acquire the lock. This may be advantageous for performance reasons, but also makes starvation of waiters a possibility.

## Parameters

- `lock`: A pointer to the unfair lock to be locked.

## See Also

### Unfair Locking
- [os_unfair_lock](./os_unfair_lock.md)
  A structure that contains the data for an unfair lock.
- [OS_UNFAIR_LOCK_INIT](./os_unfair_lock_init.md)
  A value you use to initialize a new unfair lock.
- [os_unfair_lock_t](./os_unfair_lock_t.md)
  A pointer to an unfair lock structure.
- [os_unfair_lock_lock_with_flags](./os_unfair_lock_lock_with_flags.md)
  Performs a low-level lock that acquires a passed-in lock, blocks if another thread currently holds that lock, and applies optional behavior flags.
- [os_unfair_lock_flags_t](./os_unfair_lock_flags_t.md)
  Flags that affect the behavior of an unfair locking operation.
- [os_unfair_lock_trylock](./os_unfair_lock_trylock.md)
  Locks an unfair lock if it is not already locked.
- [os_unfair_lock_unlock](./os_unfair_lock_unlock.md)
  Unlocks an unfair lock.
- [os_unfair_lock_assert_owner](./os_unfair_lock_assert_owner.md)
  Triggers an assertion if the calling thread doesn’t own the specified unfair lock.
- [os_unfair_lock_assert_not_owner](./os_unfair_lock_assert_not_owner.md)
  Triggers an assertion if the calling thread owns the specified unfair lock.
- [os_unfair_lock_flags_t](./os_unfair_lock_flags_t.md)
  Flags that affect the behavior of an unfair locking operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_unfair_lock_lock)*