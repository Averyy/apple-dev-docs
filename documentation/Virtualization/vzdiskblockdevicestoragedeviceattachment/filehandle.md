# fileHandle

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A file handle to a block device.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var fileHandle: FileHandle { get }
```

```objc
@property (strong, readonly) NSFileHandle * fileHandle;
```

## See Also

### Getting the block storage device details
- [var isReadOnly: Bool](./isreadonly.md)
  A Boolean value that indicates whether this disk attachment is read-only; otherwise, if the file handle allows writes, the device can write data into it.
- [var synchronizationMode: VZDiskSynchronizationMode](./synchronizationmode.md)
  The value that defines how the disk synchronizes with the underlying storage when the guest operating system flushes data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskblockdevicestoragedeviceattachment/filehandle)*