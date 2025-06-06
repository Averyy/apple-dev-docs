# vfs_clearflags

**Framework**: Kernel  
**Kind**: func

Clear flags on a mount.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vfs_clearflags(mount_t mp, uint64_t flags);
```

#### Return_value

void.

#### Discussion

Sets mount flags to the bitwise "AND" of their current value and the complement of the specified bits.

## Parameters

- `mp`: Mount whose flags to set.
- `flags`: Flags to deactivate. Must be in the bitwise "OR" of MNT_VISFLAGMASK and MNT_CMDFLAGS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523299-vfs_clearflags)*