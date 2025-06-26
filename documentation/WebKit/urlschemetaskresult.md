# URLSchemeTaskResult

**Framework**: WebKit  
**Kind**: enum

A value used as part of a sequence of results from a [`URLSchemeHandler`](urlschemehandler.md), which can either be a `Data` or a `URLResponse`.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
enum URLSchemeTaskResult
```

## Topics

### Enumeration Cases
- [URLSchemeTaskResult.data(_:)](urlschemetaskresult/data(_:).md)
  Data for the resource. This value may contain all of the data or only some of it.
- [URLSchemeTaskResult.response(_:)](urlschemetaskresult/response(_:).md)
  The response to return to WebKit. The response value must include the MIME type of the request resource.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WebPage.Configuration](webpage/configuration.md)
  A configuration type that specifies the preferences and behaviors of a webpage.
- [WebPage.DeviceSensorAuthorization](webpage/devicesensorauthorization.md)
  A type that describes the authorization permissions policy for the device’s sensors a web resource may access.
- [struct URLScheme](urlscheme.md)
  A type representing a valid URL scheme.
- [protocol URLSchemeHandler](urlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/urlschemetaskresult)*