# UIScene.OpenExternalURLOptions

**Framework**: UIKit  
**Kind**: class

Options you specify when asking a scene to open a URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class OpenExternalURLOptions
```

## Topics

### Specifying the link options
- [var universalLinksOnly: Bool](uiscene/openexternalurloptions/universallinksonly.md)
  A Boolean value that indicates whether URLs must be universal links and have a configured app to open them.
### Measuring ad taps
- [var eventAttribution: UIEventAttribution?](uiscene/openexternalurloptions/eventattribution.md)
  An object you use to send tap event attribution data to the browser for Private Click Measurement.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)

## See Also

- [class UIOpenURLContext](uiopenurlcontext.md)
  A system-provided object that contains the information you need to open a single URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/openexternalurloptions)*