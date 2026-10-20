# FMFontFamilyCallbackFilterProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
typealias FMFontFamilyCallbackFilterProcPtr = (FMFontFamily, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef OSStatus (*FMFontFamilyCallbackFilterProcPtr)(FMFontFamily iFontFamily, void *iRefCon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/fmfontfamilycallbackfilterprocptr)*