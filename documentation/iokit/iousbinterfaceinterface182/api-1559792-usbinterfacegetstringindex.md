# USBInterfaceGetStringIndex

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the string index in the interface descriptor.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*USBInterfaceGetStringIndex)(void *self, UInt8 *si);
```

## Discussion

The interface does not have to be open to use this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface182/1559792-usbinterfacegetstringindex)*