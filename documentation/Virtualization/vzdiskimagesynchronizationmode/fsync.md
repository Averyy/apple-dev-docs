# VZDiskImageSynchronizationMode.fsync

**Framework**: Virtualization  
**Kind**: case

Synchronizes data to the drive using the system’s best-effort synchronization mode.

**Availability**:
- macOS 12.0+

## Declaration

```swift
case fsync
```

#### Discussion

This mode synchronizes the data with the drive, but doesn’t ensure the data moves from the disk’s internal cache to permanent storage.

This is a best-effort mode with the same guarantees as the `fsync(_:)` system call.

## See Also

- [VZDiskImageSynchronizationMode.full](vzdiskimagesynchronizationmode/full.md)
  Synchronizes data to the permanent storage holding the disk image.
- [VZDiskImageSynchronizationMode.none](vzdiskimagesynchronizationmode/none.md)
  Disables data synchronization with the permanent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagesynchronizationmode/fsync)*