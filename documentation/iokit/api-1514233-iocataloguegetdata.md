# IOCatalogueGetData(_:_:_:_:)

**Framework**: IOKit  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
func IOCatalogueGetData(_ mainPort: mach_port_t, _ flag: UInt32, _ buffer: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>!, _ size: UnsafeMutablePointer<UInt32>!) -> kern_return_t
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514233-iocataloguegetdata)*