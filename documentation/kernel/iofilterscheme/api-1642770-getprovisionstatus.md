# getProvisionStatus

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.12+

## Declaration

```cpp
virtual IOReturn getProvisionStatus(IOService *client, UInt64 byteStart, UInt64 byteCount, UInt32 *extentsCount, IOStorageProvisionExtent *extents, IOStorageGetProvisionStatusOptions options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterscheme/1642770-getprovisionstatus)*