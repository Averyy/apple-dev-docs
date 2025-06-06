# vfs_clearextendedsecurity

**Framework**: Kernel  
**Kind**: func

Mark a filesystem as NOT supporting security controls beyond POSIX permissions.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vfs_clearextendedsecurity(mount_t mp);
```

#### Return_value

void.

#### Discussion

Specific controls include ACLs, file owner UUIDs, and group UUIDs.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523368-vfs_clearextendedsecurity)*