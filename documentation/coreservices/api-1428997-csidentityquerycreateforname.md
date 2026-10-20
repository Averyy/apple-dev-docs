# CSIdentityQueryCreateForName(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func CSIdentityQueryCreateForName(_ allocator: CFAllocator!, _ name: CFString!, _ comparisonMethod: CSIdentityQueryStringComparisonMethod, _ identityClass: CSIdentityClass, _ authority: CSIdentityAuthority!) -> Unmanaged<CSIdentityQuery>!
```

```c
CSIdentityQueryRef CSIdentityQueryCreateForName(CFAllocatorRef allocator, CFStringRef name, CSIdentityQueryStringComparisonMethod comparisonMethod, CSIdentityClass identityClass, CSIdentityAuthorityRef authority);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1428997-csidentityquerycreateforname)*