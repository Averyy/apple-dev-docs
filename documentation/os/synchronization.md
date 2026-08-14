# Synchronization

**Framework**: os

Access low-level synchronization mechanisms to control state across threads.

#### Overview

> **Note**: When possible, use higher-level synchronization primitives such as `pthread`, Grand Central Dispatch, or Swift’s concurrency features to control access to state across different threads. For more information, see [`Updating an app to use strict concurrency`](https://developer.apple.com/documentation/swift/updating-an-app-to-use-strict-concurrency).

## Topics

### Swift Wrappers
- [struct OSAllocatedUnfairLock](osallocatedunfairlock.md)
  A structure that creates an unfair lock.
- [struct OSAllocatedUnfairLockFlags](osallocatedunfairlockflags.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/synchronization)*