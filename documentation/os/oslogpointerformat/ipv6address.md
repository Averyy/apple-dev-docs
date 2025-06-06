# OSLogPointerFormat.ipv6Address

**Framework**: os  
**Kind**: case

An option to display the pointer bytes as an IPv6 network address.

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
case ipv6Address
```

#### Discussion

This option formats an `in6_addr` structure as an easily readable string.

## See Also

- [OSLogPointerFormat.none](oslogpointerformat/none.md)
  An option to treat the pointer as raw bytes, and not format it.
- [OSLogPointerFormat.sockaddr](oslogpointerformat/sockaddr.md)
  An option to display the pointer bytes as a socket address.
- [OSLogPointerFormat.timespec](oslogpointerformat/timespec.md)
  An option to display the pointer bytes as a time specification.
- [OSLogPointerFormat.timeval](oslogpointerformat/timeval.md)
  An option to display the pointer bytes as a time value.
- [OSLogPointerFormat.uuid](oslogpointerformat/uuid.md)
  An option to display the pointer bytes as a formatted UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogpointerformat/ipv6address)*