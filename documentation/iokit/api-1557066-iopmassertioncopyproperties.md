# IOPMAssertionCopyProperties

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Copies details about an `IOPMAssertion`

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```c
CFDictionaryRef IOPMAssertionCopyProperties(IOPMAssertionID theAssertion);
```

#### Return Value

A dictionary describing the assertion with keys specified in See [IOPMAssertionDictionaryKeys](./iopmlib_h/iopmassertiondictionarykeys.md). It's the caller's responsibility to release this dictionary.

#### Discussion

Returns a dictionary describing an IOPMAssertion's specifications and current state.

## Parameters

- `theAssertion`: The assertion ID to copy info about.

## See Also

### Assertions
- [IOPMAssertionCreate](./api-1557118-iopmassertioncreate.md)
  Dynamically requests a system behavior from the power management system.
- [IOPMAssertionCreateWithDescription](./api-1557078-iopmassertioncreatewithdescripti.md)
- [IOPMAssertionCreateWithName](./api-1557134-iopmassertioncreatewithname.md)
  Dynamically requests a system behavior from the power management system.
- [IOPMAssertionCreateWithProperties](./api-1557082-iopmassertioncreatewithpropertie.md)
  Creates an IOPMAssertion with more flexibility than [`IOPMAssertionCreateWithDescription`](./api-1557078-iopmassertioncreatewithdescripti.md).
- [IOPMAssertionDeclareUserActivity](./api-1557127-iopmassertiondeclareuseractivity.md)
  Declares that the user is active on the system. This causes the display to power on and postpone display sleep up to the user's display sleep Energy Saver settings. If you prefer to hold the display awake for a longer period and you know how long you'd like to hold it, consider taking assertion [`kIOPMAssertionTypePreventUserIdleDisplaySleep`](./kiopmassertiontypepreventuseridledisplaysleep.md) using [`IOPMAssertionCreateWithDescription`](./api-1557078-iopmassertioncreatewithdescripti.md) API instead.
- [IOPMAssertionRelease](./api-1557090-iopmassertionrelease.md)
  Decrements the assertion's retain count.
- [IOPMAssertionRetain](./api-1557071-iopmassertionretain.md)
  Increments the assertion's retain count.
- [IOPMAssertionSetProperty](./api-1557107-iopmassertionsetproperty.md)
  Sets a property in the assertion.
- [IOPMCopyAssertionsByProcess](./api-1557130-iopmcopyassertionsbyprocess.md)
  Returns a dictionary listing all assertions, grouped by their owning process.
- [IOPMCopyAssertionsStatus](./api-1557072-iopmcopyassertionsstatus.md)
  Returns a list of available assertions and their system-wide levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557066-iopmassertioncopyproperties)*