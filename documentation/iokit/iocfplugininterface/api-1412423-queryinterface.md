# QueryInterface

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!
```

```c
HRESULT (*QueryInterface)(void *thisPointer, REFIID iid, LPVOID *ppv);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iocfplugininterface/1412423-queryinterface)*