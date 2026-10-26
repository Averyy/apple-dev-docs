# AddRef

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!
```

```c
ULONG (*AddRef)(void *thisPointer);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iocfplugininterface/1412440-addref)*