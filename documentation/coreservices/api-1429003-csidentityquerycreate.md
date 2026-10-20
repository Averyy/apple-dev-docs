# CSIdentityQueryCreate(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CSIdentityQueryCreate(_ allocator: CFAllocator!, _ identityClass: CSIdentityClass, _ authority: CSIdentityAuthority!) -> Unmanaged<CSIdentityQuery>!
```

```c
CSIdentityQueryRef CSIdentityQueryCreate(CFAllocatorRef allocator, CSIdentityClass identityClass, CSIdentityAuthorityRef authority);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1429003-csidentityquerycreate)*