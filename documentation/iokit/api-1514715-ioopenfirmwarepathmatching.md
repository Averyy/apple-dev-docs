# IOOpenFirmwarePathMatching(_:_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```swift
func IOOpenFirmwarePathMatching(_ mainPort: mach_port_t, _ options: UInt32, _ path: UnsafePointer<CChar>!) -> Unmanaged<CFMutableDictionary>!
```

```c
CFMutableDictionaryRef IOOpenFirmwarePathMatching(mach_port_t mainPort, uint32_t options, const char *path);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514715-ioopenfirmwarepathmatching)*