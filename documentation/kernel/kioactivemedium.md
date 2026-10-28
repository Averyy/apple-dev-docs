# kIOActiveMedium

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of IONetworkController objects.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIOActiveMedium
```

## Discussion

The kIOActiveMedium property is a property of IONetworkController objects. It has an OSSymbol value that describes the name of the active medium. This is the name of the medium where an active link has been established. This name can be used as a key into the medium dictionary to gather additional information about the active medium.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kioactivemedium)*