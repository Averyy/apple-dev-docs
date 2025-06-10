# setPSProperty

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
void setPSProperty(
 const OSSymbol *,
 OSObject *);
```

#### Overview

All of these methods funnel through the generic accessor method setPSProperty. Caller can pass in any arbitrary OSSymbol key, and that value will be stored in the PM settings dictionary, and relayed onto the IORegistry at update time.

## See Also

- [powerSource](iopmpowersource/1809904-powersource.md)
  Creates a new IOPMPowerSource nub. Must be attached to IORegistry, and registered by provider.
- [updateStatus](iopmpowersource/1809926-updatestatus.md)
  Must be called by physical battery controller when battery state has changed significantly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopmpowersource/1809917-setpsproperty)*