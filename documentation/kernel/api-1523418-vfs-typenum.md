# vfs_typenum

**Framework**: Kernel  
**Kind**: func

Get (archaic) filesystem type number.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_typenum(mount_t mp);
```

#### Return_value

Type number.

#### Discussion

Filesystem type numbers are an old construct; most filesystems just get a number assigned based on the order in which they are registered with the system.

## Parameters

- `mp`: Mount for which to get type number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523418-vfs_typenum)*