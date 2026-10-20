# OSLogPointerFormat.timeval

**Framework**: os  
**Kind**: case  
**Role**: Case

An option to display the pointer bytes as a time value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
case timeval
```

#### Discussion

This option prints an easily readable `timeval` structure.

## See Also

### Getting the Format Options
- [OSLogPointerFormat.none](./none.md)
  An option to treat the pointer as raw bytes, and not format it.
- [OSLogPointerFormat.ipv6Address](./ipv6address.md)
  An option to display the pointer bytes as an IPv6 network address.
- [OSLogPointerFormat.sockaddr](./sockaddr.md)
  An option to display the pointer bytes as a socket address.
- [OSLogPointerFormat.timespec](./timespec.md)
  An option to display the pointer bytes as a time specification.
- [OSLogPointerFormat.uuid](./uuid.md)
  An option to display the pointer bytes as a formatted UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogpointerformat/timeval)*