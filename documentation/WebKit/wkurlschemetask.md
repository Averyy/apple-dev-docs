# WKURLSchemeTask

**Framework**: WebKit  
**Kind**: protocol

An interface that WebKit uses to request custom resources from your app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
protocol WKURLSchemeTask : NSObjectProtocol
```

#### Overview

The [`WKURLSchemeTask`](wkurlschemetask.md) protocol defines an interface that WebKit uses to request custom resources. You don’t adopt this interface in your own objects. Instead, WebKit creates objects that adopt this interface and delivers them to your custom scheme handlers — that is, objects that adopt the [`WKURLSchemeHandler`](wkurlschemehandler.md) protocol. You use the objects that WebKit provides to get information about the requested resources and load them. You also use those objects to report your progress back to WebKit.

When WebKit needs a custom scheme, it places an appropriate URL request in the task’s [`request`](wkurlschemetask/request.md) property. Upon receiving the request, determine the size of the resource and call the [`didReceive(_:)`](wkurlschemetask/didreceive(_:)-2u23r.md) method with an appropriate URL response object. Providing a response mirrors the behavior that a web server performs when it receives a request.

After you load some portion of the resource data, call the [`didReceive(_:)`](wkurlschemetask/didreceive(_:)-8t5f8.md) method to send it to WebKit. You may call that method multiple times to deliver data incrementally, or call it once with all of the data. After you finish delivering all of the data, call the [`didFinish()`](wkurlschemetask/didfinish().md) method. If an error occurs at any point during the load process, call [`didFailWithError(_:)`](wkurlschemetask/didfailwitherror(_:).md) to report it.

## Topics

### Getting the URL of the Requested Resource
- [var request: URLRequest](wkurlschemetask/request.md)
  Information about the resource to load.
### Reporting Progress Back to WebKit
- [func didReceive(URLResponse)](wkurlschemetask/didreceive(_:)-2u23r.md)
  Returns a URL response to WebKit with information about the requested resource.
- [func didReceive(Data)](wkurlschemetask/didreceive(_:)-8t5f8.md)
  Sends some or all of the resource data to WebKit.
- [func didFinish()](wkurlschemetask/didfinish.md)
  Signals the successful completion of the task.
### Reporting an Error to WebKit
- [func didFailWithError(any Error)](wkurlschemetask/didfailwitherror(_:).md)
  Completes the task and reports the specified error back to WebKit.

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
- [protocol WKURLSchemeHandler](wkurlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [static let readAccessURL: NSAttributedString.DocumentReadingOptionKey](../Foundation/NSAttributedString/DocumentReadingOptionKey/readAccessURL.md)
  The local files WebKit can access when loading content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkurlschemetask)*