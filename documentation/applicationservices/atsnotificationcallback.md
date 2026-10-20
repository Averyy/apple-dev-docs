# ATSNotificationCallback

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
typealias ATSNotificationCallback = (ATSFontNotificationInfoRef?, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*ATSNotificationCallback)(ATSFontNotificationInfoRef info, void *refCon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/atsnotificationcallback)*