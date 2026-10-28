# kIOPMAssertionRetainCountKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

A potential value for [`kIOPMAssertionTimeoutActionKey`](./kiopmassertiontimeoutactionkey.md)

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPMAssertionRetainCountKey
```

## Discussion

kIOPMAssertionRetainCountKey reflects the CoreFoundation-style retain count on this assertion. Creating or retaining an assertion increments its retain count. Release an assertion decrements its retain count. When the retain count decrements to zero, the OS will destroy the object.

This key can be found in the dictionary returned from [`IOPMAssertionCopyProperties`](./api-1557066-iopmassertioncopyproperties.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertionretaincountkey)*