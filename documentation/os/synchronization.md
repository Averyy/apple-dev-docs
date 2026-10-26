# Synchronization

**Framework**: os  
**Role**: API Collection

Access low-level synchronization mechanisms to control state across threads.

#### Overview

> **Note**: When possible, use higher-level synchronization primitives such as `pthread`, Grand Central Dispatch, or Swift’s concurrency features to control access to state across different threads. For more information, see [Updating an app to use strict concurrency](../Swift/updating-an-app-to-use-strict-concurrency.md).

## Topics

### Swift Wrappers
- [struct OSAllocatedUnfairLock](./osallocatedunfairlock.md)
  A structure that creates an unfair lock.
- [struct OSAllocatedUnfairLockFlags](./osallocatedunfairlockflags.md)
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
### Futex Conditional Wait Primitives
- [os_sync_wait_on_address](./os_sync_wait_on_address.md)
  An atomic compare-and-wait operation, used to implement higher-level synchronization primitives.
- [os_sync_wait_on_address_with_deadline](./os_sync_wait_on_address_with_deadline.md)
  An atomic compare-and-wait operation with a deadline, used to implement higher-level synchronization primitives.
- [os_sync_wait_on_address_with_timeout](./os_sync_wait_on_address_with_timeout.md)
  An atomic compare-and-wait operation with a timeout, used to implement higher-level synchronization primitives.
- [os_sync_wait_on_address_flags_t](./os_sync_wait_on_address_flags_t.md)
  Flags to control futex wait behavior.
- [os_sync_wake_by_address_all](./os_sync_wake_by_address_all.md)
  An atomic operation that wakes all threads blocked on a futex wait, used to implement higher-level synchronization primitives.
- [os_sync_wake_by_address_any](./os_sync_wake_by_address_any.md)
  An atomic operation that wakes one thread blocked on a futex wait, used to implement higher-level synchronization primitives.
- [os_sync_wake_by_address_flags_t](./os_sync_wake_by_address_flags_t.md)
  Flags to control futex wake behavior.

## See Also

### Task Management
- [Workgroups](./workgroups.md)
  Schedule one or more threads to run at regular intervals and before specific deadlines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/synchronization)*