# reportMediaState

**Framework**: Kernel  
**Kind**: instm

Report the device's media state.

## Declaration

```cpp
virtual IOReturn reportMediaState(
 bool *mediaPresent,
 bool *changedState = 0) = 0;
```

## Overview

This method reports whether we have media in the drive or not, and whether the state has changed from the previously reported state.

A result of kIOReturnSuccess is always returned if the test for media is successful, regardless of media presence. The mediaPresent result should be used to determine whether media is present or not. A return other than kIOReturnSuccess indicates that the Transport Driver was unable to interrogate the device. In this error case, the outputs mediaState and changedState will *not* be stored.

## Parameters

- `mediaPresent`: Pointer to returned media state. True indicates media is present in the device; False indicates no media is present.

## See Also

### Miscellaneous
- [doAsyncReadWrite](./api-1811665-doasyncreadwrite.md)
  Start an asynchronous read or write operation.
- [doEjectMedia](./api-1811672-doejectmedia.md)
  Eject the media.
- [doFormatMedia](./api-1811680-doformatmedia.md)
  Format the media to the specified byte capacity.
- [doGetFormatCapacities](./api-1811684-dogetformatcapacities.md)
  Return the allowable formatting byte capacities.
- [doSynchronizeCache](./api-1811691-dosynchronizecache.md)
  Force data blocks in the hardware's buffer to be flushed to the media.
- [doUnmap](./api-1811698-dounmap.md)
  Delete unused data blocks from the media.
- [getAdditionalDeviceInfoString](./api-1811705-getadditionaldeviceinfostring.md)
  Return additional informational string for the device.
- [getProductString](./api-1811712-getproductstring.md)
  Return Product Name string for the device.
- [getRevisionString](./api-1811717-getrevisionstring.md)
  Return Product Revision string for the device.
- [getVendorString](./api-1811724-getvendorstring.md)
  Return Vendor Name string for the device.
- [getWriteCacheState](./api-1811731-getwritecachestate.md)
  Reports the current write cache state of the device.
- [init](./api-1811746-init.md)
- [reportBlockSize](./api-1811753-reportblocksize.md)
  Report the block size for the device, in bytes.
- [reportEjectability](./api-1811761-reportejectability.md)
  Report if the media is ejectable under software control.
- [reportMaxValidBlock](./api-1811771-reportmaxvalidblock.md)
  Report the highest valid block for the device.
- [reportRemovability](./api-1811787-reportremovability.md)
  Report whether the media is removable or not.
- [reportWriteProtection](./api-1811796-reportwriteprotection.md)
  Report whether the media is write-protected or not.
- [requestIdle](./api-1811804-requestidle.md)
  Request that the device enter an idle state.
- [setWriteCacheState](./api-1811812-setwritecachestate.md)
  Sets the write cache state of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioblockstoragedevice/1811780-reportmediastate)*