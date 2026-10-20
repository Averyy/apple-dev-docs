# RegisterIconRefFromIconFamily(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.15

## Declaration

```swift
func RegisterIconRefFromIconFamily(_ creator: OSType, _ iconType: OSType, _ iconFamily: IconFamilyHandle!, _ theIconRef: UnsafeMutablePointer<IconRef?>!) -> OSErr
```

```c
OSErr RegisterIconRefFromIconFamily(OSType creator, OSType iconType, IconFamilyHandle iconFamily, IconRef *theIconRef);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1443918-registericonreffromiconfamily)*