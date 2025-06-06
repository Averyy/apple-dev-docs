# VZDiskSynchronizationMode

**Framework**: Virtualization  
**Kind**: enum

Values that describe the synchronization modes available to the guest OS.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum VZDiskSynchronizationMode
```

## Topics

### Synchronization modes
- [VZDiskSynchronizationMode.full](vzdisksynchronizationmode/full.md)
  Perform all synchronization operations as requested by the guest OS.
- [VZDiskSynchronizationMode.none](vzdisksynchronizationmode/none.md)
  Don’t synchronize the data with the permanent storage.
### Initializers
- [init?(rawValue: Int)](vzdisksynchronizationmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum VZDiskImageSynchronizationMode](vzdiskimagesynchronizationmode.md)
  An integer that describes the disk image synchronization mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdisksynchronizationmode)*