# kIOActivePacketFilters

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

A property of IOEthernetInterface objects.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
#define kIOActivePacketFilters
```

## Discussion

The kIOActivePacketFilters property has an OSDictionary value that describes the current set of packet filters that have been successfully activated. Each entry in the dictionary is a key/value pair consisting of the filter group name, and an OSNumber describing the set of active filters for that group. Entries in this dictionary will mirror those in kIORequiredPacketFilters if the controller has reported success for all filter change requests from the IOEthernetInterface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kioactivepacketfilters)*