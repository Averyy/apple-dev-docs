# GetEndpointProperties

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.7+

## Declaration

```c
IOReturn (*GetEndpointProperties)(void *self, UInt8 alternateSetting, UInt8 endpointNumber, UInt8 direction, UInt8 *transferType, UInt16 *maxPacketSize, UInt8 *interval);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface500/1559127-getendpointproperties)*