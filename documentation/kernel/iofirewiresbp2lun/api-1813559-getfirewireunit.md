# getFireWireUnit

**Framework**: Kernel  
**Kind**: instm

Returns an IOFireWireUnit object.

## Declaration

```swift
virtual IOFireWireUnit * getFireWireUnit(
 void );
```

#### Return_value

Returns a pointer to an IOFireWireUnit.

#### Overview

An IOFireWireUnit is the provider of an IOFireWireSBP2Target. In order to use the base FireWire services you will need a reference to the unit. This method returns that reference.

## See Also

- [attach](iofirewiresbp2lun/1813520-attach.md)
  Attaches an IOService client to a provider in the registry.
- [createLogin](iofirewiresbp2lun/1813525-createlogin.md)
  Creates a new IOFireWireSBP2Login object.
- [createManagementORB](iofirewiresbp2lun/1813535-createmanagementorb.md)
  Creates a new IOFireWireSBP2ManagementORB object.
- [getDiagnostics](iofirewiresbp2lun/1813549-getdiagnostics.md)
  Debug-only method.
- [getLUNumber](iofirewiresbp2lun/1813568-getlunumber.md)
  Returns the LUNs number.
- [handleClose](iofirewiresbp2lun/1813576-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](iofirewiresbp2lun/1813589-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](iofirewiresbp2lun/1813597-matchpropertytable.md)
  Implements SBP2 specific matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2lun/1813559-getfirewireunit)*