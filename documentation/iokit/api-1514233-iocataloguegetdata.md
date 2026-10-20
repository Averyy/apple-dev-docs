# IOCatalogueGetData(_:_:_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func IOCatalogueGetData(_ mainPort: mach_port_t, _ flag: UInt32, _ buffer: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>!, _ size: UnsafeMutablePointer<UInt32>!) -> kern_return_t
```

```c
kern_return_t IOCatalogueGetData(mach_port_t mainPort, uint32_t flag, char **buffer, uint32_t *size);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514233-iocataloguegetdata)*