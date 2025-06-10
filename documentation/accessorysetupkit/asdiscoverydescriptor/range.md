# ASDiscoveryDescriptor.Range

**Framework**: AccessorySetupKit  
**Kind**: enum

The Bluetooth range in which to discover accessories.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum Range
```

## Topics

### Creating an options instance
- [init?(rawValue: Int)](asdiscoverydescriptor/range/init(rawvalue:).md)
### Bluetooth options
- [ASDiscoveryDescriptor.Range.default](asdiscoverydescriptor/range/default.md)
  The default range in which to discover accessories.
- [ASDiscoveryDescriptor.Range.immediate](asdiscoverydescriptor/range/immediate.md)
  A range in the immediate vicinity of the device performing accessory discovery.
### Default Implementations
- [Equatable Implementations](asdiscoverydescriptor/range/equatable-implementations.md)
- [RawRepresentable Implementations](asdiscoverydescriptor/range/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var bluetoothCompanyIdentifier: ASBluetoothCompanyIdentifier](asdiscoverydescriptor/bluetoothcompanyidentifier.md)
  The accessory’s 16-bit Bluetooth Company Identifier.
- [struct ASBluetoothCompanyIdentifier](asbluetoothcompanyidentifier.md)
  The type used to identify a Bluetooth accessory provider.
- [struct ASBluetoothCompanyIdentifier](asbluetoothcompanyidentifier.md)
  The type used to identify a Bluetooth accessory provider.
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
- [var bluetoothNameSubstringCompareOptions: NSString.CompareOptions](asdiscoverydescriptor/bluetoothnamesubstringcompareoptions.md)
  The accessory’s over-the-air Bluetooth name substring compare options.
- [var bluetoothServiceUUID: CBUUID?](asdiscoverydescriptor/bluetoothserviceuuid.md)
  The accessory’s Bluetooth service UUID.
- [var bluetoothRange: ASDiscoveryDescriptor.Range](asdiscoverydescriptor/bluetoothrange.md)
  A property that tells the session to discover accessories within a specific Bluetooth range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asdiscoverydescriptor/range)*