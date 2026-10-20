# getDiagnostics

**Framework**: Kernel  
**Kind**: instm

Debug-only method.

## Declaration

```cpp
virtual OSObject * getDiagnostics(
 void );
```

#### Return Value

Returns a pointer to the diagnostics object (if any).

#### Overview

Returns a reference to the internal diagnostics object when the services are built in debug mode. Should be a no-op in release builds.

## See Also

### Miscellaneous
- [attach](./api-1813520-attach.md)
  Attaches an IOService client to a provider in the registry.
- [createLogin](./api-1813525-createlogin.md)
  Creates a new IOFireWireSBP2Login object.
- [createManagementORB](./api-1813535-createmanagementorb.md)
  Creates a new IOFireWireSBP2ManagementORB object.
- [getFireWireUnit](./api-1813559-getfirewireunit.md)
  Returns an IOFireWireUnit object.
- [getLUNumber](./api-1813568-getlunumber.md)
  Returns the LUNs number.
- [handleClose](./api-1813576-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](./api-1813589-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](./api-1813597-matchpropertytable.md)
  Implements SBP2 specific matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2lun/1813549-getdiagnostics)*