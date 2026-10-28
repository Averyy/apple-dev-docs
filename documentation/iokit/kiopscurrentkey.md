# kIOPSCurrentKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for the current power source's electrical current.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
#define kIOPSCurrentKey
```

## Discussion

- Apple-defined power sources will publish this key.
- For power source creators: Providing this key is RECOMMENDED.
- Type CFNumber kCFNumberIntType (signed integer) - units are mA


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopscurrentkey)*