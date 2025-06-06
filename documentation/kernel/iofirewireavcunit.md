# IOFireWireAVCUnit

**Framework**: Kernel  
**Kind**: cl

nub for AVC devices

**Availability**:
- macOS 10.2+

## Declaration

```swift
class IOFireWireAVCUnit : IOFireWireAVCNub
```

#### Overview

## Topics

### Miscellaneous
- [AVCCommand](iofirewireavcunit/1813829-avccommand.md)
  Sends an AVC command to the device and stores the response.
- [AVCCommandInGeneration](iofirewireavcunit/1813833-avccommandingeneration.md)
  Sends an AVC command to the device and stores the response. The command must complete in the specified FireWire bus generation otherwise kIOFireWireBusReset is returned.
- [handleClose](iofirewireavcunit/1813838-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](iofirewireavcunit/1813842-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](iofirewireavcunit/1813847-matchpropertytable.md)
  Matching language support Match on the following properties of the unit: Vendor_ID GUID Unit_Type and available sub-units, match if the device has at least the requested number of a sub-unit type: AVCSubUnit_0 -> AVCSubUnit_1f
- [updateAVCCommandTimeout](iofirewireavcunit/1813851-updateavccommandtimeout.md)
  By default, AVCCommands timeout 10 seconds after receiving an Interim response. This function resets the timeout of the current command to 10 seconds from the current time. Call this repeatedly for AVC commands that take a very long time to execute to prevent premature timeout.
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [fIOFireWireAVCUnitExpansion](iofirewireavcunit/fiofirewireavcunitexpansion.md)
### Instance Methods
- [- AVCCommand](iofirewireavcunit/1553133-avccommand.md)
- [- AVCCommandInGeneration](iofirewireavcunit/1553141-avccommandingeneration.md)
- [- available](iofirewireavcunit/1553138-available.md)
- [- free](iofirewireavcunit/1553124-free.md)
- [- getMetaClass](iofirewireavcunit/1553113-getmetaclass.md)
- [- handleClose](iofirewireavcunit/1553107-handleclose.md)
- [- handleOpen](iofirewireavcunit/1553139-handleopen.md)
- [- indexOfAVCAsynchronousCommandObject](iofirewireavcunit/1553148-indexofavcasynchronouscommandobj.md)
- [- lockAVCAsynchronousCommandLock](iofirewireavcunit/1553105-lockavcasynchronouscommandlock.md)
- [- matchPropertyTable](iofirewireavcunit/1553150-matchpropertytable.md)
- [- message](iofirewireavcunit/1553106-message.md)
- [- removeAVCAsynchronousCommandObjectAtIndex](iofirewireavcunit/1553127-removeavcasynchronouscommandobje.md)
- [- setProperties](iofirewireavcunit/1553140-setproperties.md)
- [- start](iofirewireavcunit/1553130-start.md)
- [- unlockAVCAsynchronousCommandLock](iofirewireavcunit/1553134-unlockavcasynchronouscommandlock.md)
- [- updateAVCCommandTimeout](iofirewireavcunit/1553149-updateavccommandtimeout.md)
- [- updateSubUnits](iofirewireavcunit/1553151-updatesubunits.md)
### Type Methods
- [+ AVCAsynchDelayDone](iofirewireavcunit/1553108-avcasynchdelaydone.md)
- [+ AVCAsynchRequestWriteDone](iofirewireavcunit/1553117-avcasynchrequestwritedone.md)
- [+ AVCResponse](iofirewireavcunit/1553132-avcresponse.md)
- [+ rescanSubUnits](iofirewireavcunit/1553125-rescansubunits.md)

## Relationships

### Inherits From
- [IOFireWireAVCNub](iofirewireavcnub.md)

## See Also

- [IOFireWireLocalNode](iofirewirelocalnode.md)
- [IOFireWireSBP2LUN](iofirewiresbp2lun.md)
  Provider for most drivers.
- [IOFireWireAVCSubUnit](iofirewireavcsubunit.md)
  nub for sub unit of AVC devices. Just for matching, calls the AVC unit for all functions.
- [IOFireWireAVCNub](iofirewireavcnub.md)
  nub for AVC devices
- [IOFireWireUnit](iofirewireunit.md)
- [IOFireWireNub](iofirewirenub.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavcunit)*