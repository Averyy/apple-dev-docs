# attach

**Framework**: Kernel  
**Kind**: instm

Attaches an IOService client to a provider in the registry.

## Declaration

```cpp
virtual bool attach(
 IOService *provider );
```

#### Return Value

false if the provider is inactive or on a resource failure, otherwise true.

#### Overview

See IOService for discussion.

## Parameters

- `provider`: The IOService object which will serve as this objects provider.

## See Also

### Miscellaneous
- [createLogin](./api-1813525-createlogin.md)
  Creates a new IOFireWireSBP2Login object.
- [createManagementORB](./api-1813535-createmanagementorb.md)
  Creates a new IOFireWireSBP2ManagementORB object.
- [getDiagnostics](./api-1813549-getdiagnostics.md)
  Debug-only method.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2lun/1813520-attach)*