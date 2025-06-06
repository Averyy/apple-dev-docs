# vfs_clearauthopaqueaccess

**Framework**: Kernel  
**Kind**: func

Mark a filesystem as not having remote VNOP_ACCESS support.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vfs_clearauthopaqueaccess(mount_t mp);
```

#### Return_value

void.

## Parameters

- `mp`: Mount to mark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523231-vfs_clearauthopaqueaccess)*