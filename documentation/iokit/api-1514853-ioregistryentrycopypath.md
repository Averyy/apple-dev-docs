# IORegistryEntryCopyPath(_:_:)

**Framework**: IOKit  
**Kind**: func

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func IORegistryEntryCopyPath(_ entry: io_registry_entry_t, _ plane: UnsafePointer<CChar>!) -> Unmanaged<CFString>!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514853-ioregistryentrycopypath)*