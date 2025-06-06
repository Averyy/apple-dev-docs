# OSGetNotificationFromMessage(_:_:_:_:_:_:)

**Framework**: IOKit  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
func OSGetNotificationFromMessage(_ msg: UnsafeMutablePointer<mach_msg_header_t>!, _ index: UInt32, _ type: UnsafeMutablePointer<UInt32>!, _ reference: UnsafeMutablePointer<UInt>!, _ content: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ size: UnsafeMutablePointer<vm_size_t>!) -> kern_return_t
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514263-osgetnotificationfrommessage)*