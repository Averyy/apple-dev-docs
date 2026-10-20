# IOCatalogueModuleLoaded(_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func IOCatalogueModuleLoaded(_ mainPort: mach_port_t, _ name: UnsafeMutablePointer<CChar>!) -> kern_return_t
```

```c
kern_return_t IOCatalogueModuleLoaded(mach_port_t mainPort, io_name_t name);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514886-iocataloguemoduleloaded)*