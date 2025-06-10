# handleOpen

**Framework**: Kernel  
**Kind**: instm

Overrideable method to control the open / close behaviour of an IOService.

## Declaration

```swift
virtual bool handleOpen(
 IOService *forClient, 
 IOOptionBits options, 
 void *arg );
```

#### Return_value

Return true if the open was successful, false otherwise.

#### Overview

See IOService for discussion.

## Parameters

- `forClient`: Designates the client of the provider requesting the open.
- `options`: Options for the open, may be interpreted by the implementor of handleOpen.

## See Also

- [attach](iofirewiresbp2lun/1813520-attach.md)
  Attaches an IOService client to a provider in the registry.
- [createLogin](iofirewiresbp2lun/1813525-createlogin.md)
  Creates a new IOFireWireSBP2Login object.
- [createManagementORB](iofirewiresbp2lun/1813535-createmanagementorb.md)
  Creates a new IOFireWireSBP2ManagementORB object.
- [getDiagnostics](iofirewiresbp2lun/1813549-getdiagnostics.md)
  Debug-only method.
- [getFireWireUnit](iofirewiresbp2lun/1813559-getfirewireunit.md)
  Returns an IOFireWireUnit object.
- [getLUNumber](iofirewiresbp2lun/1813568-getlunumber.md)
  Returns the LUNs number.
- [handleClose](iofirewiresbp2lun/1813576-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](iofirewiresbp2lun/1813597-matchpropertytable.md)
  Implements SBP2 specific matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2lun/1813589-handleopen)*