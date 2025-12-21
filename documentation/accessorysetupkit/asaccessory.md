# ASAccessory

**Framework**: AccessorySetupKit  
**Kind**: class

An accessory discovered by the accessory session.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
class ASAccessory
```

## Topics

### Accessing identifiers
- [var bluetoothIdentifier: UUID?](asaccessory/bluetoothidentifier.md)
  The accessory’s unique Bluetooth identifier, if any.
- [var bluetoothTransportBridgingIdentifier: Data?](asaccessory/bluetoothtransportbridgingidentifier.md)
  The accessory’s Bluetooth identifier, if any, for use when bridging classic transport profiles.
- [var ssid: String?](asaccessory/ssid.md)
  The accessory’s Wi-Fi SSID, if any.
### Presenting a display name
- [var displayName: String](asaccessory/displayname.md)
  The accessory’s name, suitable for displaying to someone using your app.
### Inspecting the accessory’s descriptor
- [var descriptor: ASDiscoveryDescriptor](asaccessory/descriptor.md)
  The descriptor used to discover the accessory.
### Inspecting accessory state
- [var state: ASAccessory.AccessoryState](asaccessory/state.md)
  The current authorization state of the accessory.
- [ASAccessory.AccessoryState](asaccessory/accessorystate.md)
  An enumeration of possible authorization states of an accessory.
### Working with Wi-Fi Aware
- [var wifiAwarePairedDeviceID: ASAccessory.WiFiAwarePairedDeviceID](asaccessory/wifiawarepaireddeviceid-swift.property.md)
  The accessory’s Wi-Fi Aware Pairing Identifier.
- [ASAccessory.WiFiAwarePairedDeviceID](asaccessory/wifiawarepaireddeviceid-swift.typealias.md)
  The type used for an accessory’s Wi-Fi Aware Pairing Identifier.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ASDiscoveredAccessory](asdiscoveredaccessory.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ASDiscoveredAccessory](asdiscoveredaccessory.md)
  A discovered accessory, for use in creating a customized picker display item.
- [ASAccessory.AccessoryState](asaccessory/accessorystate.md)
  An enumeration of possible authorization states of an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory)*