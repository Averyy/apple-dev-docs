# kIOMediumDictionary

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of IONetworkController objects.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIOMediumDictionary
```

#### Discussion

The kIOMediumDictionary property is a property of IONetworkController objects. It has an OSDictionary value that is a container for the collection of IONetworkMedium objects that represent the media types supported by the network controller. Each entry in the dictionary is a key/value pair consisting of the medium name, and a dictionary value that contains the properties for that medium entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiomediumdictionary)*