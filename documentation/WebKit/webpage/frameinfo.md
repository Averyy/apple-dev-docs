# WebPage.FrameInfo

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

A type that contains information about a frame on a webpage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
struct FrameInfo
```

## Topics

### Instance Properties
- [var isMainFrame: Bool](./frameinfo/ismainframe.md)
  Indicates whether the frame is the web site’s main frame or a subframe.
- [var request: URLRequest](./frameinfo/request.md)
  The frame’s current request.
- [var securityOrigin: WKSecurityOrigin](./frameinfo/securityorigin.md)
  The frame’s security origin.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing navigation between webpages
- [protocol NavigationDeciding](./navigationdeciding.md)
  Allows providing custom behavior to handle navigation changes and to coordinate these changes for the web page’s main page.
- [WebPage.NavigationAction](./navigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [WebPage.NavigationResponse](./navigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [WebPage.NavigationPreferences](./navigationpreferences.md)
  A type that specifies the behaviors to use when loading and rendering page content.
- [WebPage.NavigationPreferences.ContentMode](./navigationpreferences/contentmode.md)
  Options to indicate how to render web view content.
- [WebPage.NavigationPreferences.UpgradeToHTTPSPolicy](./navigationpreferences/upgradetohttpspolicy.md)
  Preference for loading a webpage with HTTPS, and how failures should be handled.
- [WebPage.NavigationPreferences.SecurityRestrictionMode](./navigationpreferences/securityrestrictionmode-swift.enum.md)
  Security restriction modes for WebView content.
- [WebPage.FormInfo](./forminfo.md)
  A type that contains information about a form submission from a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/frameinfo)*