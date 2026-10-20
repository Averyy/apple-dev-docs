# CSIdentityCreate(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CSIdentityCreate(_ allocator: CFAllocator!, _ identityClass: CSIdentityClass, _ fullName: CFString!, _ posixName: CFString!, _ flags: CSIdentityFlags, _ authority: CSIdentityAuthority!) -> Unmanaged<CSIdentity>!
```

```c
CSIdentityRef CSIdentityCreate(CFAllocatorRef allocator, CSIdentityClass identityClass, CFStringRef fullName, CFStringRef posixName, CSIdentityFlags flags, CSIdentityAuthorityRef authority);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447616-csidentitycreate)*