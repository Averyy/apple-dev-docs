# isReadOnly

**Framework**: Virtualization  
**Kind**: property

A Boolean value that indicates whether this disk attachment is read-only; otherwise, if the file handle allows writes, the device can write data into it.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var isReadOnly: Bool { get }
```

## See Also

- [var fileHandle: FileHandle](vzdiskblockdevicestoragedeviceattachment/filehandle.md)
  A file handle to a block device.
- [var synchronizationMode: VZDiskSynchronizationMode](vzdiskblockdevicestoragedeviceattachment/synchronizationmode.md)
  The value that defines how the disk synchronizes with the underlying storage when the guest operating system flushes data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskblockdevicestoragedeviceattachment/isreadonly)*