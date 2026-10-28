# os_unfair_lock_flags_t

**Framework**: os  
**Kind**: enum  
**Role**: Enumeration

Flags that affect the behavior of an unfair locking operation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef enum { ... } os_unfair_lock_flags_t;
```

## Overview

Use these flags with the [`os_unfair_lock_lock_with_flags`](./os_unfair_lock_lock_with_flags.md) function.

## Topics

### Enumeration Cases
- [OS_UNFAIR_LOCK_FLAG_ADAPTIVE_SPIN](./os_unfair_lock_flags_t/os_unfair_lock_flag_adaptive_spin.md)
  A flag to allow an unfair lock caller to spin temporarily before blocking.
- [OS_UNFAIR_LOCK_FLAG_NONE](./os_unfair_lock_flags_t/os_unfair_lock_flag_none.md)
  An empty flag set that tells the lock function to apply no optional behaviors.

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
- [os_unfair_lock_lock_with_flags](./os_unfair_lock_lock_with_flags.md)
  Performs a low-level lock that acquires a passed-in lock, blocks if another thread currently holds that lock, and applies optional behavior flags.
- [os_unfair_lock_trylock](./os_unfair_lock_trylock.md)
  Locks an unfair lock if it is not already locked.
- [os_unfair_lock_unlock](./os_unfair_lock_unlock.md)
  Unlocks an unfair lock.
- [os_unfair_lock_assert_owner](./os_unfair_lock_assert_owner.md)
  Triggers an assertion if the calling thread doesn’t own the specified unfair lock.
- [os_unfair_lock_assert_not_owner](./os_unfair_lock_assert_not_owner.md)
  Triggers an assertion if the calling thread owns the specified unfair lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_unfair_lock_flags_t)*