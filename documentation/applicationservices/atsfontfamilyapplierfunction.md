# ATSFontFamilyApplierFunction

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias ATSFontFamilyApplierFunction = (ATSFontFamilyRef, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef OSStatus (*ATSFontFamilyApplierFunction)(ATSFontFamilyRef iFamily, void *iRefCon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/atsfontfamilyapplierfunction)*