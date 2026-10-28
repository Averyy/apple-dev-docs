# getUnitID

**Framework**: Kernel  
**Kind**: instm

Determine whether this device is number 0 or 1 (ie, primary/secondary)

## Declaration

```cpp
virtual ataUnitID getUnitID(
 void );
```

## Return Value

ataUnitID - 0 or 1.

## See Also

### Miscellaneous
- [allocCommand](./api-1813891-alloccommand.md)
  create IOATACommands. Device drivers should allocate command objects only through this method.
- [executeCommand](./api-1813893-executecommand.md)
  Submit IO requests
- [freeCommand](./api-1813895-freecommand.md)
  release a command object that is no longer needed. Do not free an object in use and do not release the object anymore times than you have retained it.
- [getDeviceType](./api-1813897-getdevicetype.md)
  Find out what kind of device this nub is (ata or atapi)
- [matchLocation](./api-1813901-matchlocation.md)
  matching stuff for IOBSDInit and so on.
- [matchPropertyTable(OSDictionary *)](./api-1813903-matchpropertytable.md)
  matching stuff for IOBSDInit and so on.
- [matchPropertyTable(OSDictionary *, SInt32 *)](./api-1813905-matchpropertytable.md)
  matching stuff for IOBSDInit and so on.
- [notifyEvent](./api-1813907-notifyevent.md)
  called by controllers when they need to send a message to client (disk) drivers.
- [provideBusInfo](./api-1813909-providebusinfo.md)
  Find out the bus capability so the client can choose the features to set and commands to run.
- [provideConfig](./api-1813911-provideconfig.md)
  Find out what speed the bus has configured for this unit.
- [selectConfig](./api-1813913-selectconfig.md)
  Tell the bus what speed to use for your device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatadevice/1813899-getunitid)*