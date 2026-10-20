# AECompareDesc(_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.8+

## Declaration

```swift
func AECompareDesc(_ desc1: UnsafePointer<AEDesc>!, _ desc2: UnsafePointer<AEDesc>!, _ resultP: UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus
```

```c
OSStatus AECompareDesc(const AEDesc *desc1, const AEDesc *desc2, Boolean *resultP);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448782-aecomparedesc)*