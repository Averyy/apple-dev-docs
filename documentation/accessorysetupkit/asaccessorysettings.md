# ASAccessorySettings

**Framework**: AccessorySetupKit  
**Kind**: class

Properties of an accessory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
class ASAccessorySettings
```

## Topics

### Applying default settings
- [class var `default`: ASAccessorySettings](asaccessorysettings/default.md)
  An empty settings object.
### Inspecting accessory settings
- [var ssid: String?](asaccessorysettings/ssid.md)
  A hotspot identifier that clients can use to connect to an accessory’s hotspot.
- [var bluetoothTransportBridgingIdentifier: Data?](asaccessorysettings/bluetoothtransportbridgingidentifier.md)
  A 6-byte identifier for bridging classic transport profiles.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func finishAuthorization(for: ASAccessory, settings: ASAccessorySettings, completionHandler: ((any Error)?) -> Void)](asaccessorysession/finishauthorization(for:settings:completionhandler:).md)
  Finish authorization of a partially-setup accessory.
- [func failAuthorization(for: ASAccessory, completionHandler: ((any Error)?) -> Void)](asaccessorysession/failauthorization(for:completionhandler:).md)
  End authorization of a partially-configured accessory as a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysettings)*