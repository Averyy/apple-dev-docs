# VZDiskSynchronizationMode

**Framework**: Virtualization  
**Kind**: enum  
**Role**: Enumeration

Values that describe the synchronization modes available to the guest OS.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum VZDiskSynchronizationMode
```

```c
enum VZDiskSynchronizationMode : NSInteger;
```

## Topics

### Synchronization modes
- [VZDiskSynchronizationMode.full](./vzdisksynchronizationmode/full.md)
  Perform all synchronization operations as requested by the guest OS.
- [VZDiskSynchronizationMode.none](./vzdisksynchronizationmode/none.md)
  Don’t synchronize the data with the permanent storage.
### Initializers
- [init?(rawValue: Int)](./vzdisksynchronizationmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Virtual disk synchronization modes
- [enum VZDiskImageSynchronizationMode](./vzdiskimagesynchronizationmode.md)
  An integer that describes the disk image synchronization mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdisksynchronizationmode)*