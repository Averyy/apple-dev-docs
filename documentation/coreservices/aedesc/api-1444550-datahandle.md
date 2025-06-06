# dataHandle

**Framework**: Core Services  
**Kind**: structp

An opaque storage type that points to the storagefor the descriptor data. Your application doesn’t access thisdata directly—rather, it calls one of the functions [`AEGetDescDataSize(_:)`](1450119-aegetdescdatasize.md), [`AEGetDescData(_:_:_:)`](1444427-aegetdescdata.md), or [`AEReplaceDescData(_:_:_:_:)`](1446695-aereplacedescdata.md).See [`AEDataStorage`](aedatastorage.md).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var dataHandle: AEDataStorage!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aedesc/1444550-datahandle)*