# CSIdentityQueryCreateForPosixID(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CSIdentityQueryCreateForPosixID(_ allocator: CFAllocator!, _ posixID: id_t, _ identityClass: CSIdentityClass, _ authority: CSIdentityAuthority!) -> Unmanaged<CSIdentityQuery>!
```

```c
CSIdentityQueryRef CSIdentityQueryCreateForPosixID(CFAllocatorRef allocator, id_t posixID, CSIdentityClass identityClass, CSIdentityAuthorityRef authority);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1428990-csidentityquerycreateforposixid)*