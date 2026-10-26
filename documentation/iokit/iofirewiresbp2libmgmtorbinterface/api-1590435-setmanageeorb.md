# setManageeORB

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the command to be managed by the management ORB.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*setManageeORB)(void *self, void *command);
```

#### Return Value

Returns kIOReturnSuccess on a success.

#### Discussion

All management functions except kFWSBP2QueryLogins require a reference to an ORB of some sort. kFWSBP2AbortTask requires a reference to the ORB to be aborted. This method allows you to set the Normal Command ORB to be managed.

## Parameters

- `self`: Pointer to a IOFireWireSBP2LibMgmtORBInterface.
- `command`: a reference to an IOFireWireSBP2Login or an IOFireWireSBP2ORB.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libmgmtorbinterface/1590435-setmanageeorb)*