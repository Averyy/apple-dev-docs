# CSIdentityStatusUpdatedCallback

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
typealias CSIdentityStatusUpdatedCallback = (CSIdentity?, CFIndex, CFError?, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*CSIdentityStatusUpdatedCallback)(CSIdentityRef identity, CFIndex status, CFErrorRef error, void *info);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/csidentitystatusupdatedcallback)*