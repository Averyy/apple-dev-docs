# os_unfair_recursive_lock_t

**Framework**: os  
**Kind**: typealias  
**Role**: Type Alias

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
typedef struct os_unfair_recursive_lock_s * os_unfair_recursive_lock_t;
```

## Discussion

Low-level recursive lock that allows waiters to block efficiently on contention.

Must be initialized with OS_UNFAIR_RECURSIVE_LOCK_INIT.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_unfair_recursive_lock_t)*