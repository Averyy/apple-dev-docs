# createMgmtORB

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Creates a new IOFireWireSBP2LibMgmntORBInterface object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IUnknownVTbl **(*createMgmtORB)(void *self, REFIID iid);
```

## Return Value

Returns a pointer to a new IOFireWireSBP2Login.

## Discussion

Creates a new IOFireWireSBP2LibMgmtORBInterface object. Management objects let you execute commands like QueryLogins, LogicalUnitReset, and AbortTask. These commands are configured after they are created here. When they are done executing (after a call to submit) the supplied completion routine will be called with the supplied refcon. Usually this refCon is the "this" pointer of completion method's object.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLUNInterface.
- `iid`: UUID for desired type of IOFireWireSBP2LibMgmtORBInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libluninterface/1590428-createmgmtorb)*