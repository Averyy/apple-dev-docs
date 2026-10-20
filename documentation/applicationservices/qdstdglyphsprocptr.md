# QDStdGlyphsProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias QDStdGlyphsProcPtr = (UnsafeMutableRawPointer?, Int) -> OSStatus
```

```c
typedef OSStatus (*QDStdGlyphsProcPtr)(void *dataStream, ByteCount size);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/qdstdglyphsprocptr)*