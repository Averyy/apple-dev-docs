# IOMainPort(_:_:)

**Framework**: IOKit  
**Kind**: func

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func IOMainPort(_ bootstrapPort: mach_port_t, _ mainPort: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/3753260-iomainport)*