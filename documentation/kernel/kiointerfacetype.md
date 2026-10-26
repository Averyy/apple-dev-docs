# kIOInterfaceType

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of IONetworkInterface objects.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIOInterfaceType
```

#### Discussion

The kIOInterfaceType property has an OSNumber value that specifies the type of network interface that this interface represents. The type constants are defined in bsd/net/if_types.h.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiointerfacetype)*