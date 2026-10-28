# makeP2POutputConnection

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Increments the point-to-point connection count of a unit output plug.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*makeP2POutputConnection)(void *self, UInt32 outputPlug, UInt32 chan, IOFWSpeed speed);
```

## Discussion

This function is only available if the interface version is > 3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibunitinterface/1508818-makep2poutputconnection)*