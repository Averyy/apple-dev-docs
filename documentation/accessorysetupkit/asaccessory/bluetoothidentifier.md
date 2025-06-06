# bluetoothIdentifier

**Framework**: AccessorySetupKit  
**Kind**: property

The accessory’s unique Bluetooth identifier, if any.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var bluetoothIdentifier: UUID? { get }
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Discussion

Use this identifier to establish a connection to the accessory.

## See Also

- [var bluetoothTransportBridgingIdentifier: Data?](asaccessory/bluetoothtransportbridgingidentifier.md)
  The accessory’s Bluetooth identifier, if any, for use when bridging classic transport profiles.
- [var ssid: String?](asaccessory/ssid.md)
  The accessory’s Wi-Fi SSID, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/bluetoothidentifier)*