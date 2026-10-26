# kIOPMAssertionTypeNoIdleSleep

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Pass as the AssertionType argument to [`IOPMAssertionCreate`](./api-1557118-iopmassertioncreate.md). The system will not idle sleep when enabled (display may sleep). Note that the system may sleep for other reasons.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
#define kIOPMAssertionTypeNoIdleSleep
```

#### Discussion

When asserted and set to level [`kIOPMAssertionLevelOn`](./api-1557096-assertion/kiopmassertionlevelon.md), the system will prefer to enter the Dark Wake state, or remain in Dark Wake if already there, rather than go to sleep.

Assertions are just suggestions to the OS, and the OS can only honor them to the best of its ability. In the case of low power or a thermal emergency, the system may sleep anyway despite the assertion.

An assertion must publish the AssertionType in its assertion properties dictionary. The AssertionType should be a key in the properties dictionary, with a value of a CFNumber containing the kCFNumberIntegerType value [`kIOPMAssertionLevelOff`](./api-1557096-assertion/kiopmassertionleveloff.md) or [`kIOPMAssertionLevelOn`](./api-1557096-assertion/kiopmassertionlevelon.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertiontypenoidlesleep)*