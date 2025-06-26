# URLSchemeHandler

**Framework**: WebKit  
**Kind**: protocol

A protocol for loading resources with URL schemes that WebKit doesn’t handle.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
protocol URLSchemeHandler
```

#### Overview

Adopt the `URLSchemeHandler` protocol in types that handle custom URL schemes for your web content. Custom schemes let you integrate custom resource types into your web content, and you may define custom schemes for resources that your app requires. For example, you might use a custom scheme to integrate content that is available only on the user’s device, such as the user’s photos. These types can then be registered to a particular WebPage by using the [`urlSchemeHandlers`](webpage/configuration/urlschemehandlers.md) property of [`WebPage.Configuration`](webpage/configuration.md).

When a web page encounters a resource that uses a custom scheme, it passes the `URLRequest` to the scheme handler, and expects a stream of responses and data to load the result.

If WebKit determines that it no longer needs a resource that your handler is loading, it will cancel the Task responsible for the async sequence. Typically, this may happen when the user navigates to another page, but may happen for other reasons.

## Topics

### Associated Types
- [associatedtype TaskSequence : AsyncSequence](urlschemehandler/tasksequence.md)
  The type of sequence produced by the handler.
### Instance Methods
- [func reply(for: URLRequest) -> Self.TaskSequence](urlschemehandler/reply(for:).md)
  Produces a sequence of intermixed responses and data to load a resource for a given request.

## See Also

- [WebPage.Configuration](webpage/configuration.md)
  A configuration type that specifies the preferences and behaviors of a webpage.
- [WebPage.DeviceSensorAuthorization](webpage/devicesensorauthorization.md)
  A type that describes the authorization permissions policy for the device’s sensors a web resource may access.
- [struct URLScheme](urlscheme.md)
  A type representing a valid URL scheme.
- [enum URLSchemeTaskResult](urlschemetaskresult.md)
  A value used as part of a sequence of results from a [`URLSchemeHandler`](urlschemehandler.md), which can either be a `Data` or a `URLResponse`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/urlschemehandler)*