# IOCatalogueTerminate(_:_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func IOCatalogueTerminate(_ mainPort: mach_port_t, _ flag: UInt32, _ description: UnsafeMutablePointer<CChar>!) -> kern_return_t
```

```c
kern_return_t IOCatalogueTerminate(mach_port_t mainPort, uint32_t flag, io_name_t description);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514665-iocatalogueterminate)*