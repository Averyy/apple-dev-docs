# bMult

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

For SuperSpeed isoc endpoints, this is the mult value from the SuperSpeed Endpoint Companion Descriptor. For High Speed isoc and interrupt endpoints, this is bits 11 and 12 of the Standard Endpoint Descriptor, which represents a similar value.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.8+

## Declaration

```c
UInt8 bMult;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbendpointproperties/1426019-bmult)*