# IOServiceOFPathToBSDName(_:_:_:)

**Framework**: IOKit  
**Kind**: func

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```swift
func IOServiceOFPathToBSDName(_ mainPort: mach_port_t, _ openFirmwarePath: UnsafePointer<CChar>!, _ bsdName: UnsafeMutablePointer<CChar>!) -> kern_return_t
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514661-ioserviceofpathtobsdname)*