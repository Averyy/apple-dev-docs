# IOPMAssertionCreateWithDescription

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```c
IOReturn IOPMAssertionCreateWithDescription(CFStringRef AssertionType, CFStringRef Name, CFStringRef Details, CFStringRef HumanReadableReason, CFStringRef LocalizationBundlePath, CFTimeInterval Timeout, CFStringRef TimeoutAction, IOPMAssertionID *AssertionID);
```

#### Return Value

kIOReturnSuccess, or another IOKit return code on error.

#### Discussion

Creates an IOPMAssertion. This is the preferred API to call to create an assertion. It allows the caller to specify the Name, Details, and HumanReadableReason at creation time. There are other keys that can further describe an assertion, but most developers don't need to use them. Use IOPMAssertionSetProperties or [`IOPMAssertionCreateWithProperties`](./api-1557082-iopmassertioncreatewithpropertie.md) if you need to specify properties that aren't available here.

## Parameters

- `AssertionType`: An assertion type constant. Caller must specify this argument.
- `Name`: A CFString value to correspond to key [`kIOPMAssertionNameKey`](./kiopmassertionnamekey.md). Caller must specify this argument.
- `Details`: A CFString value to correspond to key [`kIOPMAssertionDetailsKey`](./kiopmassertiondetailskey.md). Caller my pass NULL, but it helps power users and administrators identify the reasons for this assertion.
- `HumanReadableReason`: A CFString value to correspond to key [`kIOPMAssertionHumanReadableReasonKey`](./kiopmassertionhumanreadablereasonkey.md). Caller may pass NULL, but if it's specified macOS may display it to users to describe the active assertions on their system.
- `LocalizationBundlePath`: A CFString value to correspond to key [`kIOPMAssertionLocalizationBundlePathKey`](./kiopmassertionlocalizationbundlepathkey.md). This bundle path should include a localization for the string `HumanReadableReason` Caller may pass NULL, but this argument is required if caller specifies `HumanReadableReason`
- `Timeout`: Specifies a timeout for this assertion. Pass 0 for no timeout.
- `TimeoutAction`: Specifies a timeout action. Caller my pass NULL. If a timeout is specified but a TimeoutAction is not, the default timeout action is `kIOPMAssertionTimeoutActionTurnOff`
- `AssertionID`: (Output) On successful return, contains a unique reference to a PM assertion.

## See Also

### Assertions
- [IOPMAssertionCopyProperties](./api-1557066-iopmassertioncopyproperties.md)
  Copies details about an `IOPMAssertion`
- [IOPMAssertionCreate](./api-1557118-iopmassertioncreate.md)
  Dynamically requests a system behavior from the power management system.
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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557078-iopmassertioncreatewithdescripti)*