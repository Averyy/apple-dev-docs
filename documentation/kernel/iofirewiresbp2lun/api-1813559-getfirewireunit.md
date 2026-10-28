# getFireWireUnit

**Framework**: Kernel  
**Kind**: instm

Returns an IOFireWireUnit object.

## Declaration

```cpp
virtual IOFireWireUnit * getFireWireUnit(
 void );
```

## Return Value

Returns a pointer to an IOFireWireUnit.

## Overview

An IOFireWireUnit is the provider of an IOFireWireSBP2Target. In order to use the base FireWire services you will need a reference to the unit. This method returns that reference.

## See Also

### Miscellaneous
- [attach](./api-1813520-attach.md)
  Attaches an IOService client to a provider in the registry.
- [createLogin](./api-1813525-createlogin.md)
  Creates a new IOFireWireSBP2Login object.
- [createManagementORB](./api-1813535-createmanagementorb.md)
  Creates a new IOFireWireSBP2ManagementORB object.
- [getDiagnostics](./api-1813549-getdiagnostics.md)
  Debug-only method.
- [getLUNumber](./api-1813568-getlunumber.md)
  Returns the LUNs number.
- [handleClose](./api-1813576-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](./api-1813589-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](./api-1813597-matchpropertytable.md)
  Implements SBP2 specific matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2lun/1813559-getfirewireunit)*