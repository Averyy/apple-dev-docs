# makeP2PInputConnection

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Increments the point-to-point connection count of a unit input plug.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*makeP2PInputConnection)(void *self, UInt32 inputPlug, UInt32 chan);
```

## Discussion

This function is only available if the interface version is > 3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibunitinterface/1508816-makep2pinputconnection)*