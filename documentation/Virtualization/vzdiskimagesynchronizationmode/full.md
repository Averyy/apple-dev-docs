# VZDiskImageSynchronizationMode.full

**Framework**: Virtualization  
**Kind**: case

Synchronizes data to the permanent storage holding the disk image.

**Availability**:
- macOS 12.0+

## Declaration

```swift
case full
```

#### Discussion

This mode synchronizes the data with the permanent storage holding the disk image and ensures the data moves from the disk’s internal cache to permanent storage. This ensures there’s no loss of already synchronized data in the case of panic or loss of power.

## See Also

- [VZDiskImageSynchronizationMode.fsync](vzdiskimagesynchronizationmode/fsync.md)
  Synchronizes data to the drive using the system’s best-effort synchronization mode.
- [VZDiskImageSynchronizationMode.none](vzdiskimagesynchronizationmode/none.md)
  Disables data synchronization with the permanent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagesynchronizationmode/full)*