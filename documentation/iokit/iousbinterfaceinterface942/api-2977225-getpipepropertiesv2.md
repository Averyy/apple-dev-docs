# GetPipePropertiesV2

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.14+

## Declaration

```c
IOReturn (*GetPipePropertiesV2)(void *self, UInt8 pipeRef, UInt8 *direction, UInt8 *number, UInt8 *transferType, UInt16 *maxPacketSize, UInt8 *interval, UInt8 *maxBurst, UInt8 *mult, UInt16 *bytesPerInterval);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface942/2977225-getpipepropertiesv2)*