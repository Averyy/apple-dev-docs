# ATSQuadraticLineProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias ATSQuadraticLineProcPtr = (UnsafePointer<Float32Point>?, UnsafePointer<Float32Point>?, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef OSStatus (*ATSQuadraticLineProcPtr)(const Float32Point *pt1, const Float32Point *pt2, void *callBackDataPtr);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/atsquadraticlineprocptr)*