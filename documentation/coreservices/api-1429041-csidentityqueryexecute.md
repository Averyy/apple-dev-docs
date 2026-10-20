# CSIdentityQueryExecute(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func CSIdentityQueryExecute(_ query: CSIdentityQuery!, _ flags: CSIdentityQueryFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

```c
Boolean CSIdentityQueryExecute(CSIdentityQueryRef query, CSIdentityQueryFlags flags, CFErrorRef *error);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1429041-csidentityqueryexecute)*