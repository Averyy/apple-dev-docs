# AnimationFormatString.OSLogMessage

**Framework**: os  
**Kind**: struct  
**Role**: Structure

A log message that includes an animation tag.

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
@frozen
struct OSLogMessage
```

#### Overview

An [`AnimationFormatString.OSLogMessage`](./oslogmessage.md) structure contains a message that you construct from a string interpolation or string literal. This message includes an additional animation tag. Don’t create this structure directly. The system creates one automatically when you log a message using the [`os_signpost(_:dso:log:name:signpostID:_:_:)`](../os_signpost%28_,dso,log,name,signpostid,_,_%29-nez5.md) function

## Topics

### Creating a Format String
- [init(stringLiteral: String)](./oslogmessage/init%28stringliteral%29.md)
  Creates a log message using a string literal.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../Swift/expressiblebyunicodescalarliteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/animationformatstring/oslogmessage)*