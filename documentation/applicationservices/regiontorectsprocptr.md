# RegionToRectsProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias RegionToRectsProcPtr = (UInt16, RgnHandle?, UnsafePointer<Rect>?, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef OSStatus (*RegionToRectsProcPtr)(UInt16 message, RgnHandle rgn, const Rect *rect, void *refCon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/regiontorectsprocptr)*