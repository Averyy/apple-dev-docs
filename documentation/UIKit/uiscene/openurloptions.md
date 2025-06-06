# UIScene.OpenURLOptions

**Framework**: UIKit  
**Kind**: class

Options that UIKit provides when asking your app to open a URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class OpenURLOptions
```

#### Overview

Don’t create a [`UIScene.OpenURLOptions`](uiscene/openurloptions.md) object directly. UIKit creates one for you when your app receives a request to open a URL. Use the information in the object to determine how to respond to the URL.

## Topics

### Specifying the URL details
- [var sourceApplication: String?](uiscene/openurloptions/sourceapplication.md)
  The bundle ID of the app that originated the request.
- [var annotation: Any?](uiscene/openurloptions/annotation.md)
  A property-list object that contains the annotation data provided by a document interaction controller.
- [var eventAttribution: UIEventAttribution?](uiscene/openurloptions/eventattribution.md)
  An event attribution associated with the URL to open.
### Specifying the behavior options
- [var openInPlace: Bool](uiscene/openurloptions/openinplace.md)
  A Boolean value that indicates whether you should open the URL at its current location instead of copying it to your app’s container.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var url: URL](uiopenurlcontext/url.md)
  The URL to open.
- [var options: UIScene.OpenURLOptions](uiopenurlcontext/options.md)
  Additional information for determining how to open the URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/openurloptions)*