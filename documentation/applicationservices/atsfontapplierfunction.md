# ATSFontApplierFunction

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias ATSFontApplierFunction = (ATSFontRef, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef OSStatus (*ATSFontApplierFunction)(ATSFontRef iFont, void *iRefCon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/atsfontapplierfunction)*