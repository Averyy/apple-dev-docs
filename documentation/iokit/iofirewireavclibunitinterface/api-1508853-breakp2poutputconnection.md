# breakP2POutputConnection

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Decrements the point-to-point connection count of a unit output plug.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*breakP2POutputConnection)(void *self, UInt32 outputPlug);
```

## Discussion

This function is only available if the interface version is > 3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibunitinterface/1508853-breakp2poutputconnection)*