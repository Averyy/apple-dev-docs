# OS_UNFAIR_RECURSIVE_LOCK_FLAG_NONE

**Framework**: os  
**Kind**: case  
**Role**: Enumeration Case

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
OS_UNFAIR_RECURSIVE_LOCK_FLAG_NONE
```

## Discussion

This flag allows the caller of os_unfair_recursive_lock_lock_with_flags API to spin temporarily before blocking, particularly useful when the holder of the lock is on core. This should only be used for locks where the protected critical section is always extremely short. When reacquiring a lock already held by the calling thread, this flag does nothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_unfair_recursive_lock_flags_t/os_unfair_recursive_lock_flag_none)*