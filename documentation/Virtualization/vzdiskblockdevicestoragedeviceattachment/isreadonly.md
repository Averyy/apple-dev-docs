# isReadOnly

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this disk attachment is read-only; otherwise, if the file handle allows writes, the device can write data into it.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var isReadOnly: Bool { get }
```

```objc
@property (readonly, getter=isReadOnly) BOOL readOnly;
```

## See Also

### Getting the block storage device details
- [var fileHandle: FileHandle](./filehandle.md)
  A file handle to a block device.
- [var synchronizationMode: VZDiskSynchronizationMode](./synchronizationmode.md)
  The value that defines how the disk synchronizes with the underlying storage when the guest operating system flushes data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskblockdevicestoragedeviceattachment/isreadonly)*