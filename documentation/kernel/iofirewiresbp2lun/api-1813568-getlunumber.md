# getLUNumber

**Framework**: Kernel  
**Kind**: instm

Returns the LUNs number.

## Declaration

```cpp
virtual UInt32 getLUNumber(
 void );
```

#### Return Value

Returns a UInt32 containing the Logical Unit Number.

#### Overview

Each LUN has a number to uniquely identify it on a device. This method returns this value in a UInt32.

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
- [getFireWireUnit](./api-1813559-getfirewireunit.md)
  Returns an IOFireWireUnit object.
- [handleClose](./api-1813576-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](./api-1813589-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](./api-1813597-matchpropertytable.md)
  Implements SBP2 specific matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2lun/1813568-getlunumber)*