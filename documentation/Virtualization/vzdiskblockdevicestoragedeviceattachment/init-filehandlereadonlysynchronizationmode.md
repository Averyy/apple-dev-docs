# init(fileHandle:readOnly:synchronizationMode:)

**Framework**: Virtualization  
**Kind**: init

Creates a new block storage device attachment from a file handle and with the specified access mode, synchronization mode, and error object that you provide.

**Availability**:
- macOS 14.0+

## Declaration

```swift
init(fileHandle: FileHandle, readOnly: Bool, synchronizationMode: VZDiskSynchronizationMode) throws
```

#### Discussion

> **Note**:  The disk attachment retains the file handle, and the handle must be open when the virtual machine starts.

 The disk attachment retains the file handle, and the handle must be open when the virtual machine starts.

The `readOnly` parameter affects how the Virtualization framework exposes the disk to the guest operating system by the storage controller. If you intend to use the disk in read-only mode, it’s also a best practice to open the file handle as read-only.

## Parameters

- `fileHandle`: The   to a block device to attach to this VM.
- `readOnly`: A Boolean value that indicates whether this disk attachment is read-only; otherwise, if the file handle allows writes, the device can write data into it.
- `synchronizationMode`: The   value that defines how the disk synchronizes with the underlying storage when the guest operating system flushes data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskblockdevicestoragedeviceattachment/init(filehandle:readonly:synchronizationmode:))*