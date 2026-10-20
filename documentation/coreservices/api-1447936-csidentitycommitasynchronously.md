# CSIdentityCommitAsynchronously(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CSIdentityCommitAsynchronously(_ identity: CSIdentity!, _ clientContext: UnsafePointer<CSIdentityClientContext>!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!, _ authorization: AuthorizationRef!) -> Bool
```

```c
Boolean CSIdentityCommitAsynchronously(CSIdentityRef identity, const CSIdentityClientContext *clientContext, CFRunLoopRef runLoop, CFStringRef runLoopMode, AuthorizationRef authorization);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447936-csidentitycommitasynchronously)*