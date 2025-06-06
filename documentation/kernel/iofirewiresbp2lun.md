# IOFireWireSBP2LUN

**Framework**: Kernel  
**Kind**: cl

Provider for most drivers.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOFireWireSBP2LUN : IOService
```

#### Overview

IOFireWireSBP2LUN objects are created by IOFireWireSBP2Target objects. Each target may have zero or more IOFireWireSBP2LUN children. The LUN object serves as the matching nub for most drivers and therefore will be the provider for most drivers. It supplies the methods that control the operation of the LUN as a whole. Methods that control the behavior and execution of an SBP2 login session are supplied in a separate IOFireWireSBP2Login object. The LUN can be used to create one of these login objects. The LUN can also create IOFireWireSBP2ManagementORBs for configuring and appending non-login related management functions. Login related management functions (ie. Login, Logout, Reconnect) are supplied by the IOFireWireSBP2Login. Finally the LUN can supply a reference to the IOFireWireUnit. This can be useful if a driver wishes to access the standard FireWire APIs.

## Topics

### Miscellaneous
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
- [matchPropertyTable](iofirewiresbp2lun/1813597-matchpropertytable.md)
  Implements SBP2 specific matching.
### Instance Methods
- [- attach](iofirewiresbp2lun/1551896-attach.md)
- [- clearAllTasksInSet](iofirewiresbp2lun/1551890-clearalltasksinset.md)
- [- createLogin](iofirewiresbp2lun/1551889-createlogin.md)
- [- createLoginAction](iofirewiresbp2lun/1551899-createloginaction.md)
- [- createManagementORB](iofirewiresbp2lun/1551910-createmanagementorb.md)
- [- createManagementORBAction](iofirewiresbp2lun/1551914-createmanagementorbaction.md)
- [- executeFlushAllMgmtORBs](iofirewiresbp2lun/1551885-executeflushallmgmtorbs.md)
- [- finalize](iofirewiresbp2lun/1551883-finalize.md)
- [- flushAllManagementORBs](iofirewiresbp2lun/1551908-flushallmanagementorbs.md)
- [- free](iofirewiresbp2lun/1551907-free.md)
- [- getDiagnostics](iofirewiresbp2lun/1551884-getdiagnostics.md)
- [- getFireWireUnit](iofirewiresbp2lun/1551894-getfirewireunit.md)
- [- getLUNumber](iofirewiresbp2lun/1551904-getlunumber.md)
- [- getMetaClass](iofirewiresbp2lun/1551902-getmetaclass.md)
- [- getTarget](iofirewiresbp2lun/1551909-gettarget.md)
- [- handleClose](iofirewiresbp2lun/1551905-handleclose.md)
- [- handleOpen](iofirewiresbp2lun/1551901-handleopen.md)
- [- initLoginWithLUN](iofirewiresbp2lun/1551895-initloginwithlun.md)
- [- initMgmtORBWithLUN](iofirewiresbp2lun/1551903-initmgmtorbwithlun.md)
- [- matchPropertyTable](iofirewiresbp2lun/1551888-matchpropertytable.md)
- [- message](iofirewiresbp2lun/1551911-message.md)
- [- removeLogin](iofirewiresbp2lun/1551913-removelogin.md)
- [- removeLoginAction](iofirewiresbp2lun/1551892-removeloginaction.md)
- [- removeManagementORB](iofirewiresbp2lun/1551891-removemanagementorb.md)
- [- removeManagementORBAction](iofirewiresbp2lun/1551900-removemanagementorbaction.md)
- [- resumeNotify](iofirewiresbp2lun/1551915-resumenotify.md)
- [- suspendedNotify](iofirewiresbp2lun/1551906-suspendednotify.md)
- [- terminateNotify](iofirewiresbp2lun/1551912-terminatenotify.md)
### Type Methods
- [+ staticCreateLogin](iofirewiresbp2lun/1551887-staticcreatelogin.md)
- [+ staticCreateManagementORBAction](iofirewiresbp2lun/1551916-staticcreatemanagementorbaction.md)
- [+ staticExecuteFlushAllMgmtORBs](iofirewiresbp2lun/1551893-staticexecuteflushallmgmtorbs.md)
- [+ staticRemoveLoginAction](iofirewiresbp2lun/1551886-staticremoveloginaction.md)
- [+ staticRemoveManagementORBAction](iofirewiresbp2lun/1551897-staticremovemanagementorbaction.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOFireWireLocalNode](iofirewirelocalnode.md)
- [IOFireWireAVCSubUnit](iofirewireavcsubunit.md)
  nub for sub unit of AVC devices. Just for matching, calls the AVC unit for all functions.
- [IOFireWireAVCUnit](iofirewireavcunit.md)
  nub for AVC devices
- [IOFireWireAVCNub](iofirewireavcnub.md)
  nub for AVC devices
- [IOFireWireUnit](iofirewireunit.md)
- [IOFireWireNub](iofirewirenub.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2lun)*