# IconGetterProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias IconGetterProcPtr = (ResType, UnsafeMutableRawPointer?) -> Handle?
```

```c
typedef Handle (*IconGetterProcPtr)(ResType theType, void *yourDataPtr);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/icongetterprocptr)*