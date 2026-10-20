# acquireGlobalLock

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOReturn acquireGlobalLock(IOService *client, UInt32 *lockToken, const mach_timespec_t *timeout);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioacpiplatformexpert/1563914-acquiregloballock)*