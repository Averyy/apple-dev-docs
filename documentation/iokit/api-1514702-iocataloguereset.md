# IOCatalogueReset(_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func IOCatalogueReset(_ mainPort: mach_port_t, _ flag: UInt32) -> kern_return_t
```

```c
kern_return_t IOCatalogueReset(mach_port_t mainPort, uint32_t flag);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514702-iocataloguereset)*