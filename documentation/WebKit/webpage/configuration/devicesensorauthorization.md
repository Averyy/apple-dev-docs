# deviceSensorAuthorization

**Framework**: WebKit  
**Kind**: property

Allows specifying how web resources may access device sensors.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
var deviceSensorAuthorization: WebPage.DeviceSensorAuthorization
```

#### Discussion

The default implementation returns `WKPermissionDecision.prompt` for all requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/devicesensorauthorization)*