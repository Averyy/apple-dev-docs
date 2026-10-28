# kIORequiredPacketFilters

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

A property of IOEthernetInterface objects.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
#define kIORequiredPacketFilters
```

## Discussion

The kIORequiredPacketFilters property has an OSDictionary value that describes the current set of required packet filters. Each entry in the dictionary is a key/value pair consisting of the filter group name, and an OSNumber describing the set of required filters for that group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiorequiredpacketfilters)*