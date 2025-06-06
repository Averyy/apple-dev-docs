# vfs_setflags

**Framework**: Kernel  
**Kind**: func

Set flags on a mount.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vfs_setflags(mount_t mp, uint64_t flags);
```

#### Return_value

Flags.

#### Discussion

Sets mount flags to the bitwise "OR" of their current value and the specified bits. Often used by a filesystem as part of the mount process.

## Parameters

- `mp`: Mount whose flags to set.
- `flags`: Flags to activate. Must be in the bitwise "OR" of MNT_VISFLAGMASK and MNT_CMDFLAGS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523521-vfs_setflags)*