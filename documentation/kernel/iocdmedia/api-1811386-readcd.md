# readCD()

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
#ifdef __LP64__
 virtual void readCD(
 IOService *client, 
 UInt64 byteStart, 
 IOMemoryDescriptor *buffer, 
 CDSectorArea sectorArea, 
 CDSectorType sectorType, 
 IOStorageAttributes *attributes, 
 IOStorageCompletion *completion); 
#else /* !__LP64__ */
virtual void readCD(
 IOService *client, 
 UInt64 byteStart, 
 IOMemoryDescriptor *buffer, 
 CDSectorArea sectorArea, 
 CDSectorType sectorType, 
 IOStorageCompletion completion); 
#endif 
/* !__LP64__ */
```

#### Overview

Read data from the CD media object at the specified byte offset into the specified buffer, asynchronously. Special areas of the CD sector can be read via this method, such as the header and subchannel data. When the read completes, the caller will be notified via the specified completion action.

The buffer will be retained for the duration of the read.

## Parameters

- `client`: Client requesting the read.
- `byteStart`: Starting byte offset for the data transfer (see sectorArea parameter).
- `buffer`: Buffer for the data transfer. The size of the buffer implies the size of the data transfer.
- `sectorArea`: Sector area(s) to read. The sum of each area's size defines the natural block size of the media for the call. This should be taken into account when computing the address of byteStart. See IOCDTypes.h.
- `sectorType`: Sector type that is expected. The data transfer is terminated as soon as data is encountered that does not match the expected type.
- `attributes`: Attributes of the data transfer. See IOStorageAttributes. It is the responsibility of the callee to maintain the information for the duration of the data transfer, as necessary.
- `completion`: Completion routine to call once the data transfer is complete. It is the responsibility of the callee to maintain the information for the duration of the data transfer, as necessary.

## See Also

- [getSpeed](iocdmedia/1811353-getspeed.md)
- [getTOC](iocdmedia/1811363-gettoc.md)
- [read](iocdmedia/1811376-read.md)
- [readCD()](iocdmedia/1811393-readcd.md)
- [readDiscInfo](iocdmedia/1811402-readdiscinfo.md)
- [readISRC](iocdmedia/1811412-readisrc.md)
- [readMCN](iocdmedia/1811424-readmcn.md)
- [readTOC](iocdmedia/1811431-readtoc.md)
- [readTrackInfo](iocdmedia/1811438-readtrackinfo.md)
- [setSpeed](iocdmedia/1811448-setspeed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/1811386-readcd)*