# AnimationFormatString.OSLogMessage

**Framework**: os  
**Kind**: struct

A log message that includes an animation tag.

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
@frozen
struct OSLogMessage
```

#### Overview

An [`AnimationFormatString.OSLogMessage`](animationformatstring/oslogmessage.md) structure contains a message that you construct from a string interpolation or string literal. This message includes an additional animation tag. Don’t create this structure directly. The system creates one automatically when you log a message using the [`os_signpost(_:dso:log:name:signpostID:_:_:)`](os_signpost(_:dso:log:name:signpostid:_:_:)-nez5.md) function

## Topics

### Creating a Format String
- [init(stringLiteral: String)](animationformatstring/oslogmessage/init(stringliteral:).md)
  Creates a log message using a string literal.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/animationformatstring/oslogmessage)*