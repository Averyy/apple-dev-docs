# getWriteCacheState

**Framework**: Kernel  
**Kind**: instm

Reports the current write cache state of the device.

## Declaration

```swift
#ifdef __LP64__
 virtual IOReturn getWriteCacheState(
 bool *enabled) = 0; 
#else /* !__LP64__ */
virtual IOReturn getWriteCacheState(
 bool *enabled); 
#endif 
/* !__LP64__ */
```

#### Overview

Reports the current write cache state of the device. The write cache state is not guaranteed to persist across reboots and detaches.

## Parameters

- `enabled`: Pointer to returned result. True indicates the write cache is enabled; False indicates the write cache is disabled.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioblockstoragedevice/1811731-getwritecachestate)*