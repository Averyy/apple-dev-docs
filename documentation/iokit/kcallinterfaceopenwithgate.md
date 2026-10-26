# kCallInterfaceOpenWithGate

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
#define kCallInterfaceOpenWithGate
```

#### Discussion

If the USB Device has this property, drivers for any of its interfaces will have their handleOpen method called while holding the workloop gate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kcallinterfaceopenwithgate)*