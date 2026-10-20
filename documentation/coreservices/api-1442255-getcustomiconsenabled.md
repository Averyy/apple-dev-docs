# GetCustomIconsEnabled(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.15

## Declaration

```swift
func GetCustomIconsEnabled(_ vRefNum: Int16, _ customIconsEnabled: UnsafeMutablePointer<DarwinBoolean>!) -> OSErr
```

```c
OSErr GetCustomIconsEnabled(SInt16 vRefNum, Boolean *customIconsEnabled);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442255-getcustomiconsenabled)*