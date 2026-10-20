# HIShapeEnumerateProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.5+

## Declaration

```swift
typealias HIShapeEnumerateProcPtr = (Int32, HIShape?, UnsafePointer<CGRect>?, UnsafeMutableRawPointer?) -> OSStatus
```

```c
typedef OSStatus (*HIShapeEnumerateProcPtr)(int inMessage, HIShapeRef inShape, const CGRect *inRect, void *inRefcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/hishapeenumerateprocptr)*