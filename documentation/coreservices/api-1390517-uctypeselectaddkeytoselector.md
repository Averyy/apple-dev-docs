# UCTypeSelectAddKeyToSelector(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func UCTypeSelectAddKeyToSelector(_ inRef: UCTypeSelectRef!, _ inText: CFString!, _ inEventTime: Double, _ updateFlag: UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus
```

```c
OSStatus UCTypeSelectAddKeyToSelector(UCTypeSelectRef inRef, CFStringRef inText, double inEventTime, Boolean *updateFlag);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390517-uctypeselectaddkeytoselector)*