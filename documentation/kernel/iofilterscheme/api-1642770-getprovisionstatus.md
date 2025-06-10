# getProvisionStatus

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.12+

## Declaration

```swift
virtual IOReturn getProvisionStatus(IOService *client, UInt64 byteStart, UInt64 byteCount, UInt32 *extentsCount, IOStorageProvisionExtent *extents, IOStorageGetProvisionStatusOptions options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme/1642770-getprovisionstatus)*