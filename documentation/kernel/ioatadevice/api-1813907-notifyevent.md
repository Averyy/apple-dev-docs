# notifyEvent

**Framework**: Kernel  
**Kind**: instm

called by controllers when they need to send a message to client (disk) drivers.

## Declaration

```swift
virtual void notifyEvent(
 UInt32 event );
```

## See Also

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
- [provideBusInfo](ioatadevice/1813909-providebusinfo.md)
  Find out the bus capability so the client can choose the features to set and commands to run.
- [provideConfig](ioatadevice/1813911-provideconfig.md)
  Find out what speed the bus has configured for this unit.
- [selectConfig](ioatadevice/1813913-selectconfig.md)
  Tell the bus what speed to use for your device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatadevice/1813907-notifyevent)*