# IOATADevice

**Framework**: Kernel  
**Kind**: cl

This object implements a relay to an ATA Bus where a drive is attached.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class IOATADevice : IOService
```

#### Overview

IOATADevice is the superclass which represents a particular device attached to a particular IOATAController (bus). IOATADevice is the provider for ATA mass-storage device drivers.IOATADevice is the factory for all IOATACommand objects and is responsible for creating and freeing IOATACommands. IOATAControllers will create an instance of IOATADevice for each device physically connected to the ata bus. IOATADevice is virtual and specific subclass should be implemented for particular types of IOATAController. In this manner, controller-specifc IOATACommands may be paired with the proper type of controller.

## Topics

### Miscellaneous
- [allocCommand](ioatadevice/1813891-alloccommand.md)
  create IOATACommands. Device drivers should allocate command objects only through this method.
- [executeCommand](ioatadevice/1813893-executecommand.md)
  Submit IO requests
- [freeCommand](ioatadevice/1813895-freecommand.md)
  release a command object that is no longer needed. Do not free an object in use and do not release the object anymore times than you have retained it.
- [getDeviceType](ioatadevice/1813897-getdevicetype.md)
  Find out what kind of device this nub is (ata or atapi)
- [getUnitID](ioatadevice/1813899-getunitid.md)
  Determine whether this device is number 0 or 1 (ie, primary/secondary)
- [matchLocation](ioatadevice/1813901-matchlocation.md)
  matching stuff for IOBSDInit and so on.
- [matchPropertyTable(OSDictionary *)](ioatadevice/1813903-matchpropertytable.md)
  matching stuff for IOBSDInit and so on.
- [matchPropertyTable(OSDictionary *, SInt32 *)](ioatadevice/1813905-matchpropertytable.md)
  matching stuff for IOBSDInit and so on.
- [notifyEvent](ioatadevice/1813907-notifyevent.md)
  called by controllers when they need to send a message to client (disk) drivers.
- [provideBusInfo](ioatadevice/1813909-providebusinfo.md)
  Find out the bus capability so the client can choose the features to set and commands to run.
- [provideConfig](ioatadevice/1813911-provideconfig.md)
  Find out what speed the bus has configured for this unit.
- [selectConfig](ioatadevice/1813913-selectconfig.md)
  Tell the bus what speed to use for your device.
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](ioatadevice/reserved.md)
### Instance Methods
- [- allocCommand](ioatadevice/1436258-alloccommand.md)
- [- executeCommand](ioatadevice/1436268-executecommand.md)
- [- freeCommand](ioatadevice/1436261-freecommand.md)
- [- getDeviceType](ioatadevice/1436262-getdevicetype.md)
- [- getMetaClass](ioatadevice/1436272-getmetaclass.md)
- [- getUnitID](ioatadevice/1436265-getunitid.md)
- [- matchLocation](ioatadevice/1436270-matchlocation.md)
- [- matchPropertyTable](ioatadevice/1436263-matchpropertytable.md)
- [- matchPropertyTable](ioatadevice/3516513-matchpropertytable.md)
- [- notifyEvent](ioatadevice/1436266-notifyevent.md)
- [- provideBusInfo](ioatadevice/1436267-providebusinfo.md)
- [- provideConfig](ioatadevice/1436271-provideconfig.md)
- [- selectConfig](ioatadevice/1436260-selectconfig.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [ATADeviceNub](atadevicenub.md)
  ATADeviceNub is a concrete implementation of IOATADevice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatadevice)*