# GetIconRefFromIconFamilyPtr(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+ - Deprecated in 10.15

## Declaration

```swift
func GetIconRefFromIconFamilyPtr(_ inIconFamilyPtr: UnsafePointer<IconFamilyResource>!, _ inSize: Size, _ outIconRef: UnsafeMutablePointer<IconRef?>!) -> OSStatus
```

```c
OSStatus GetIconRefFromIconFamilyPtr(const IconFamilyResource *inIconFamilyPtr, Size inSize, IconRef *outIconRef);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1443251-geticonreffromiconfamilyptr)*