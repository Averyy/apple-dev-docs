# synchronizationMode

**Framework**: Virtualization  
**Kind**: property

The value that defines how the disk synchronizes with the underlying storage when the guest operating system flushes data.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var synchronizationMode: VZDiskSynchronizationMode { get }
```

## See Also

- [var fileHandle: FileHandle](vzdiskblockdevicestoragedeviceattachment/filehandle.md)
  A file handle to a block device.
- [var isReadOnly: Bool](vzdiskblockdevicestoragedeviceattachment/isreadonly.md)
  A Boolean value that indicates whether this disk attachment is read-only; otherwise, if the file handle allows writes, the device can write data into it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskblockdevicestoragedeviceattachment/synchronizationmode)*