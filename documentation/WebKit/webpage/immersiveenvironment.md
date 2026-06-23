# WebPage.ImmersiveEnvironment

**Framework**: WebKit  
**Kind**: struct

An object representing a website-provided immersive environment that is ready for presentation.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
struct ImmersiveEnvironment
```

## Topics

### Instance Properties
- [var sourceFrame: WebPage.FrameInfo](webpage/immersiveenvironment/sourceframe.md)
  The frame information of the website that provided this immersive environment.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WebViewImmersiveEnvironmentView](webviewimmersiveenvironmentview.md)
  A SwiftUI view that renders a specific website-provided immersive environment.
- [var allowsImmersiveEnvironments: Bool](webpage/configuration/allowsimmersiveenvironments.md)
  Indicates whether website immersive environments are allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/immersiveenvironment)*