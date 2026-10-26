# kIOPMAssertionTypePreventUserIdleSystemSleep

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Prevents the system from sleeping automatically due to a lack of user activity.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPMAssertionTypePreventUserIdleSystemSleep
```

#### Discussion

When asserted and set to level [`kIOPMAssertionLevelOn`](./api-1557096-assertion/kiopmassertionlevelon.md), will prevent the system from sleeping due to a period of idle user activity.

The display may dim and idle sleep while kIOPMAssertionTypePreventUserIdleSystemSleep is enabled, but the system may not idle sleep.

The system may still sleep for lid close, Apple menu, low battery, or other sleep reasons.

This assertion does not put the system into Dark Wake.

A caller publish the AssertionType in its assertion properties dictionary. The AssertionType should be a key in the properties dictionary, with a value of a CFNumber containing the kCFNumberIntegerType value [`kIOPMAssertionLevelOff`](./api-1557096-assertion/kiopmassertionleveloff.md) or [`kIOPMAssertionLevelOn`](./api-1557096-assertion/kiopmassertionlevelon.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertiontypepreventuseridlesystemsleep)*