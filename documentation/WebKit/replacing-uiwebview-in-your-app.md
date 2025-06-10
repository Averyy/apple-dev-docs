# Replacing UIWebView in your app

**Framework**: WebKit

Find a suitable alternative to handle your app’s web content.

#### Overview

If your app is using [`UIWebView`](https://developer.apple.com/documentation/UIKit/UIWebView), you need to replace it with another Apple technology, because this class is now deprecated. Choose among several technologies, based on your app’s functionality and the degree of configurability you need. This article explores some alternatives and specifically the configuration and architectural changes of [`WKWebView`](wkwebview.md).

##### Consider Alternative Technologies

Before beginning a migration away from [`UIWebView`](https://developer.apple.com/documentation/UIKit/UIWebView), consider whether it can be replaced with other tools. Apple has a variety of technologies that can replace a web view to accomplish similar functionality, and possibly a richer feature set with less code.

If you need an in-app web browser and don’t need deep customization of that experience, [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) is a good choice. It handles all the features you’d need to implement in a basic browser and more.

If you need to authenticate your users, use [`ASWebAuthenticationSession`](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession).

If you need to display maps or map tiles, consider using [`MKMapView`](https://developer.apple.com/documentation/MapKit/MKMapView).

##### Update to Wkwebview

If you need a high degree of configurability or are using web content in ways unrelated to browsing, use [`WKWebView`](wkwebview.md).

[`WKWebView`](wkwebview.md) isn’t a drop-in replacement for [`UIWebView`](https://developer.apple.com/documentation/UIKit/UIWebView). It has a different architecture that requires rethinking how you use web views, as well as code changes to implement its functionality. You may not be able to implement some features in [`WKWebView`](wkwebview.md).

##### Implement Delegates for Functionality

[`WKWebView`](wkwebview.md) uses various delegates to implement functionality that’s similar to [`UIWebViewDelegate`](https://developer.apple.com/documentation/UIKit/UIWebViewDelegate). The table below shows the [`UIWebViewDelegate`](https://developer.apple.com/documentation/UIKit/UIWebViewDelegate) methods and their [`WKWebView`](wkwebview.md) equivalents in the [`WKNavigationDelegate`](wknavigationdelegate.md) column.

| `UIWebViewDelegate` | `WKNavigationDelegate` |
| --- | --- |
| [`webViewDidStartLoad(_:)`](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/1617947-webviewdidstartload) | [`webView(_:didStartProvisionalNavigation:)`](wknavigationdelegate/webview(_:didstartprovisionalnavigation:).md) |
| [`webViewDidFinishLoad(_:)`](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/1617969-webviewdidfinishload) | [`webView(_:didFinish:)`](wknavigationdelegate/webview(_:didfinish:).md) |
| [`webView(_:didFailLoadWithError:)`](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/1617970-webview) | [`webView(_:didFailProvisionalNavigation:withError:)`](wknavigationdelegate/webview(_:didfailprovisionalnavigation:witherror:).md) or [`webView(_:didFail:withError:)`](wknavigationdelegate/webview(_:didfail:witherror:).md) |
| [`webView(_:shouldStartLoadWith:navigationType:)`](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/1617945-webview) | [`webView(_:decidePolicyFor:decisionHandler:)`](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-2ni62.md) or [`webView(_:decidePolicyFor:decisionHandler:)`](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-19mn2.md) |
| [`connection(_:didReceive:)`](https://developer.apple.com/documentation/Foundation/NSURLConnectionDelegate/connection(_:didReceive:)) | [`webView(_:didReceive:completionHandler:)`](wknavigationdelegate/webview(_:didreceive:completionhandler:).md) |

> **Note**:  The [`webView(_:decidePolicyFor:decisionHandler:)`](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-2ni62.md) function doesn’t return a Boolean as its [`UIWebView`](https://developer.apple.com/documentation/UIKit/UIWebView) counterpart did; it uses the `decisionHandler` to return an [`WKNavigationActionPolicy.allow`](wknavigationactionpolicy/allow.md) or [`WKNavigationActionPolicy.cancel`](wknavigationactionpolicy/cancel.md) value.

##### Plan for Architectural Changes

One major architectural difference between [`UIWebView`](https://developer.apple.com/documentation/UIKit/UIWebView) and [`WKWebView`](wkwebview.md) is that the methods of [`WKWebView`](wkwebview.md) tend to be asynchronous, while the methods of [`UIWebView`](https://developer.apple.com/documentation/UIKit/UIWebView) were synchronous.

This difference requires code and architecture changes in your app. Another major change relates to creating single sign on (SSO) functionality. Cookie restrictions across the entire [`WKWebView`](wkwebview.md) landscape, mean SSO functionality in [`WKWebView`](wkwebview.md) isn’t supported for third-party cookies and clients should use a token-based authentication system like OAuth for SSO. Third-party cookies are cookies for a domain other than the domain for which the context was loaded. APIs in the [`Authentication Services`](https://developer.apple.com/documentation/AuthenticationServices) framework are specifically built to do this.

## See Also

- [Viewing Desktop or Mobile Web Content Using a Web View](viewing-desktop-or-mobile-web-content-using-a-web-view.md)
  Implement a simple iPad web browser that can view either the desktop or mobile version of a website.
- [class WKWebView](wkwebview.md)
  An object that displays interactive web content, such as for an in-app browser.
- [protocol WKUIDelegate](wkuidelegate.md)
  The methods for presenting native user interface elements on behalf of a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/replacing-uiwebview-in-your-app)*