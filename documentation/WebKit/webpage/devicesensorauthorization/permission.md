# WebPage.DeviceSensorAuthorization.Permission

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

The kind of sensor permission a web resource may request to access.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Permission
```

## Topics

### Enumeration Cases
- [WebPage.DeviceSensorAuthorization.Permission.deviceOrientationAndMotion](./permission/deviceorientationandmotion.md)
  The orientation and motion of the device.
- [WebPage.DeviceSensorAuthorization.Permission.mediaCapture(_:)](./permission/mediacapture%28_%29.md)
  A media capture device, like a microphone or camera.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Configuring a WebPage
- [WebPage.Configuration](../configuration.md)
  A configuration type that specifies the preferences and behaviors of a webpage.
- [WebPage.DeviceSensorAuthorization](../devicesensorauthorization.md)
  A type that describes the authorization permissions policy for the device’s sensors a web resource may access.
- [struct URLScheme](../../urlscheme.md)
  A type representing a valid URL scheme.
- [protocol URLSchemeHandler](../../urlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [enum URLSchemeTaskResult](../../urlschemetaskresult.md)
  A value used as part of a sequence of results from a [`URLSchemeHandler`](../../urlschemehandler.md), which can either be a `Data` or a `URLResponse`.
- [WebPage.Configuration.MediaPlaybackBehavior](../configuration/mediaplaybackbehavior-swift.enum.md)
  The behavior used when playing HTML video within a page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/devicesensorauthorization/permission)*