# matchPropertyTable

**Framework**: Kernel  
**Kind**: instm

Implements SBP2 specific matching.

## Declaration

```swift
virtual bool matchPropertyTable(
 OSDictionary *table);
```

#### Return_value

Returns false if the family considers the matching dictionary does not match in properties it understands, true otherwise.

#### Overview

See IOService for discussion.

## Parameters

- `table`: The dictionary of properties to be matched against.

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
- [handleOpen](iofirewiresbp2lun/1813589-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2lun/1813597-matchpropertytable)*