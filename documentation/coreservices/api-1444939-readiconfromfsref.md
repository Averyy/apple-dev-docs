# ReadIconFromFSRef(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.1+ - Deprecated in 10.13

## Declaration

```swift
func ReadIconFromFSRef(_ ref: UnsafePointer<FSRef>!, _ iconFamily: UnsafeMutablePointer<IconFamilyHandle?>!) -> OSStatus
```

```c
OSStatus ReadIconFromFSRef(const FSRef *ref, IconFamilyHandle *iconFamily);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444939-readiconfromfsref)*