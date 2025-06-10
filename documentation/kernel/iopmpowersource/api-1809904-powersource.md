# powerSource

**Framework**: Kernel  
**Kind**: instm

Creates a new IOPMPowerSource nub. Must be attached to IORegistry, and registered by provider.

## Declaration

```swift
static IOPMPowerSource *powerSource(
 void);
```

## See Also

- [setPSProperty](iopmpowersource/1809917-setpsproperty.md)
- [updateStatus](iopmpowersource/1809926-updatestatus.md)
  Must be called by physical battery controller when battery state has changed significantly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopmpowersource/1809904-powersource)*