# WebPage.FrameInfo

**Framework**: WebKit  
**Kind**: struct

A type that contains information about a frame on a webpage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
struct FrameInfo
```

## Topics

### Instance Properties
- [var isMainFrame: Bool](webpage/frameinfo/ismainframe.md)
  Indicates whether the frame is the web site’s main frame or a subframe.
- [var request: URLRequest](webpage/frameinfo/request.md)
  The frame’s current request.
- [var securityOrigin: WKSecurityOrigin](webpage/frameinfo/securityorigin.md)
  The frame’s security origin.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NavigationDeciding](webpage/navigationdeciding.md)
  Allows providing custom behavior to handle navigation changes and to coordinate these changes for the web page’s main page.
- [WebPage.NavigationAction](webpage/navigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [WebPage.NavigationResponse](webpage/navigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [WebPage.NavigationPreferences](webpage/navigationpreferences.md)
  A type that specifies the behaviors to use when loading and rendering page content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/frameinfo)*