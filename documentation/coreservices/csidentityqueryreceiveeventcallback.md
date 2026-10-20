# CSIdentityQueryReceiveEventCallback

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
typealias CSIdentityQueryReceiveEventCallback = (CSIdentityQuery?, CSIdentityQueryEvent, CFArray?, CFError?, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*CSIdentityQueryReceiveEventCallback)(CSIdentityQueryRef query, CSIdentityQueryEvent event, CFArrayRef identities, CFErrorRef error, void *info);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/csidentityqueryreceiveeventcallback)*