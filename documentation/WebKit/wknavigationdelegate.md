# WKNavigationDelegate

**Framework**: WebKit  
**Kind**: protocol

Methods for accepting or rejecting navigation changes, and for tracking the progress of navigation requests.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol WKNavigationDelegate : NSObjectProtocol
```

## Mentions

- [Replacing UIWebView in your app](replacing-uiwebview-in-your-app.md)

#### Overview

Implement the methods of the [`WKNavigationDelegate`](wknavigationdelegate.md) protocol in the object you use to coordinate changes in your web view’s main frame. As the user attempts to navigate web content, the web view coordinates with its navigation delegate to manage any transitions. For example, you might use these methods to restrict navigation from specific links within your content. You might also use them to track the progress of requests, and to respond to errors and authentication challenges.

## Topics

### Allowing or denying navigation requests
- [func webView(WKWebView, decidePolicyFor: WKNavigationAction, preferences: WKWebpagePreferences, decisionHandler: (WKNavigationActionPolicy, WKWebpagePreferences) -> Void)](wknavigationdelegate/webview(_:decidepolicyfor:preferences:decisionhandler:).md)
  Asks the delegate for permission to navigate to new content based on the specified preferences and action information.
- [func webView(WKWebView, decidePolicyFor: WKNavigationAction, decisionHandler: (WKNavigationActionPolicy) -> Void)](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-2ni62.md)
  Asks the delegate for permission to navigate to new content based on the specified action information.
- [enum WKNavigationActionPolicy](wknavigationactionpolicy.md)
  Constants that indicate whether to allow or cancel navigation to a webpage from an action.
- [func webView(WKWebView, decidePolicyFor: WKNavigationResponse, decisionHandler: (WKNavigationResponsePolicy) -> Void)](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-19mn2.md)
  Asks the delegate for permission to navigate to new content after the response to the navigation request is known.
- [enum WKNavigationResponsePolicy](wknavigationresponsepolicy.md)
  Constants that indicate whether to allow or cancel navigation to a webpage from a response.
### Tracking the load progress of a request
- [func webView(WKWebView, didStartProvisionalNavigation: WKNavigation!)](wknavigationdelegate/webview(_:didstartprovisionalnavigation:).md)
  Tells the delegate that navigation from the main frame has started.
- [func webView(WKWebView, didReceiveServerRedirectForProvisionalNavigation: WKNavigation!)](wknavigationdelegate/webview(_:didreceiveserverredirectforprovisionalnavigation:).md)
  Tells the delegate that the web view received a server redirect for a request.
- [func webView(WKWebView, didCommit: WKNavigation!)](wknavigationdelegate/webview(_:didcommit:).md)
  Tells the delegate that the web view has started to receive content for the main frame.
- [func webView(WKWebView, didFinish: WKNavigation!)](wknavigationdelegate/webview(_:didfinish:).md)
  Tells the delegate that navigation is complete.
### Responding to authentication challenges
- [func webView(WKWebView, didReceive: URLAuthenticationChallenge, completionHandler: (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)](wknavigationdelegate/webview(_:didreceive:completionhandler:).md)
  Asks the delegate to respond to an authentication challenge.
- [func webView(WKWebView, authenticationChallenge: URLAuthenticationChallenge, shouldAllowDeprecatedTLS: (Bool) -> Void)](wknavigationdelegate/webview(_:authenticationchallenge:shouldallowdeprecatedtls:).md)
  Asks the delegate whether to continue with a connection that uses a deprecated version of TLS.
### Responding to navigation errors
- [func webView(WKWebView, didFail: WKNavigation!, withError: any Error)](wknavigationdelegate/webview(_:didfail:witherror:).md)
  Tells the delegate that an error occurred during navigation.
- [func webView(WKWebView, didFailProvisionalNavigation: WKNavigation!, withError: any Error)](wknavigationdelegate/webview(_:didfailprovisionalnavigation:witherror:).md)
  Tells the delegate that an error occurred during the early navigation process.
- [func webViewWebContentProcessDidTerminate(WKWebView)](wknavigationdelegate/webviewwebcontentprocessdidterminate(_:).md)
  Tells the delegate that the web view’s content process was terminated.
### Handling download progress
- [func webView(WKWebView, navigationResponse: WKNavigationResponse, didBecome: WKDownload)](wknavigationdelegate/webview(_:navigationresponse:didbecome:).md)
  Tells the delegate that a navigation response became a download.
- [func webView(WKWebView, navigationAction: WKNavigationAction, didBecome: WKDownload)](wknavigationdelegate/webview(_:navigationaction:didbecome:).md)
  Tells the delegate that a navigation action became a download.
### Instance Methods
- [func webView(WKWebView, shouldGoTo: WKBackForwardListItem, willUseInstantBack: Bool, completionHandler: (Bool) -> Void)](wknavigationdelegate/webview(_:shouldgoto:willuseinstantback:completionhandler:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKBackForwardList](wkbackforwardlist.md)
  An object that manages the list of previously loaded webpages, which the web view uses for forward and backward navigation.
- [class WKBackForwardListItem](wkbackforwardlistitem.md)
  A representation of a webpage that the web view previously visited.
- [class WKNavigation](wknavigation.md)
  An object that tracks the loading progress of a webpage.
- [class WKNavigationAction](wknavigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [class WKNavigationResponse](wknavigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate)*