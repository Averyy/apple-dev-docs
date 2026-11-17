# os_unfair_recursive_lock_flags_t

**Framework**: os  
**Kind**: enum  
**Role**: Enumeration

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
typedef enum { ... } os_unfair_recursive_lock_flags_t;
```

## Overview

This flag allows the caller of os_unfair_recursive_lock_lock_with_flags API to spin temporarily before blocking, particularly useful when the holder of the lock is on core. This should only be used for locks where the protected critical section is always extremely short. When reacquiring a lock already held by the calling thread, this flag does nothing.

## Topics

### Enumeration Cases
- [OS_UNFAIR_RECURSIVE_LOCK_FLAG_ADAPTIVE_SPIN](./os_unfair_recursive_lock_flags_t/os_unfair_recursive_lock_flag_adaptive_spin.md)
- [OS_UNFAIR_RECURSIVE_LOCK_FLAG_NONE](./os_unfair_recursive_lock_flags_t/os_unfair_recursive_lock_flag_none.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_unfair_recursive_lock_flags_t)*