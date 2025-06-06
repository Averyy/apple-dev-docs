# IOServiceAddNotification(_:_:_:_:_:_:)

**Framework**: IOKit  
**Kind**: func

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```swift
func IOServiceAddNotification(_ mainPort: mach_port_t, _ notificationType: UnsafePointer<CChar>!, _ matching: CFDictionary!, _ wakePort: mach_port_t, _ reference: UInt, _ notification: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514382-ioserviceaddnotification)*