# QDTextProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias QDTextProcPtr = (Int16, UnsafeRawPointer?, Point, Point) -> Void
```

```c
typedef void (*QDTextProcPtr)(short byteCount, const void *textBuf, Point numer, Point denom);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/qdtextprocptr)*