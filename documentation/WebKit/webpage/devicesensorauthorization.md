# WebPage.DeviceSensorAuthorization

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

A type that describes the authorization permissions policy for the device’s sensors a web resource may access.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DeviceSensorAuthorization
```

## Topics

### Initializers
- [init(decision: WKPermissionDecision)](./devicesensorauthorization/init%28decision%29.md)
  A convenience initializer to create a DeviceSensorAuthorization that always uses the same permission decision.
- [init(decisionHandler: (WebPage.DeviceSensorAuthorization.Permission, WebPage.FrameInfo, WKSecurityOrigin) async -> WKPermissionDecision)](./devicesensorauthorization/init%28decisionhandler%29.md)
  Creates a new `DeviceSensorAuthorization` using the specified policy.
### Enumerations
- [WebPage.DeviceSensorAuthorization.Permission](./devicesensorauthorization/permission.md)
  The kind of sensor permission a web resource may request to access.

## See Also

### Configuring a WebPage
- [WebPage.Configuration](./configuration.md)
  A configuration type that specifies the preferences and behaviors of a webpage.
- [struct URLScheme](../urlscheme.md)
  A type representing a valid URL scheme.
- [protocol URLSchemeHandler](../urlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [enum URLSchemeTaskResult](../urlschemetaskresult.md)
  A value used as part of a sequence of results from a [`URLSchemeHandler`](../urlschemehandler.md), which can either be a `Data` or a `URLResponse`.
- [WebPage.Configuration.MediaPlaybackBehavior](./configuration/mediaplaybackbehavior-swift.enum.md)
  The behavior used when playing HTML video within a page.
- [WebPage.DeviceSensorAuthorization.Permission](./devicesensorauthorization/permission.md)
  The kind of sensor permission a web resource may request to access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/devicesensorauthorization)*