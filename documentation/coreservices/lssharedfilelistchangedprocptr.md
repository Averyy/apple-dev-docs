# LSSharedFileListChangedProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 16.0+
- macOS 10.5+

## Declaration

```swift
typealias LSSharedFileListChangedProcPtr = (LSSharedFileList, UnsafeMutableRawPointer) -> Void
```

```c
typedef void (*LSSharedFileListChangedProcPtr)(LSSharedFileListRef inList, void *context);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lssharedfilelistchangedprocptr)*