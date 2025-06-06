# VZDiskSynchronizationMode.none

**Framework**: Virtualization  
**Kind**: case

Don’t synchronize the data with the permanent storage.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case none
```

#### Discussion

This option doesn’t guarantee data integrity if any error condition occurs such as disk full on the host, panic, power loss, and so on.

This mode is useful when a VM is only run once to perform a task to completion or failure. In case of failure, the state of blocks on disk and their order isn’t defined.

Using this mode may result in improved performance since no synchronization with the underlying storage is necessary.

## See Also

- [VZDiskSynchronizationMode.full](vzdisksynchronizationmode/full.md)
  Perform all synchronization operations as requested by the guest OS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdisksynchronizationmode/none)*