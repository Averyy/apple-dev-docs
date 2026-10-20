# IOCatalogueSendData(_:_:_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func IOCatalogueSendData(_ mainPort: mach_port_t, _ flag: UInt32, _ buffer: UnsafePointer<CChar>!, _ size: UInt32) -> kern_return_t
```

```c
kern_return_t IOCatalogueSendData(mach_port_t mainPort, uint32_t flag, const char *buffer, uint32_t size);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514405-iocataloguesenddata)*