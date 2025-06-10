# IOBlockStorageDevice

**Framework**: Kernel  
**Kind**: cl

A generic block storage device abstraction.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IOBlockStorageDevice : IOService
```

#### Overview

The IOBlockStorageDevice class exports the generic block storage protocol, independent of the physical connection protocol (e.g. SCSI, ATA, USB), forwarding all requests to its provider (the Transport Driver). Though the nub does no actual processing of requests, it is necessary in a C++ environment. The Transport Driver can be of any type, as long as it inherits from IOService. Because Transport Drivers needn't derive from a type known to IOBlockStorageDriver, it isn't possible for IOBlockStorageDriver to include the appropriate header file to allow direct communication with the Transport Driver. Thus we achieve polymorphism by having the Transport Driver instantiate a subclass of IOBlockStorageDevice. A typical implementation for a concrete subclass of IOBlockStorageDevice simply relays all methods to its provider (the Transport Driver), which implements the protocol- and device-specific behavior.

All pure-virtual functions must be implemented by the Transport Driver, which is responsible for instantiating the Nub.

## Topics

### Miscellaneous
- [doAsyncReadWrite](ioblockstoragedevice/1811665-doasyncreadwrite.md)
  Start an asynchronous read or write operation.
- [doEjectMedia](ioblockstoragedevice/1811672-doejectmedia.md)
  Eject the media.
- [doFormatMedia](ioblockstoragedevice/1811680-doformatmedia.md)
  Format the media to the specified byte capacity.
- [doGetFormatCapacities](ioblockstoragedevice/1811684-dogetformatcapacities.md)
  Return the allowable formatting byte capacities.
- [doSynchronizeCache](ioblockstoragedevice/1811691-dosynchronizecache.md)
  Force data blocks in the hardware's buffer to be flushed to the media.
- [doUnmap](ioblockstoragedevice/1811698-dounmap.md)
  Delete unused data blocks from the media.
- [getAdditionalDeviceInfoString](ioblockstoragedevice/1811705-getadditionaldeviceinfostring.md)
  Return additional informational string for the device.
- [getProductString](ioblockstoragedevice/1811712-getproductstring.md)
  Return Product Name string for the device.
- [getRevisionString](ioblockstoragedevice/1811717-getrevisionstring.md)
  Return Product Revision string for the device.
- [getVendorString](ioblockstoragedevice/1811724-getvendorstring.md)
  Return Vendor Name string for the device.
- [getWriteCacheState](ioblockstoragedevice/1811731-getwritecachestate.md)
  Reports the current write cache state of the device.
- [init](ioblockstoragedevice/1811746-init.md)
- [reportBlockSize](ioblockstoragedevice/1811753-reportblocksize.md)
  Report the block size for the device, in bytes.
- [reportEjectability](ioblockstoragedevice/1811761-reportejectability.md)
  Report if the media is ejectable under software control.
- [reportMaxValidBlock](ioblockstoragedevice/1811771-reportmaxvalidblock.md)
  Report the highest valid block for the device.
- [reportMediaState](ioblockstoragedevice/1811780-reportmediastate.md)
  Report the device's media state.
- [reportRemovability](ioblockstoragedevice/1811787-reportremovability.md)
  Report whether the media is removable or not.
- [reportWriteProtection](ioblockstoragedevice/1811796-reportwriteprotection.md)
  Report whether the media is write-protected or not.
- [requestIdle](ioblockstoragedevice/1811804-requestidle.md)
  Request that the device enter an idle state.
- [setWriteCacheState](ioblockstoragedevice/1811812-setwritecachestate.md)
  Sets the write cache state of the device.
### Instance Methods
- [- doAsyncReadWrite](ioblockstoragedevice/1568473-doasyncreadwrite.md)
- [- doDiscard](ioblockstoragedevice/1568461-dodiscard.md)
- [- doEjectMedia](ioblockstoragedevice/1568469-doejectmedia.md)
- [- doFormatMedia](ioblockstoragedevice/1568474-doformatmedia.md)
- [- doGetFormatCapacities](ioblockstoragedevice/1568458-dogetformatcapacities.md)
- [- doGetProvisionStatus](ioblockstoragedevice/1646351-dogetprovisionstatus.md)
- [- doLockUnlockMedia](ioblockstoragedevice/1568449-dolockunlockmedia.md)
- [- doSetPriority](ioblockstoragedevice/1568459-dosetpriority.md)
- [- doSynchronize](ioblockstoragedevice/1568462-dosynchronize.md)
- [- doSynchronizeCache](ioblockstoragedevice/1568444-dosynchronizecache.md)
- [- doUnmap](ioblockstoragedevice/1568476-dounmap.md)
- [- getAdditionalDeviceInfoString](ioblockstoragedevice/1568452-getadditionaldeviceinfostring.md)
- [- getMetaClass](ioblockstoragedevice/1568460-getmetaclass.md)
- [- getProductString](ioblockstoragedevice/1568467-getproductstring.md)
- [- getProperty](ioblockstoragedevice/1568466-getproperty.md)
- [- getRevisionString](ioblockstoragedevice/1568447-getrevisionstring.md)
- [- getVendorString](ioblockstoragedevice/1568480-getvendorstring.md)
- [- getWriteCacheState](ioblockstoragedevice/1568451-getwritecachestate.md)
- [- init](ioblockstoragedevice/1568471-init.md)
- [- reportBlockSize](ioblockstoragedevice/1568477-reportblocksize.md)
- [- reportEjectability](ioblockstoragedevice/1568454-reportejectability.md)
- [- reportLockability](ioblockstoragedevice/1568445-reportlockability.md)
- [- reportMaxValidBlock](ioblockstoragedevice/1568465-reportmaxvalidblock.md)
- [- reportMediaState](ioblockstoragedevice/1568475-reportmediastate.md)
- [- reportPollRequirements](ioblockstoragedevice/1568457-reportpollrequirements.md)
- [- reportRemovability](ioblockstoragedevice/1568478-reportremovability.md)
- [- reportWriteProtection](ioblockstoragedevice/1568463-reportwriteprotection.md)
- [- requestIdle](ioblockstoragedevice/1568442-requestidle.md)
- [- setProperties](ioblockstoragedevice/1568464-setproperties.md)
- [- setWriteCacheState](ioblockstoragedevice/1568468-setwritecachestate.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOBlockStorageServices](ioblockstorageservices.md)
- [IOCDBlockStorageDevice](iocdblockstoragedevice.md)
  The IOCDBlockStorageDevice class is a generic CD block storage device abstraction.
- [IOBDServices](iobdservices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioblockstoragedevice)*