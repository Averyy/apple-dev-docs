# QDOpcodeProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias QDOpcodeProcPtr = (UnsafePointer<Rect>?, UnsafePointer<Rect>?, UInt16, Int16) -> Void
```

```c
typedef void (*QDOpcodeProcPtr)(const Rect *fromRect, const Rect *toRect, UInt16 opcode, SInt16 version);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/qdopcodeprocptr)*