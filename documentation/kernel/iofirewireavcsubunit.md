# IOFireWireAVCSubUnit

**Framework**: Kernel  
**Kind**: cl

nub for sub unit of AVC devices. Just for matching, calls the AVC unit for all functions.

**Availability**:
- macOS 10.2+

## Declaration

```swift
class IOFireWireAVCSubUnit : IOFireWireAVCNub
```

#### Overview

## Topics

### Miscellaneous
- [AVCCommand](iofirewireavcsubunit/1810566-avccommand.md)
  Sends an AVC command to the device and stores the response.
- [AVCCommandInGeneration](iofirewireavcsubunit/1810598-avccommandingeneration.md)
  Sends an AVC command to the device and stores the response. The command must complete in the specified FireWire bus generation otherwise kIOFireWireBusReset is returned.
- [handleClose](iofirewireavcsubunit/1810634-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](iofirewireavcsubunit/1810680-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](iofirewireavcsubunit/1810716-matchpropertytable.md)
  Matching language support Match on the following properties of the sub unit: Vendor_ID GUID SubUnit_Type
- [updateAVCCommandTimeout](iofirewireavcsubunit/1810751-updateavccommandtimeout.md)
  By default, AVCCommands timeout 10 seconds after receiving an Interim response. This function resets the timeout of the current command to 10 seconds from the current time. Call this repeatedly for AVC commands that take a very long time to execute to prevent premature timeout.
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](iofirewireavcsubunit/reserved.md)
### Instance Methods
- [- AVCCommand](iofirewireavcsubunit/1553143-avccommand.md)
- [- AVCCommandInGeneration](iofirewireavcsubunit/1553109-avccommandingeneration.md)
- [- getMetaClass](iofirewireavcsubunit/1553104-getmetaclass.md)
- [- handleClose](iofirewireavcsubunit/1553122-handleclose.md)
- [- handleOpen](iofirewireavcsubunit/1553112-handleopen.md)
- [- init](iofirewireavcsubunit/1553123-init.md)
- [- matchPropertyTable](iofirewireavcsubunit/1553136-matchpropertytable.md)
- [- message](iofirewireavcsubunit/1553116-message.md)
- [- updateAVCCommandTimeout](iofirewireavcsubunit/1553142-updateavccommandtimeout.md)

## Relationships

### Inherits From
- [IOFireWireAVCNub](iofirewireavcnub.md)

## See Also

- [IOFireWireLocalNode](iofirewirelocalnode.md)
- [IOFireWireSBP2LUN](iofirewiresbp2lun.md)
  Provider for most drivers.
- [IOFireWireAVCUnit](iofirewireavcunit.md)
  nub for AVC devices
- [IOFireWireAVCNub](iofirewireavcnub.md)
  nub for AVC devices
- [IOFireWireUnit](iofirewireunit.md)
- [IOFireWireNub](iofirewirenub.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavcsubunit)*