# CSIdentityQueryCreateForUUID(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CSIdentityQueryCreateForUUID(_ allocator: CFAllocator!, _ uuid: CFUUID!, _ authority: CSIdentityAuthority!) -> Unmanaged<CSIdentityQuery>!
```

```c
CSIdentityQueryRef CSIdentityQueryCreateForUUID(CFAllocatorRef allocator, CFUUIDRef uuid, CSIdentityAuthorityRef authority);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1429007-csidentityquerycreateforuuid)*