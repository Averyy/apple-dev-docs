# FMFontCallbackFilterProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
typealias FMFontCallbackFilterProcPtr = (FMFont, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef OSStatus (*FMFontCallbackFilterProcPtr)(FMFont iFont, void *iRefCon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/fmfontcallbackfilterprocptr)*