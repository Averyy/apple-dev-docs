# WKURLSchemeHandler

**Framework**: WebKit  
**Kind**: protocol

A protocol for loading resources with URL schemes that WebKit doesn’t handle.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol WKURLSchemeHandler : NSObjectProtocol
```

#### Overview

Adopt the [`WKURLSchemeHandler`](wkurlschemehandler.md) protocol in objects that handle custom URL schemes for your web content. Custom schemes let you integrate custom resource types into your web content, and you may define custom schemes for resources that your app requires. For example, you might use a custom scheme to integrate content that is available only on the user’s device, such as the user’s photos. Adopt this protocol in one of your app’s objects and register it using the [`setURLSchemeHandler(_:forURLScheme:)`](wkwebviewconfiguration/seturlschemehandler(_:forurlscheme:).md) method of [`WKWebViewConfiguration`](wkwebviewconfiguration.md).

When a web view encounters a resource that uses a custom scheme, it creates a [`WKURLSchemeTask`](wkurlschemetask.md) object and passes it to the methods of your scheme handler object. Use the [`webView(_:start:)`](wkurlschemehandler/webview(_:start:).md) method to begin loading the resource. While your handler loads the object, the web view may call your handler’s [`webView(_:stop:)`](wkurlschemehandler/webview(_:stop:).md) method to notify you that the resource is no longer needed.

## Topics

### Loading a Custom Resource
- [func webView(WKWebView, start: any WKURLSchemeTask)](wkurlschemehandler/webview(_:start:).md)
  Asks your handler to begin loading the data for the specified resource.
### Responding to a Canceled Resource Request
- [func webView(WKWebView, stop: any WKURLSchemeTask)](wkurlschemehandler/webview(_:stop:).md)
  Asks your handler to stop loading the data for the specified resource.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKWebsiteDataStore](wkwebsitedatastore.md)
  An object that manages cookies, disk and memory caches, and other types of data for a web view.
- [class WKWebsiteDataRecord](wkwebsitedatarecord.md)
  A record of the data that a particular website stores persistently.
- [class WKHTTPCookieStore](wkhttpcookiestore.md)
  An object that manages the HTTP cookies associated with a particular web view.
- [protocol WKURLSchemeTask](wkurlschemetask.md)
  An interface that WebKit uses to request custom resources from your app.
- [static let readAccessURL: NSAttributedString.DocumentReadingOptionKey](../Foundation/NSAttributedString/DocumentReadingOptionKey/readAccessURL.md)
  The local files WebKit can access when loading content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkurlschemehandler)*