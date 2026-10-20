# IORegistryEntryCopyFromPath(_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func IORegistryEntryCopyFromPath(_ mainPort: mach_port_t, _ path: CFString!) -> io_registry_entry_t
```

```c
io_registry_entry_t IORegistryEntryCopyFromPath(mach_port_t mainPort, CFStringRef path);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514248-ioregistryentrycopyfrompath)*