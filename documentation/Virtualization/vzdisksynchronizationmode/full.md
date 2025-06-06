# VZDiskSynchronizationMode.full

**Framework**: Virtualization  
**Kind**: case

Perform all synchronization operations as requested by the guest OS.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case full
```

#### Discussion

Using this mode, `flush` and `barrier` commands from the guest result in the system sending their counterpart synchronization commands to the underlying disk implementation.

## See Also

- [VZDiskSynchronizationMode.none](vzdisksynchronizationmode/none.md)
  Don’t synchronize the data with the permanent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdisksynchronizationmode/full)*