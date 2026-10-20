# CSDiskSpaceStartRecovery(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CSDiskSpaceStartRecovery(_ volumeURL: CFURL!, _ bytesNeeded: UInt64, _ options: CSDiskSpaceRecoveryOptions, _ outOperationUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>!, _ callbackQueue: dispatch_queue_t!, _ callback: CSDiskSpaceRecoveryCallback!)
```

```c
void CSDiskSpaceStartRecovery(CFURLRef volumeURL, UInt64 bytesNeeded, CSDiskSpaceRecoveryOptions options, CFUUIDRef *outOperationUUID, dispatch_queue_t callbackQueue, CSDiskSpaceRecoveryCallback callback);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447968-csdiskspacestartrecovery)*