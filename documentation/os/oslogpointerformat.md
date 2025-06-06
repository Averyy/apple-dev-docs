# OSLogPointerFormat

**Framework**: os  
**Kind**: enum

The formatting options for pointer data.

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
enum OSLogPointerFormat
```

## Mentions

- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md)

## Topics

### Getting the Format Options
- [OSLogPointerFormat.none](oslogpointerformat/none.md)
  An option to treat the pointer as raw bytes, and not format it.
- [OSLogPointerFormat.ipv6Address](oslogpointerformat/ipv6address.md)
  An option to display the pointer bytes as an IPv6 network address.
- [OSLogPointerFormat.sockaddr](oslogpointerformat/sockaddr.md)
  An option to display the pointer bytes as a socket address.
- [OSLogPointerFormat.timespec](oslogpointerformat/timespec.md)
  An option to display the pointer bytes as a time specification.
- [OSLogPointerFormat.timeval](oslogpointerformat/timeval.md)
  An option to display the pointer bytes as a time value.
- [OSLogPointerFormat.uuid](oslogpointerformat/uuid.md)
  An option to display the pointer bytes as a formatted UUID.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [enum OSLogBoolFormat](oslogboolformat.md)
  The formatting options for Boolean values.
- [struct OSLogIntegerFormatting](oslogintegerformatting.md)
  The formatting options for integer values.
- [enum OSLogInt32ExtendedFormat](oslogint32extendedformat.md)
  The formatting options for 32-bit integer values.
- [struct OSLogFloatFormatting](oslogfloatformatting.md)
  The formatting options for double and floating-point numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogpointerformat)*