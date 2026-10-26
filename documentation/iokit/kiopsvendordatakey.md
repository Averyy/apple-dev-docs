# kIOPSVendorDataKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for arbitrary vendor data.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
#define kIOPSVendorDataKey
```

#### Discussion

- Apple-defined power sources are not required to publish this key.
- For power source creators: Providing this key is OPTIONAL.
- CFDictionary; contents determined by the power source software. macOS will not look at this data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopsvendordatakey)*