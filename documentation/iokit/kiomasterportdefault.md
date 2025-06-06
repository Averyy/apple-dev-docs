# kIOMasterPortDefault

**Framework**: IOKit  
**Kind**: data

The default mach port used to initiate communication with IOKit.

**Availability**:
- Mac Catalyst 10.14+
- macOS 10.0+ - Deprecated in 12.0

## Declaration

```swift
let kIOMasterPortDefault: mach_port_t
```

#### Discussion

When specifying a primary port to IOKit functions, the NULL argument indicates "use the default". This is a synonym for NULL, if you'd rather use a named constant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiomasterportdefault)*