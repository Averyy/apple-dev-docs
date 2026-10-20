# ATSCubicCurveToProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias ATSCubicCurveToProcPtr = (UnsafePointer<Float32Point>?, UnsafePointer<Float32Point>?, UnsafePointer<Float32Point>?, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef OSStatus (*ATSCubicCurveToProcPtr)(const Float32Point *pt1, const Float32Point *pt2, const Float32Point *pt3, void *callBackDataPtr);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/atscubiccurvetoprocptr)*