# QDArcProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias QDArcProcPtr = (GrafVerb, UnsafePointer<Rect>?, Int16, Int16) -> Void
```

```c
typedef void (*QDArcProcPtr)(GrafVerb verb, const Rect *r, short startAngle, short arcAngle);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/qdarcprocptr)*