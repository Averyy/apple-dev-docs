# LSSharedFileListCreate(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+ - Deprecated in 10.11

## Declaration

```swift
func LSSharedFileListCreate(_ inAllocator: CFAllocator?, _ inListType: CFString, _ listOptions: CFTypeRef?) -> Unmanaged<LSSharedFileList>?
```

```c
LSSharedFileListRef LSSharedFileListCreate(CFAllocatorRef inAllocator, CFStringRef inListType, CFTypeRef listOptions);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1443926-lssharedfilelistcreate)*