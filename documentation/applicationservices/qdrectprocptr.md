# QDRectProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias QDRectProcPtr = (GrafVerb, UnsafePointer<Rect>?) -> Void
```

```c
typedef void (*QDRectProcPtr)(GrafVerb verb, const Rect *r);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/qdrectprocptr)*