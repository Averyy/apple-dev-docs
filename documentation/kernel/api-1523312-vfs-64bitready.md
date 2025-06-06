# vfs_64bitready

**Framework**: Kernel  
**Kind**: func

Check if the filesystem associated with a mountpoint is marked ready for interaction with 64-bit user processes.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_64bitready(mount_t mp);
```

#### Return_value

Nonzero if filesystem is ready for 64-bit; 0 otherwise.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523312-vfs_64bitready)*