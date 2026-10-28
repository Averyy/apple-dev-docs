# kIOInterfaceState

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of IONetworkInterface objects.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIOInterfaceState
```

## Discussion

The kIOInterfaceState property has an OSNumber value that describes the current state of the interface object. This property is not exported to BSD via the ifnet structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiointerfacestate)*