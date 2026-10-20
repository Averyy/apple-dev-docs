# IOServiceOFPathToBSDName(_:_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```swift
func IOServiceOFPathToBSDName(_ mainPort: mach_port_t, _ openFirmwarePath: UnsafePointer<CChar>!, _ bsdName: UnsafeMutablePointer<CChar>!) -> kern_return_t
```

```c
kern_return_t IOServiceOFPathToBSDName(mach_port_t mainPort, const io_name_t openFirmwarePath, io_name_t bsdName);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514661-ioserviceofpathtobsdname)*