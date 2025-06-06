# IOLockGroup

**Framework**: Kernel  
**Kind**: data

**Availability**:
- macOS 10.4+

## Declaration

```swift
lck_grp_t *IOLockGroup;
```

#### Discussion

Global lock group used by all IOKit locks. To simplify kext debugging and lock-heat analysis, consider using lck_* locks with a per-driver lock group, as defined in kern/locks.h.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iolockgroup)*