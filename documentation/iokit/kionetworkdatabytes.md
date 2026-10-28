# kIONetworkDataBytes

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

A property of IONetworkData objects.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
#define kIONetworkDataBytes
```

## Discussion

The kIONetworkDataBytes property is an OSData that describes the data buffer of an IONetworkData object. This property is present only if kIONetworkDataAccessTypeSerialize access is supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kionetworkdatabytes)*