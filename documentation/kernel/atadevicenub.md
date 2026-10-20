# ATADeviceNub

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

ATADeviceNub is a concrete implementation of IOATADevice.

**Availability**:
- macOS 11.0+

## Declaration

```cpp
class ATADeviceNub : IOATADevice
```

#### Overview

clients of IOATA (disk drivers) should use the interface presented by IOATADevice. Concrete nubs are private to the IOATA family and specific subclasses of IOATADevice are instantiated by controller drivers to provide the abstract interface to clients.

## Topics

### Miscellaneous
- [allocCommand](./atadevicenub/api-1805563-alloccommand.md)
  create command objects for clients.
- [ataDeviceNub](./atadevicenub/api-1805565-atadevicenub.md)
  static creator function - used by IOATAControllers to create nubs.
- [attach](./atadevicenub/api-1805568-attach.md)
  override of IOService method.
- [executeCommand](./atadevicenub/api-1805572-executecommand.md)
  Submit IO requests
- [freeCommand](./atadevicenub/api-1805576-freecommand.md)
  Clients use this method to dispose of command objects.
- [getDeviceID](./atadevicenub/api-1805578-getdeviceid.md)
  get the unit id of this drive (0 or 1)
- [init](./atadevicenub/api-1805582-init.md)
  used after creating the nub.
- [MyATACallback](./atadevicenub/api-1805585-myatacallback.md)
  to be deprecated.
- [processCallback](./atadevicenub/api-1805590-processcallback.md)
  to be deprecated.
- [publishBusProperties](./atadevicenub/api-1805593-publishbusproperties.md)
  puts info about this device's bus capability in the device tree.
- [publishProperties](./atadevicenub/api-1805598-publishproperties.md)
  publish the nub's properties in the device tree.
- [publishVendorProperties](./atadevicenub/api-1805600-publishvendorproperties.md)
  will be deprecated.
- [swapBytes16](./atadevicenub/api-1805603-swapbytes16.md)
  to be deprecated.
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [reserved](./atadevicenub/reserved.md)
### Instance Methods
- [- allocCommand](./atadevicenub/api-1558312-alloccommand.md)
- [- attach](./atadevicenub/api-1558299-attach.md)
- [- executeCommand](./atadevicenub/api-1558313-executecommand.md)
- [- freeCommand](./atadevicenub/api-1558304-freecommand.md)
- [- getDeviceID](./atadevicenub/api-1558301-getdeviceid.md)
- [- getMetaClass](./atadevicenub/api-1558300-getmetaclass.md)
- [- init](./atadevicenub/api-1558310-init.md)
- [- processCallback](./atadevicenub/api-1558302-processcallback.md)
- [- publishBusProperties](./atadevicenub/api-1558303-publishbusproperties.md)
- [- publishProperties](./atadevicenub/api-1558308-publishproperties.md)
- [- publishVendorProperties](./atadevicenub/api-1558307-publishvendorproperties.md)
- [- swapBytes16](./atadevicenub/api-1558309-swapbytes16.md)
### Type Methods
- [+ MyATACallback](./atadevicenub/api-1558306-myatacallback.md)
- [+ ataDeviceNub](./atadevicenub/api-1558311-atadevicenub.md)

## Relationships

### Inherits From
- [IOATADevice](./ioatadevice.md)

## See Also

### Devices
- [IOATADevice](./ioatadevice.md)
  This object implements a relay to an ATA Bus where a drive is attached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/atadevicenub)*