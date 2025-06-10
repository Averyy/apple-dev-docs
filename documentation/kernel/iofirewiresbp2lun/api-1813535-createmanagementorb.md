# createManagementORB

**Framework**: Kernel  
**Kind**: instm

Creates a new IOFireWireSBP2ManagementORB object.

## Declaration

```swift
virtual IOFireWireSBP2ManagementORB * createManagementORB(
 void *refCon,
 FWSBP2ManagementCallbackcompletion );
```

#### Return_value

Returns a pointer to a new IOFireWireSBP2Login.

#### Overview

Creates a new IOFireWireSBP2ManagementORB object. Management objects let you execute commands like QueryLogins, LogicalUnitReset, and AbortTask. These commands are configured after they are created here. When they are done executing (after a call to submit) the supplied completion routine will be called with the supplied refcon. Usually this refCon is the "this" pointer of completion method's object.

## Parameters

- `refCon`: The refcon passed to the completion routine.
- `completion`: The completion routine. Called when the ORB finishes execution.

## See Also

- [attach](iofirewiresbp2lun/1813520-attach.md)
  Attaches an IOService client to a provider in the registry.
- [createLogin](iofirewiresbp2lun/1813525-createlogin.md)
  Creates a new IOFireWireSBP2Login object.
- [getDiagnostics](iofirewiresbp2lun/1813549-getdiagnostics.md)
  Debug-only method.
- [getFireWireUnit](iofirewiresbp2lun/1813559-getfirewireunit.md)
  Returns an IOFireWireUnit object.
- [getLUNumber](iofirewiresbp2lun/1813568-getlunumber.md)
  Returns the LUNs number.
- [handleClose](iofirewiresbp2lun/1813576-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](iofirewiresbp2lun/1813589-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](iofirewiresbp2lun/1813597-matchpropertytable.md)
  Implements SBP2 specific matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2lun/1813535-createmanagementorb)*