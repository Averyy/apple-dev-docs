# kIOMediaContentKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of IOMedia objects.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIOMediaContentKey
```

#### Discussion

The kIOMediaContentKey property has an OSString value and contains a description of the media's contents. The description is the same as the hint at the time of the object's creation, but it is possible that the description has been overridden by a client (which has probed the media and identified the content correctly) of the media object. It is more accurate than the hint for this reason. The string is formed in the likeness of Apple's "Apple_HFS" strings or in the likeness of a UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiomediacontentkey)*