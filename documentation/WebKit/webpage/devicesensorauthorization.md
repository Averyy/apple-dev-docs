# WebPage.DeviceSensorAuthorization

**Framework**: WebKit  
**Kind**: struct

A type that describes the authorization permissions policy for the device’s sensors a web resource may access.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct DeviceSensorAuthorization
```

## Topics

### Initializers
- [init(decision: WKPermissionDecision)](webpage/devicesensorauthorization/init(decision:).md)
  A convenience initializer to create a DeviceSensorAuthorization that always uses the same permission decision.
- [init(decisionHandler: (WebPage.DeviceSensorAuthorization.Permission, WebPage.FrameInfo, WKSecurityOrigin) async -> WKPermissionDecision)](webpage/devicesensorauthorization/init(decisionhandler:).md)
  Creates a new `DeviceSensorAuthorization` using the specified policy.
### Enumerations
- [WebPage.DeviceSensorAuthorization.Permission](webpage/devicesensorauthorization/permission.md)
  The kind of sensor permission a web resource may request to access.

## See Also

- [WebPage.Configuration](webpage/configuration.md)
  A configuration type that specifies the preferences and behaviors of a webpage.
- [struct URLScheme](urlscheme.md)
  A type representing a valid URL scheme.
- [protocol URLSchemeHandler](urlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [enum URLSchemeTaskResult](urlschemetaskresult.md)
  A value used as part of a sequence of results from a [`URLSchemeHandler`](urlschemehandler.md), which can either be a `Data` or a `URLResponse`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/devicesensorauthorization)*