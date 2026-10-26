# kIONetworkData

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of IONetworkInterface objects.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIONetworkData
```

#### Discussion

The kIONetworkData property has an OSDictionary value and is a container for the set of IONetworkData objects managed by the interface. Each entry in the dictionary is a key/value pair consisting of the network data name, and an OSDictionary describing the contents of the network data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kionetworkdata)*