# kIOPSIsFinishingChargeKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key indicates whether the battery is finishing off its charge.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOPSIsFinishingChargeKey
```

#### Discussion

When this is true, the system UI should indicate that the battery is "Finishing Charge." Some batteries may continue charging after they report 100% capacity.

- Apple-defined battery power sources will publish this key.
- For power source creators: Providing this key is RECOMMENDED.
- Type CFBoolean - kCFBooleanTrue or kCFBooleanFalse


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopsisfinishingchargekey)*