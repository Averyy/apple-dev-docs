# WebViewImmersiveEnvironmentView

**Framework**: WebKit  
**Kind**: struct

A SwiftUI view that renders a specific website-provided immersive environment.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
struct WebViewImmersiveEnvironmentView
```

#### Overview

Place this view in your app’s Immersive Space hierarchy. Initialize it with the `WebPage.ImmersiveEnvironment` received from the presentation callback to render that specific environment.

## Topics

### Initializers
- [init(WebPage.ImmersiveEnvironment)](webviewimmersiveenvironmentview/init(_:)-1ydxs.md)
  Creates an immersive environment view from a [`WebPage.ImmersiveEnvironment`](webpage/immersiveenvironment.md).
- [init(WKImmersiveEnvironment)](webviewimmersiveenvironmentview/init(_:)-2y2u7.md)
  Creates an immersive environment view from a `WKImmersiveEnvironment`.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webviewimmersiveenvironmentview)*