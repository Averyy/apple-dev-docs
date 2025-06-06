# kFSEventStreamCreateFlagUseCFTypes

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var kFSEventStreamCreateFlagUseCFTypes: Int { get }
```

#### Discussion

The framework will invoke your callback function with CF types rather than raw C types (i.e., a CFArrayRef of CFStringRefs, rather than a raw C array of raw C string pointers). See FSEventStreamCallback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kfseventstreamcreateflagusecftypes)*