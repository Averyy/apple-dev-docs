# OSLogPointerFormat.sockaddr

**Framework**: os  
**Kind**: case

An option to display the pointer bytes as a socket address.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
case sockaddr
```

#### Discussion

This option prints an easily readable `sockaddr` structure.

## See Also

- [OSLogPointerFormat.none](oslogpointerformat/none.md)
  An option to treat the pointer as raw bytes, and not format it.
- [OSLogPointerFormat.ipv6Address](oslogpointerformat/ipv6address.md)
  An option to display the pointer bytes as an IPv6 network address.
- [OSLogPointerFormat.timespec](oslogpointerformat/timespec.md)
  An option to display the pointer bytes as a time specification.
- [OSLogPointerFormat.timeval](oslogpointerformat/timeval.md)
  An option to display the pointer bytes as a time value.
- [OSLogPointerFormat.uuid](oslogpointerformat/uuid.md)
  An option to display the pointer bytes as a formatted UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogpointerformat/sockaddr)*