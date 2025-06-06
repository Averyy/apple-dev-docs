# bluetoothCompanyIdentifier

**Framework**: AccessorySetupKit  
**Kind**: property

The accessory’s 16-bit Bluetooth Company Identifier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var bluetoothCompanyIdentifier: ASBluetoothCompanyIdentifier { get set }
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

## See Also

- [struct ASBluetoothCompanyIdentifier](asbluetoothcompanyidentifier.md)
  The identifier of a Bluetooth accessory provider.
- [var bluetoothManufacturerDataBlob: Data?](asdiscoverydescriptor/bluetoothmanufacturerdatablob.md)
  A byte buffer that matches the accessory’s Bluetooth manufacturer data.
- [var bluetoothManufacturerDataMask: Data?](asdiscoverydescriptor/bluetoothmanufacturerdatamask.md)
  The accessory’s Bluetooth manufacturer data mask.
- [var bluetoothServiceDataBlob: Data?](asdiscoverydescriptor/bluetoothservicedatablob.md)
  A byte buffer that matches the accessory’s Bluetooth service data.
- [var bluetoothServiceDataMask: Data?](asdiscoverydescriptor/bluetoothservicedatamask.md)
  The accessory’s Bluetooth service data mask.
- [var bluetoothNameSubstring: String?](asdiscoverydescriptor/bluetoothnamesubstring.md)
  The accessory’s over-the-air Bluetooth name substring.
- [var bluetoothServiceUUID: CBUUID?](asdiscoverydescriptor/bluetoothserviceuuid.md)
  The accessory’s Bluetooth service UUID.
- [var bluetoothRange: ASDiscoveryDescriptor.Range](asdiscoverydescriptor/bluetoothrange.md)
  A property that tells the session to discover accessories within a specific Bluetooth range.
- [ASDiscoveryDescriptor.Range](asdiscoverydescriptor/range.md)
  The Bluetooth range in which to discover accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asdiscoverydescriptor/bluetoothcompanyidentifier)*