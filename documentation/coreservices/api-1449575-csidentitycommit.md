# CSIdentityCommit(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CSIdentityCommit(_ identity: CSIdentity!, _ authorization: AuthorizationRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

```c
Boolean CSIdentityCommit(CSIdentityRef identity, AuthorizationRef authorization, CFErrorRef *error);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449575-csidentitycommit)*