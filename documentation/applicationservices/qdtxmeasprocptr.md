# QDTxMeasProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias QDTxMeasProcPtr = (Int16, UnsafeRawPointer?, UnsafeMutablePointer<Point>?, UnsafeMutablePointer<Point>?, UnsafeMutablePointer<FontInfo>?) -> Int16
```

```c
typedef short (*QDTxMeasProcPtr)(short byteCount, const void *textAddr, Point *numer, Point *denom, FontInfo *info);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/qdtxmeasprocptr)*