# CSIdentityCreatePersistentReference(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func CSIdentityCreatePersistentReference(_ allocator: CFAllocator!, _ identity: CSIdentity!) -> Unmanaged<CFData>!
```

```c
CFDataRef CSIdentityCreatePersistentReference(CFAllocatorRef allocator, CSIdentityRef identity);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444037-csidentitycreatepersistentrefere)*