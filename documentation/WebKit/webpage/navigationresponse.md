# WebPage.NavigationResponse

**Framework**: WebKit  
**Kind**: struct

An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
struct NavigationResponse
```

#### Overview

A `NavigationResponse` value is intended to be used to make policy decisions about whether to allow navigation within a web page via a `NavigationDeciding`.

## Topics

### Instance Properties
- [var canShowMimeType: Bool](webpage/navigationresponse/canshowmimetype.md)
  Indicates whether WebKit is capable of displaying the response’s MIME type natively.
- [var response: URLResponse](webpage/navigationresponse/response.md)
  The frame’s response.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NavigationDeciding](webpage/navigationdeciding.md)
  Allows providing custom behavior to handle navigation changes and to coordinate these changes for the web page’s main page.
- [WebPage.NavigationAction](webpage/navigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [WebPage.NavigationPreferences](webpage/navigationpreferences.md)
  A type that specifies the behaviors to use when loading and rendering page content.
- [WebPage.FrameInfo](webpage/frameinfo.md)
  A type that contains information about a frame on a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationresponse)*