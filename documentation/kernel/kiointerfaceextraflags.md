# kIOInterfaceExtraFlags

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of IONetworkInterface objects.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIOInterfaceExtraFlags
```

#### Discussion

The kIOInterfaceExtraFlags property has an OSNumber value that specifies the current value of the interface eflags. The eflag constants are defined in bsd/net/if.h.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiointerfaceextraflags)*