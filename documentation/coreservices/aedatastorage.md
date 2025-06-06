# AEDataStorage

**Framework**: Core Services  
**Kind**: tdef

A pointer to an opaque data type that provides storage for an `AEDesc` descriptor.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AEDataStorage = UnsafeMutablePointer<AEDataStorageType?>
```

#### Discussion

The Apple Event Manager defines the `AEDataStorage` data type to serve as a data storage field in the [`AEDesc`](aedesc.md) structure. Your application doesn’t access the data pointed to by a data storage pointer directly. Rather, you work with the following functions:

- [`AEGetDescDataSize(_:)`](1450119-aegetdescdatasize.md)
- [`AEGetDescData(_:_:_:)`](1444427-aegetdescdata.md)
- [`AEGetDescDataRange(_:_:_:_:)`](1446560-aegetdescdatarange.md)
- [`AEReplaceDescData(_:_:_:_:)`](1446695-aereplacedescdata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aedatastorage)*