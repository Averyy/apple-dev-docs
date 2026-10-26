# IOPMAssertionCreateWithProperties

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Creates an IOPMAssertion with more flexibility than [`IOPMAssertionCreateWithDescription`](./api-1557078-iopmassertioncreatewithdescripti.md).

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```c
IOReturn IOPMAssertionCreateWithProperties(CFDictionaryRef AssertionProperties, IOPMAssertionID *AssertionID);
```

#### Discussion

Create a new PM assertion - the caller must specify the type of assertion, initial level, and its properties as [IOPMAssertionDictionaryKeys](./iopmlib_h/iopmassertiondictionarykeys.md) keys in the `AssertionProperties` dictionary. The following keys are recommend and/or required to be specified in the AssertionProperties dictionary argument.

- REQUIRED: `kIOPMAssertionTypeKey` define the assertion type.
- REQUIRED: `kIOPMAssertionValueKey` define an inital value.
- REQUIRED: `kIOPMAssertionNameKey` Caller must describe the name for the activity that requires the change in behavior provided by the assertion.
- OPTIONAL: `kIOPMAssertionDetailsKey` Caller may describe context-specific data about the assertion.
- OPTIONAL: `kIOPMAssertionHumanReadableReasonKey` Caller may describe the reason for creating the assertion in a localizable CFString. This should be a human readable phrase that describes the actions the calling process is taking while the assertion is held, like "Downloading TV episodes", or "Compiling Projects"
- OPTIONAL: `kIOPMAssertionLocalizationBundlePathKey` Caller may provide its bundle's path, where macOS can localize for GUI display the CFString specified by [`kIOPMAssertionHumanReadableReasonKey`](./kiopmassertionhumanreadablereasonkey.md).
- OPTIONAL: `kIOPMAssertionPlugInIDKey` if the caller is a plugin with a different identity than the process it's loaded in.
- OPTIONAL: `kIOPMAssertionFrameworkIDKey` if the caller is a framework acting on behalf of a process.
- OPTIONAL: The caller may specify a timeout.

## Parameters

- `AssertionProperties`: Dictionary providing the properties of the assertion that need to be created.
- `AssertionID`: (Output) On successful return, contains a unique reference to a PM assertion.

## See Also

### Assertions
- [IOPMAssertionCopyProperties](./api-1557066-iopmassertioncopyproperties.md)
  Copies details about an `IOPMAssertion`
- [IOPMAssertionCreate](./api-1557118-iopmassertioncreate.md)
  Dynamically requests a system behavior from the power management system.
- [IOPMAssertionCreateWithDescription](./api-1557078-iopmassertioncreatewithdescripti.md)
- [IOPMAssertionCreateWithName](./api-1557134-iopmassertioncreatewithname.md)
  Dynamically requests a system behavior from the power management system.
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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557082-iopmassertioncreatewithpropertie)*