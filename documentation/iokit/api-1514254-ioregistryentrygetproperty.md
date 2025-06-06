# IORegistryEntryGetProperty(_:_:_:_:)

**Framework**: IOKit  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
func IORegistryEntryGetProperty(_ entry: io_registry_entry_t, _ propertyName: UnsafePointer<CChar>!, _ buffer: UnsafeMutablePointer<CChar>!, _ size: UnsafeMutablePointer<UInt32>!) -> kern_return_t
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514254-ioregistryentrygetproperty)*