# wBytesPerInterval

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

For SuperSpeed interrupt and isoc endpoints, this is the wBytesPerInterval from the SuperSpeed Endpoint Companion Descriptor. For High Speed High Bandwidth isoc endpoints, this will be equal to wMaxPacketSize * (bMult+1).

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.8+

## Declaration

```c
UInt16 wBytesPerInterval;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbendpointproperties/1426234-wbytesperinterval)*