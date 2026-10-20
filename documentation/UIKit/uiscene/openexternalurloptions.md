# UIScene.OpenExternalURLOptions

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UISceneOpenExternalURLOptions : NSObject
```

## Topics

### Specifying the link options
- [var universalLinksOnly: Bool](./openexternalurloptions/universallinksonly.md)
  A Boolean value that indicates whether URLs must be universal links and have a configured app to open them.
### Measuring ad taps
- [var eventAttribution: UIEventAttribution?](./openexternalurloptions/eventattribution.md)
  An object you use to send tap event attribution data to the browser for Private Click Measurement.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### URL management
- [class UIOpenURLContext](../uiopenurlcontext.md)
  A system-provided object that contains the information you need to open a single URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/openexternalurloptions)*