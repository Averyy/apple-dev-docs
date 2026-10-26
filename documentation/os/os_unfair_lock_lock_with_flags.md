# os_unfair_lock_lock_with_flags

**Framework**: os  
**Kind**: func  
**Role**: Function

Performs a low-level lock that acquires a passed-in lock, blocks if another thread currently holds that lock, and applies optional behavior flags.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```c
extern void os_unfair_lock_lock_with_flags(os_unfair_lock_t lock, os_unfair_lock_flags_t flags);
```

## Parameters

- `lock`: A pointer to the unfair lock to be locked.
- `flags`: Flags that affect the behavior of the lock. For possible values, see [`os_unfair_lock_flags_t`](./os_unfair_lock_flags_t.md).

## See Also

### Unfair Locking
- [os_unfair_lock](./os_unfair_lock.md)
  A structure that contains the data for an unfair lock.
- [OS_UNFAIR_LOCK_INIT](./os_unfair_lock_init.md)
  A value you use to initialize a new unfair lock.
- [os_unfair_lock_t](./os_unfair_lock_t.md)
  A pointer to an unfair lock structure.
- [os_unfair_lock_lock](./os_unfair_lock_lock.md)
  Performs a low-level lock that acquires a passed-in lock, and blocks if another thread currently holds that lock.
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

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_unfair_lock_lock_with_flags)*