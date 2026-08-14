# WebPage.FormInfo

**Framework**: WebKit  
**Kind**: struct

A type that contains information about a form submission from a webpage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
struct FormInfo
```

## Topics

### Instance Properties
- [var formValues: [String : String]](webpage/forminfo/formvalues.md)
  A dictionary of the form values that will be submitted during the navigation.
- [var httpMethod: String](webpage/forminfo/httpmethod.md)
  The HTTP method used to submit the form; generally either @“GET” or @“POST”.
- [var sourceFrame: WebPage.FrameInfo](webpage/forminfo/sourceframe.md)
  The frame that caused the form submission.
- [var submissionURL: URL](webpage/forminfo/submissionurl.md)
  The URL that the frame is being navigated to.
- [var targetFrame: WebPage.FrameInfo](webpage/forminfo/targetframe.md)
  The frame where the form is being submitted will cause a navigation.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol NavigationDeciding](webpage/navigationdeciding.md)
  Allows providing custom behavior to handle navigation changes and to coordinate these changes for the web page’s main page.
- [WebPage.NavigationAction](webpage/navigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [WebPage.NavigationResponse](webpage/navigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [WebPage.NavigationPreferences](webpage/navigationpreferences.md)
  A type that specifies the behaviors to use when loading and rendering page content.
- [WebPage.FrameInfo](webpage/frameinfo.md)
  A type that contains information about a frame on a webpage.
- [WebPage.NavigationPreferences.ContentMode](webpage/navigationpreferences/contentmode.md)
  Options to indicate how to render web view content.
- [WebPage.NavigationPreferences.UpgradeToHTTPSPolicy](webpage/navigationpreferences/upgradetohttpspolicy.md)
  Preference for loading a webpage with HTTPS, and how failures should be handled.
- [WebPage.NavigationPreferences.SecurityRestrictionMode](webpage/navigationpreferences/securityrestrictionmode-swift.enum.md)
  Security restriction modes for WebView content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/forminfo)*