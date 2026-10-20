# GetIconRef(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.15

## Declaration

```swift
func GetIconRef(_ vRefNum: Int16, _ creator: OSType, _ iconType: OSType, _ theIconRef: UnsafeMutablePointer<IconRef?>!) -> OSErr
```

```c
OSErr GetIconRef(SInt16 vRefNum, OSType creator, OSType iconType, IconRef *theIconRef);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442776-geticonref)*