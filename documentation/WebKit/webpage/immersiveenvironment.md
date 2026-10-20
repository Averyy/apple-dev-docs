# WebPage.ImmersiveEnvironment

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

An object representing a website-provided immersive environment that is ready for presentation.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
@MainActor
struct ImmersiveEnvironment
```

## Topics

### Instance Properties
- [var sourceFrame: WebPage.FrameInfo](./immersiveenvironment/sourceframe.md)
  The frame information of the website that provided this immersive environment.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Immersive environments
- [struct WebViewImmersiveEnvironmentView](../webviewimmersiveenvironmentview.md)
  A SwiftUI view that renders a specific website-provided immersive environment.
- [var allowsImmersiveEnvironments: Bool](./configuration/allowsimmersiveenvironments.md)
  Indicates whether website immersive environments are allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/immersiveenvironment)*