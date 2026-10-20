# IconActionProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias IconActionProcPtr = (ResType, UnsafeMutablePointer<Handle?>?, UnsafeMutableRawPointer?) -> OSErr
```

```c
typedef OSErr (*IconActionProcPtr)(ResType theType, Handle *theIcon, void *yourDataPtr);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/iconactionprocptr)*