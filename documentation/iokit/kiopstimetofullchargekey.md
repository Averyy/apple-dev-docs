# kIOPSTimeToFullChargeKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for the current power source's time remaining until empty.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
#define kIOPSTimeToFullChargeKey
```

#### Discussion

Only valid if the value of [`kIOPSIsChargingKey`](./kiopsischargingkey.md) is kCFBooleanTrue.

- Apple-defined power sources will publish this key.
- For power source creators: Providing this key is RECOMMENDED.
- Type CFNumber kCFNumberIntType (signed integer), units are minutes
- A value of -1 indicates "Still Calculating the Time", otherwise estimated minutes until fully charged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopstimetofullchargekey)*