# synchronizationMode

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The value that defines how the disk synchronizes with the underlying storage when the guest operating system flushes data.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var synchronizationMode: VZDiskSynchronizationMode { get }
```

```objc
@property (readonly) VZDiskSynchronizationMode synchronizationMode;
```

## See Also

### Getting the block storage device details
- [var fileHandle: FileHandle](./filehandle.md)
  A file handle to a block device.
- [var isReadOnly: Bool](./isreadonly.md)
  A Boolean value that indicates whether this disk attachment is read-only; otherwise, if the file handle allows writes, the device can write data into it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskblockdevicestoragedeviceattachment/synchronizationmode)*