# attach

**Framework**: Kernel  
**Kind**: instm

Attaches an IOService client to a provider in the registry.

## Declaration

```swift
virtual bool attach(
 IOService *provider );
```

#### Return_value

false if the provider is inactive or on a resource failure, otherwise true.

#### Overview

See IOService for discussion.

## Parameters

- `provider`: The IOService object which will serve as this objects provider.

## See Also

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
- [handleOpen](iofirewiresbp2lun/1813589-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](iofirewiresbp2lun/1813597-matchpropertytable.md)
  Implements SBP2 specific matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2lun/1813520-attach)*