# reportBlockSize

**Framework**: Kernel  
**Kind**: instm

Report the block size for the device, in bytes.

## Declaration

```cpp
virtual IOReturn reportBlockSize(
 UInt64 *blockSize) = 0;
```

## Parameters

- `blockSize`: Pointer to returned block size value.

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
- [reportEjectability](./api-1811761-reportejectability.md)
  Report if the media is ejectable under software control.
- [reportMaxValidBlock](./api-1811771-reportmaxvalidblock.md)
  Report the highest valid block for the device.
- [reportMediaState](./api-1811780-reportmediastate.md)
  Report the device's media state.
- [reportRemovability](./api-1811787-reportremovability.md)
  Report whether the media is removable or not.
- [reportWriteProtection](./api-1811796-reportwriteprotection.md)
  Report whether the media is write-protected or not.
- [requestIdle](./api-1811804-requestidle.md)
  Request that the device enter an idle state.
- [setWriteCacheState](./api-1811812-setwritecachestate.md)
  Sets the write cache state of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioblockstoragedevice/1811753-reportblocksize)*