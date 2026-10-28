# kIOPMAssertionTimeoutActionTurnOff

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

A potential value for [`kIOPMAssertionTimeoutActionKey`](./kiopmassertiontimeoutactionkey.md)

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPMAssertionTimeoutActionTurnOff
```

## Discussion

When a timeout expires with this action, Power Management will log the timeout event, and will set the assertion's level to [`kIOPMAssertionLevelOff`](./api-1557096-assertion/kiopmassertionleveloff.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertiontimeoutactionturnoff)*