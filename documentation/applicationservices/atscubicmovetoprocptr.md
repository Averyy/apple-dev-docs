# ATSCubicMoveToProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias ATSCubicMoveToProcPtr = (UnsafePointer<Float32Point>?, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef OSStatus (*ATSCubicMoveToProcPtr)(const Float32Point *pt, void *callBackDataPtr);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/atscubicmovetoprocptr)*