# QDRRectProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias QDRRectProcPtr = (GrafVerb, UnsafePointer<Rect>?, Int16, Int16) -> Void
```

```c
typedef void (*QDRRectProcPtr)(GrafVerb verb, const Rect *r, short ovalWidth, short ovalHeight);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/qdrrectprocptr)*