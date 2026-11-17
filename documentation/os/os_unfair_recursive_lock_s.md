# os_unfair_recursive_lock_s

**Framework**: os  
**Kind**: struct  
**Role**: Structure

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
struct os_unfair_recursive_lock_s;
```

## Overview

Low-level recursive lock that allows waiters to block efficiently on contention.

Must be initialized with OS_UNFAIR_RECURSIVE_LOCK_INIT.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_unfair_recursive_lock_s)*