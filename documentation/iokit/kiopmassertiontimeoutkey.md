# kIOPMAssertionTimeoutKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

kIOPMAssertionTimeoutKey specifies an outer bound, in seconds, that this assertion should be asserted.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPMAssertionTimeoutKey
```

## Discussion

If your application hangs, or is unable to complete its assertion task in a reasonable amount of time, specifying a timeout allows PM to disable your assertion so the system can resume normal activity. Once a timeout with the [`kIOPMAssertionTimeoutActionTurnOff`](./kiopmassertiontimeoutactionturnoff.md) assertion fires, the level will be set to [`kIOPMAssertionTimeoutActionTurnOff`](./kiopmassertiontimeoutactionturnoff.md). The assertion may be re-armed by calling IOPMAssertionSetLevel.

This key may be specified in the dictionary passed to [`IOPMAssertionCreateWithProperties`](./api-1557082-iopmassertioncreatewithpropertie.md).

This key may be present in the dictionary returned from [`IOPMAssertionCopyProperties`](./api-1557066-iopmassertioncopyproperties.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertiontimeoutkey)*