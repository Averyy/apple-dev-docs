# vfs_name

**Framework**: Kernel  
**Kind**: func

Copy filesystem name into a buffer.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vfs_name(mount_t mp, char *buffer);
```

#### Return_value

void.

#### Discussion

Get filesystem name; this refers to the filesystem type of which a mount is an instantiation, rather than a name specific to the mountpoint.

## Parameters

- `mp`: Mount for which to get name.
- `buffer`: Destination for name; length should be at least MFSNAMELEN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523128-vfs_name)*