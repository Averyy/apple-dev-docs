# createLogin

**Framework**: Kernel  
**Kind**: instm

Creates a new IOFireWireSBP2Login object.

## Declaration

```swift
virtual IOFireWireSBP2Login *createLogin(
 void );
```

#### Return_value

Returns a pointer to a new IOFireWireSBP2Login.

#### Overview

Creates a new IOFireWireSBP2Login object for the LUN. Login objects supply most of the SBP2 APIs related to login maintenance and Normal Command ORB execution.

## See Also

- [attach](iofirewiresbp2lun/1813520-attach.md)
  Attaches an IOService client to a provider in the registry.
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
- [handleOpen](iofirewiresbp2lun/1813589-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](iofirewiresbp2lun/1813597-matchpropertytable.md)
  Implements SBP2 specific matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2lun/1813525-createlogin)*