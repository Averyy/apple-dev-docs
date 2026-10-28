# vfs_flags

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Retrieve mount flags.

**Availability**:
- macOS 10.4+

## Declaration

```c
uint64_t vfs_flags(mount_t mp);
```

## Return Value

Flags.

## Discussion

Results will be in the bitwise "OR" of MNT_VISFLAGMASK and MNT_CMDFLAGS.

## Parameters

- `mp`: Mount whose flags to grab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523261-vfs_flags)*