# VZDiskImageSynchronizationMode.none

**Framework**: Virtualization  
**Kind**: case  
**Role**: Case

Disables data synchronization with the permanent storage.

**Availability**:
- macOS 12.0+

## Declaration

```swift
case none
```

```c
VZDiskImageSynchronizationModeNone
```

#### Discussion

This option doesn’t guarantee data integrity if any error condition occurs, such as disk full on the host, panic, power loss, and so on.

This mode is useful when a VM is run only once to perform a task to completion or failure. In that case, the framework can’t safely reuse the disk image on failure.

Using this mode may result in improved performance because no synchronization with the underlying storage is necessary.

## See Also

### Disk image synchronization modes
- [VZDiskImageSynchronizationMode.full](./full.md)
  Synchronizes data to the permanent storage holding the disk image.
- [VZDiskImageSynchronizationMode.fsync](./fsync.md)
  Synchronizes data to the drive using the system’s best-effort synchronization mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagesynchronizationmode/none)*