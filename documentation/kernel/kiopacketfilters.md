# kIOPacketFilters

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of IONetworkController objects.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIOPacketFilters
```

## Discussion

The kIOPacketFilters property is a property of IONetworkController objects. It has an OSDictionary value that describes the entire set of packet filters supported by the controller. Each entry in the dictionary is a key/value pair consisting of the filter group name, and an OSNumber describing the set of supported filters for that group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopacketfilters)*