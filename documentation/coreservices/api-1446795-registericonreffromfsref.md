# RegisterIconRefFromFSRef(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.1+ - Deprecated in 10.13

## Declaration

```swift
func RegisterIconRefFromFSRef(_ creator: OSType, _ iconType: OSType, _ iconFile: UnsafePointer<FSRef>!, _ theIconRef: UnsafeMutablePointer<IconRef?>!) -> OSStatus
```

```c
OSStatus RegisterIconRefFromFSRef(OSType creator, OSType iconType, const FSRef *iconFile, IconRef *theIconRef);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446795-registericonreffromfsref)*