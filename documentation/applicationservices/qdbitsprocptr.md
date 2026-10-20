# QDBitsProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias QDBitsProcPtr = (UnsafePointer<BitMap>?, UnsafePointer<Rect>?, UnsafePointer<Rect>?, Int16, RgnHandle?) -> Void
```

```c
typedef void (*QDBitsProcPtr)(const BitMap *srcBits, const Rect *srcRect, const Rect *dstRect, short mode, RgnHandle maskRgn);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/qdbitsprocptr)*