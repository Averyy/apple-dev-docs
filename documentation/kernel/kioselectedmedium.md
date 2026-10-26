# kIOSelectedMedium

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of IONetworkController objects.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIOSelectedMedium
```

#### Discussion

The kIOSelectedMedium property is a property of IONetworkController objects. It has an OSSymbol value that describes the name of the current selected medium. This name can be used as a key into the medium dictionary to gather additional information about the selected medium.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kioselectedmedium)*