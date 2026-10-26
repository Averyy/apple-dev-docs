# kIOMediaContentMaskKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of IOMedia clients.

**Availability**:
- macOS 10.0+

## Declaration

```c
#define kIOMediaContentMaskKey
```

#### Discussion

The kIOMediaContentMaskKey property has an OSString value and must exist in all IOMedia clients that drive new content (that is, produce new media objects). When the client matches against the provider media, the value of the client's kIOMediaContentMaskKey property is used to replace the provider's kIOMediaContentKey property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiomediacontentmaskkey)*