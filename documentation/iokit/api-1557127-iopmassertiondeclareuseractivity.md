# IOPMAssertionDeclareUserActivity

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Declares that the user is active on the system. This causes the display to power on and postpone display sleep up to the user's display sleep Energy Saver settings. If you prefer to hold the display awake for a longer period and you know how long you'd like to hold it, consider taking assertion [`kIOPMAssertionTypePreventUserIdleDisplaySleep`](./kiopmassertiontypepreventuseridledisplaysleep.md) using [`IOPMAssertionCreateWithDescription`](./api-1557078-iopmassertioncreatewithdescripti.md) API instead.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```c
IOReturn IOPMAssertionDeclareUserActivity(CFStringRef AssertionName, IOPMUserActiveType userType, IOPMAssertionID *AssertionID);
```

#### Return Value

Returns kIOReturnSuccess on success, any other return indicates PM could not successfully activate the specified assertion.

#### Discussion

No special privileges are necessary to make this call - any process may call this API. Caller must specify an AssertionName - NULL is not a valid input.

## Parameters

- `AssertionName`: A string that describes the name of the caller and the activity being handled by this assertion (e.g. "Mail Compacting Mailboxes"). Name may be no longer than 128 characters.
- `userType`: This parameter specifies if the active user is located locally in front of the system or connected to the system over the network. Various components of the system are maintained at different power levels depending on user location.
- `AssertionID`: On Success, unique id will be returned in this parameter. Caller may call this function again with the unique id retured previously to report continous user activity. The unique id returned by this function may change on each call depending on how frequently this function call is repeated and the current display sleep timer value. If you make this call more than once, track the returned value for assertionID, and pass it in as an argument on each call.

## See Also

### Assertions
- [IOPMAssertionCopyProperties](./api-1557066-iopmassertioncopyproperties.md)
  Copies details about an `IOPMAssertion`
- [IOPMAssertionCreate](./api-1557118-iopmassertioncreate.md)
  Dynamically requests a system behavior from the power management system.
- [IOPMAssertionCreateWithDescription](./api-1557078-iopmassertioncreatewithdescripti.md)
- [IOPMAssertionCreateWithName](./api-1557134-iopmassertioncreatewithname.md)
  Dynamically requests a system behavior from the power management system.
- [IOPMAssertionCreateWithProperties](./api-1557082-iopmassertioncreatewithpropertie.md)
  Creates an IOPMAssertion with more flexibility than [`IOPMAssertionCreateWithDescription`](./api-1557078-iopmassertioncreatewithdescripti.md).
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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557127-iopmassertiondeclareuseractivity)*