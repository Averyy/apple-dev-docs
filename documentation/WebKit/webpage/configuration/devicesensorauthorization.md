# deviceSensorAuthorization

**Framework**: WebKit  
**Kind**: property

Allows specifying how web resources may access device sensors.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var deviceSensorAuthorization: WebPage.DeviceSensorAuthorization
```

#### Discussion

The default implementation returns `WKPermissionDecision.prompt` for all requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/devicesensorauthorization)*