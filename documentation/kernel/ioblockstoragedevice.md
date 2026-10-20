# IOBlockStorageDevice

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

A generic block storage device abstraction.

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IOBlockStorageDevice : IOService
```

#### Overview

The IOBlockStorageDevice class exports the generic block storage protocol, independent of the physical connection protocol (e.g. SCSI, ATA, USB), forwarding all requests to its provider (the Transport Driver). Though the nub does no actual processing of requests, it is necessary in a C++ environment. The Transport Driver can be of any type, as long as it inherits from IOService. Because Transport Drivers needn't derive from a type known to IOBlockStorageDriver, it isn't possible for IOBlockStorageDriver to include the appropriate header file to allow direct communication with the Transport Driver. Thus we achieve polymorphism by having the Transport Driver instantiate a subclass of IOBlockStorageDevice. A typical implementation for a concrete subclass of IOBlockStorageDevice simply relays all methods to its provider (the Transport Driver), which implements the protocol- and device-specific behavior.

All pure-virtual functions must be implemented by the Transport Driver, which is responsible for instantiating the Nub.

## Topics

### Miscellaneous
- [doAsyncReadWrite](./ioblockstoragedevice/api-1811665-doasyncreadwrite.md)
  Start an asynchronous read or write operation.
- [doEjectMedia](./ioblockstoragedevice/api-1811672-doejectmedia.md)
  Eject the media.
- [doFormatMedia](./ioblockstoragedevice/api-1811680-doformatmedia.md)
  Format the media to the specified byte capacity.
- [doGetFormatCapacities](./ioblockstoragedevice/api-1811684-dogetformatcapacities.md)
  Return the allowable formatting byte capacities.
- [doSynchronizeCache](./ioblockstoragedevice/api-1811691-dosynchronizecache.md)
  Force data blocks in the hardware's buffer to be flushed to the media.
- [doUnmap](./ioblockstoragedevice/api-1811698-dounmap.md)
  Delete unused data blocks from the media.
- [getAdditionalDeviceInfoString](./ioblockstoragedevice/api-1811705-getadditionaldeviceinfostring.md)
  Return additional informational string for the device.
- [getProductString](./ioblockstoragedevice/api-1811712-getproductstring.md)
  Return Product Name string for the device.
- [getRevisionString](./ioblockstoragedevice/api-1811717-getrevisionstring.md)
  Return Product Revision string for the device.
- [getVendorString](./ioblockstoragedevice/api-1811724-getvendorstring.md)
  Return Vendor Name string for the device.
- [getWriteCacheState](./ioblockstoragedevice/api-1811731-getwritecachestate.md)
  Reports the current write cache state of the device.
- [init](./ioblockstoragedevice/api-1811746-init.md)
- [reportBlockSize](./ioblockstoragedevice/api-1811753-reportblocksize.md)
  Report the block size for the device, in bytes.
- [reportEjectability](./ioblockstoragedevice/api-1811761-reportejectability.md)
  Report if the media is ejectable under software control.
- [reportMaxValidBlock](./ioblockstoragedevice/api-1811771-reportmaxvalidblock.md)
  Report the highest valid block for the device.
- [reportMediaState](./ioblockstoragedevice/api-1811780-reportmediastate.md)
  Report the device's media state.
- [reportRemovability](./ioblockstoragedevice/api-1811787-reportremovability.md)
  Report whether the media is removable or not.
- [reportWriteProtection](./ioblockstoragedevice/api-1811796-reportwriteprotection.md)
  Report whether the media is write-protected or not.
- [requestIdle](./ioblockstoragedevice/api-1811804-requestidle.md)
  Request that the device enter an idle state.
- [setWriteCacheState](./ioblockstoragedevice/api-1811812-setwritecachestate.md)
  Sets the write cache state of the device.
### Instance Methods
- [- doAsyncReadWrite](./ioblockstoragedevice/api-1568473-doasyncreadwrite.md)
- [- doDiscard](./ioblockstoragedevice/api-1568461-dodiscard.md)
- [- doEjectMedia](./ioblockstoragedevice/api-1568469-doejectmedia.md)
- [- doFormatMedia](./ioblockstoragedevice/api-1568474-doformatmedia.md)
- [- doGetFormatCapacities](./ioblockstoragedevice/api-1568458-dogetformatcapacities.md)
- [- doGetProvisionStatus](./ioblockstoragedevice/api-1646351-dogetprovisionstatus.md)
- [- doLockUnlockMedia](./ioblockstoragedevice/api-1568449-dolockunlockmedia.md)
- [- doSetPriority](./ioblockstoragedevice/api-1568459-dosetpriority.md)
- [- doSynchronize](./ioblockstoragedevice/api-1568462-dosynchronize.md)
- [- doSynchronizeCache](./ioblockstoragedevice/api-1568444-dosynchronizecache.md)
- [- doUnmap](./ioblockstoragedevice/api-1568476-dounmap.md)
- [- getAdditionalDeviceInfoString](./ioblockstoragedevice/api-1568452-getadditionaldeviceinfostring.md)
- [- getMetaClass](./ioblockstoragedevice/api-1568460-getmetaclass.md)
- [- getProductString](./ioblockstoragedevice/api-1568467-getproductstring.md)
- [- getProperty](./ioblockstoragedevice/api-1568466-getproperty.md)
- [- getRevisionString](./ioblockstoragedevice/api-1568447-getrevisionstring.md)
- [- getVendorString](./ioblockstoragedevice/api-1568480-getvendorstring.md)
- [- getWriteCacheState](./ioblockstoragedevice/api-1568451-getwritecachestate.md)
- [- init](./ioblockstoragedevice/api-1568471-init.md)
- [- reportBlockSize](./ioblockstoragedevice/api-1568477-reportblocksize.md)
- [- reportEjectability](./ioblockstoragedevice/api-1568454-reportejectability.md)
- [- reportLockability](./ioblockstoragedevice/api-1568445-reportlockability.md)
- [- reportMaxValidBlock](./ioblockstoragedevice/api-1568465-reportmaxvalidblock.md)
- [- reportMediaState](./ioblockstoragedevice/api-1568475-reportmediastate.md)
- [- reportPollRequirements](./ioblockstoragedevice/api-1568457-reportpollrequirements.md)
- [- reportRemovability](./ioblockstoragedevice/api-1568478-reportremovability.md)
- [- reportWriteProtection](./ioblockstoragedevice/api-1568463-reportwriteprotection.md)
- [- requestIdle](./ioblockstoragedevice/api-1568442-requestidle.md)
- [- setProperties](./ioblockstoragedevice/api-1568464-setproperties.md)
- [- setWriteCacheState](./ioblockstoragedevice/api-1568468-setwritecachestate.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Devices
- [IOBlockStorageServices](./ioblockstorageservices.md)
- [IOCDBlockStorageDevice](./iocdblockstoragedevice.md)
  The IOCDBlockStorageDevice class is a generic CD block storage device abstraction.
- [IOBDServices](./iobdservices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioblockstoragedevice)*