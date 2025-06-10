# WebPage.NavigationDeciding

**Framework**: WebKit  
**Kind**: protocol

Allows providing custom behavior to handle navigation changes and to coordinate these changes for the web page’s main page.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
protocol NavigationDeciding
```

#### Overview

For example, you might use these methods to restrict navigation from specific links within your content.

## Topics

### Instance Methods
- [func decideAuthenticationChallengeDisposition(for: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)](webpage/navigationdeciding/decideauthenticationchallengedisposition(for:).md)
  Determines the response to an authentication challenge.
- [func decidePolicy(for: WebPage.NavigationResponse) async -> WKNavigationResponsePolicy](webpage/navigationdeciding/decidepolicy(for:).md)
  Determines permission to navigate to new content after the response to the navigation request is known.
- [func decidePolicy(for: WebPage.NavigationAction, preferences: inout WebPage.NavigationPreferences) async -> WKNavigationActionPolicy](webpage/navigationdeciding/decidepolicy(for:preferences:).md)
  Determines permission to navigate to new content based on the specified preferences and action information.

## See Also

- [WebPage.NavigationAction](webpage/navigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [WebPage.NavigationResponse](webpage/navigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [WebPage.NavigationPreferences](webpage/navigationpreferences.md)
  A type that specifies the behaviors to use when loading and rendering page content.
- [WebPage.FrameInfo](webpage/frameinfo.md)
  A type that contains information about a frame on a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationdeciding)*