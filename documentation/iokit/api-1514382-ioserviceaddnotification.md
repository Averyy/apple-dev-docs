# IOServiceAddNotification(_:_:_:_:_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```swift
func IOServiceAddNotification(_ mainPort: mach_port_t, _ notificationType: UnsafePointer<CChar>!, _ matching: CFDictionary!, _ wakePort: mach_port_t, _ reference: UInt, _ notification: UnsafeMutablePointer<io_iterator_t>!) -> kern_return_t
```

```c
kern_return_t IOServiceAddNotification(mach_port_t mainPort, const io_name_t notificationType, CFDictionaryRef matching, mach_port_t wakePort, uintptr_t reference, io_iterator_t *notification);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514382-ioserviceaddnotification)*