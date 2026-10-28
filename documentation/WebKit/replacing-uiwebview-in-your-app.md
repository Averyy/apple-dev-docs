# Replacing UIWebView in your app

**Framework**: WebKit  
**Role**: Article

Find a suitable alternative to handle your app’s web content.

## Overview

If your app is using [`UIWebView`](../UIKit/uiwebview.md), you need to replace it with another Apple technology, because this class is now deprecated. Choose among several technologies, based on your app’s functionality and the degree of configurability you need. This article explores some alternatives and specifically the configuration and architectural changes of [`WKWebView`](./wkwebview.md).

### Consider alternative technologies

Before beginning a migration away from [`UIWebView`](../UIKit/uiwebview.md), consider whether it can be replaced with other tools. Apple has a variety of technologies that can replace a web view to accomplish similar functionality, and possibly a richer feature set with less code.

If you need an in-app web browser and don’t need deep customization of that experience, [`SFSafariViewController`](../SafariServices/sfsafariviewcontroller.md) is a good choice. It handles all the features you’d need to implement in a basic browser and more.

If you need to authenticate your users, use [`ASWebAuthenticationSession`](../AuthenticationServices/aswebauthenticationsession.md).

If you need to display maps or map tiles, consider using [`MKMapView`](../MapKit/mkmapview.md).

### Update to WKWebView

If you need a high degree of configurability or are using web content in ways unrelated to browsing, use [`WKWebView`](./wkwebview.md).

[`WKWebView`](./wkwebview.md) isn’t a drop-in replacement for [`UIWebView`](../UIKit/uiwebview.md). It has a different architecture that requires rethinking how you use web views, as well as code changes to implement its functionality. You may not be able to implement some features in [`WKWebView`](./wkwebview.md).

### Implement delegates for functionality

[`WKWebView`](./wkwebview.md) uses various delegates to implement functionality that’s similar to [`UIWebViewDelegate`](../UIKit/uiwebviewdelegate.md). The table below shows the [`UIWebViewDelegate`](../UIKit/uiwebviewdelegate.md) methods and their [`WKWebView`](./wkwebview.md) equivalents in the [`WKNavigationDelegate`](./wknavigationdelegate.md) column.

| `UIWebViewDelegate` | `WKNavigationDelegate` |
| --- | --- |
| [`webViewDidStartLoad(_:)`](../UIKit/uiwebviewdelegate/webviewdidstartload%28_%29.md) | [`webView(_:didStartProvisionalNavigation:)`](./wknavigationdelegate/webview%28_,didstartprovisionalnavigation%29.md) |
| [`webViewDidFinishLoad(_:)`](../UIKit/uiwebviewdelegate/webviewdidfinishload%28_%29.md) | [`webView(_:didFinish:)`](./wknavigationdelegate/webview%28_,didfinish%29.md) |
| [`webView(_:didFailLoadWithError:)`](../UIKit/uiwebviewdelegate/webview%28_,didfailloadwitherror%29.md) | [`webView(_:didFailProvisionalNavigation:withError:)`](./wknavigationdelegate/webview%28_,didfailprovisionalnavigation,witherror%29.md) or [`webView(_:didFail:withError:)`](./wknavigationdelegate/webview%28_,didfail,witherror%29.md) |
| [`webView(_:shouldStartLoadWith:navigationType:)`](../UIKit/uiwebviewdelegate/webview%28_,shouldstartloadwith,navigationtype%29.md) | [`webView(_:decidePolicyFor:decisionHandler:)`](./wknavigationdelegate/webview%28_,decidepolicyfor,decisionhandler%29-2ni62.md) or [`webView(_:decidePolicyFor:decisionHandler:)`](./wknavigationdelegate/webview%28_,decidepolicyfor,decisionhandler%29-19mn2.md) |
| [`connection(_:didReceive:)`](../Foundation/nsurlconnectiondelegate/connection%28_,didreceive%29.md) | [`webView(_:didReceive:completionHandler:)`](./wknavigationdelegate/webview%28_,didreceive,completionhandler%29.md) |

> **Note**:  The [`webView(_:decidePolicyFor:decisionHandler:)`](./wknavigationdelegate/webview%28_,decidepolicyfor,decisionhandler%29-2ni62.md) function doesn’t return a Boolean as its [`UIWebView`](../UIKit/uiwebview.md) counterpart did; it uses the `decisionHandler` to return an [`WKNavigationActionPolicy.allow`](./wknavigationactionpolicy/allow.md) or [`WKNavigationActionPolicy.cancel`](./wknavigationactionpolicy/cancel.md) value.

### Plan for architectural changes

One major architectural difference between [`UIWebView`](../UIKit/uiwebview.md) and [`WKWebView`](./wkwebview.md) is that the methods of [`WKWebView`](./wkwebview.md) tend to be asynchronous, while the methods of [`UIWebView`](../UIKit/uiwebview.md) were synchronous.

This difference requires code and architecture changes in your app. Another major change relates to creating single sign on (SSO) functionality. Cookie restrictions across the entire [`WKWebView`](./wkwebview.md) landscape, mean SSO functionality in [`WKWebView`](./wkwebview.md) isn’t supported for third-party cookies and clients should use a token-based authentication system like OAuth for SSO. Third-party cookies are cookies for a domain other than the domain for which the context was loaded. APIs in the [Authentication Services](../AuthenticationServices/AuthenticationServices.md) framework are specifically built to do this.

## See Also

### Web views
- [Viewing Desktop or Mobile Web Content Using a Web View](./viewing-desktop-or-mobile-web-content-using-a-web-view.md)
  Implement a simple iPad web browser that can view either the desktop or mobile version of a website.
- [class WKWebView](./wkwebview.md)
  An object that displays interactive web content, such as for an in-app browser.
- [protocol WKUIDelegate](./wkuidelegate.md)
  The methods for presenting native user interface elements on behalf of a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/replacing-uiwebview-in-your-app)*