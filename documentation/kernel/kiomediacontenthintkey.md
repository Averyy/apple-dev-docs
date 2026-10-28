# kIOMediaContentHintKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of IOMedia objects.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIOMediaContentHintKey
```

## Discussion

The kIOMediaContentHintKey property has an OSString value and contains a hint of the media's contents. The hint is set at the time of the object's creation, should the creator have a clue as to what it may contain. The hint string does not change for the lifetime of the object and is formed in the likeness of Apple's "Apple_HFS" strings or in the likeness of a UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiomediacontenthintkey)*