# CSDiskSpaceStartRecovery(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- macOS 10.7+

## Declaration

```swift
func CSDiskSpaceStartRecovery(_ volumeURL: CFURL!, _ bytesNeeded: UInt64, _ options: CSDiskSpaceRecoveryOptions, _ outOperationUUID: UnsafeMutablePointer<Unmanaged<CFUUID>?>!, _ callbackQueue: dispatch_queue_t!, _ callback: CSDiskSpaceRecoveryCallback!)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447968-csdiskspacestartrecovery)*