# WebKit for SwiftUI

**Framework**: WebKit

Integrate web content into your SwiftUI apps with new standard views you connect to webpages.

#### Overview

Present web content in your SwiftUI app with WebKit for SwiftUI. Use WebKit features to observe content and customize the web browsing and display experience.

Create a [`WebView`](webview-swift.struct.md) with a [`URL`](https://developer.apple.com/documentation/Foundation/URL) to display your web content. Apply view modifiers for various customizations, like displaying a find navigator, customizing scrolling behavior, configuring gesture behavior, and more.

Connect [`WebView`](webview-swift.struct.md) to a [`WebPage`](webpage.md) to interact with and react to changes in web content, such as observing navigation progress and calling JavaScript. You can use [`WebPage`](webpage.md) by itself when you don’t need to display the content directly.

## Topics

### Essentials
- [struct WebView](webview-swift.struct.md)
  A view that displays some web content.
- [class WebPage](webpage.md)
  An object that controls and manages the behavior of interactive web content.
### Managing navigation between webpages
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
### Observing navigation between webpages
- [WebPage.BackForwardList](webpage/backforwardlist-swift.struct.md)
  An observable representation of a webpage’s navigations.
- [WebPage.NavigationID](webpage/navigationid.md)
  An opaque identifier which can be used to uniquely identify a load request for a web page.
- [WebPage.NavigationEvent](webpage/navigationevent.md)
  A particular state that occurs during the progression of a navigation.
### Configuring a WebPage
- [WebPage.Configuration](webpage/configuration.md)
- [WebPage.DeviceSensorAuthorization](webpage/devicesensorauthorization.md)
  A type that describes the authorization permissions policy for the device’s sensors a web resource may access.
- [struct URLScheme](urlscheme.md)
  A type representing a valid URL scheme.
- [protocol URLSchemeHandler](urlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [enum URLSchemeTaskResult](urlschemetaskresult.md)

## See Also

- [WebKit for AppKit and UIKit](webkit-for-appkit-and-uikit.md)
  Display web content in AppKit or UIKit apps, or apps built with Objective-C.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webkit-for-swiftui)*