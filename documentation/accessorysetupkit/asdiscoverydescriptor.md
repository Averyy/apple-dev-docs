# ASDiscoveryDescriptor

**Framework**: AccessorySetupKit  
**Kind**: class

Descriptive traits used to discover accessories.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
class ASDiscoveryDescriptor
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Overview

Use an instance of this type to identify accessories your app can set up, then set it as the [`descriptor`](aspickerdisplayitem/descriptor.md) property of an [`ASPickerDisplayItem`](aspickerdisplayitem.md).

Some of the Bluetooth identifier properties work together to filter matching accessories, as described in the following table.

| Use | Filter property | Also requires | Description |
| --- | --- | --- | --- |
| Required | [`bluetoothServiceUUID`](asdiscoverydescriptor/bluetoothserviceuuid.md) or [`bluetoothCompanyIdentifier`](asdiscoverydescriptor/bluetoothcompanyidentifier.md) | (none) | Provide at least one UUID or manufacturer ID to filter. |
| Optional | [`bluetoothNameSubstring`](asdiscoverydescriptor/bluetoothnamesubstring.md) | [`bluetoothServiceUUID`](asdiscoverydescriptor/bluetoothserviceuuid.md) or [`bluetoothCompanyIdentifier`](asdiscoverydescriptor/bluetoothcompanyidentifier.md) | Provide a name substring to look for.  Requires setting at least a service UUID or company ID, which identifies the service or company using the name. |
| Optional | [`bluetoothManufacturerDataBlob`](asdiscoverydescriptor/bluetoothmanufacturerdatablob.md) and [`bluetoothManufacturerDataMask`](asdiscoverydescriptor/bluetoothmanufacturerdatamask.md) | [`bluetoothCompanyIdentifier`](asdiscoverydescriptor/bluetoothcompanyidentifier.md) | When using manufacturer data filters, provide both the data and mask. These properties should have the same length and be less than or equal to the size of the advertised payload. The [`bluetoothCompanyIdentifier`](asdiscoverydescriptor/bluetoothcompanyidentifier.md) identifies the manufacturer associated with the data. |
| Optional | [`bluetoothServiceDataBlob`](asdiscoverydescriptor/bluetoothservicedatablob.md) and [`bluetoothServiceDataMask`](asdiscoverydescriptor/bluetoothservicedatamask.md) | [`bluetoothServiceUUID`](asdiscoverydescriptor/bluetoothserviceuuid.md) | When using UUID service data filters, provide both the data and mask. These properties should have the same length and be less than or equal to the size of the advertised payload. The [`bluetoothServiceUUID`](asdiscoverydescriptor/bluetoothserviceuuid.md) identifies the service associated with the data. |

The descriptor also allows you to set the [`bluetoothRange`](asdiscoverydescriptor/bluetoothrange.md) of matched accessories; set its value to [`ASDiscoveryDescriptor.Range.immediate`](asdiscoverydescriptor/range/immediate.md) to limit discovery of Bluetooth accessories to those within the immediate proximity of the device running your app.

## Topics

### Specifying Bluetooth properties
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
- [ASDiscoveryDescriptor.Range](asdiscoverydescriptor/range.md)
  The Bluetooth range in which to discover accessories.
### Specifying Wi-Fi properties
- [var ssid: String?](asdiscoverydescriptor/ssid.md)
  The SSID of the accessory’s Wi-Fi network.
- [var ssidPrefix: String?](asdiscoverydescriptor/ssidprefix.md)
  The prefix string of SSID of the accessory’s Wi-Fi network.
### Specifying options
- [var supportedOptions: ASAccessory.SupportOptions](asdiscoverydescriptor/supportedoptions.md)
  Options supported by an accessory.
- [ASAccessory.SupportOptions](asaccessory/supportoptions.md)
  Options of discoverable accessories.
### Specifying Wi-Fi Aware properties
- [var wifiAwareServiceName: String?](asdiscoverydescriptor/wifiawareservicename.md)
  The accessory’s Wi-Fi Aware’s service name if available.
- [var wifiAwareServiceRole: ASDiscoveryDescriptor.WiFiAwareServiceRole](asdiscoverydescriptor/wifiawareservicerole-swift.property.md)
  The role of the accessory’s Wi-Fi Aware’s service.
- [ASDiscoveryDescriptor.WiFiAwareServiceRole](asdiscoverydescriptor/wifiawareservicerole-swift.enum.md)
  A type that defines the role of an accessory’s Wi-Fi Aware’s service.
- [var wifiAwareModelNameMatch: ASPropertyCompareString?](asdiscoverydescriptor/wifiawaremodelnamematch.md)
  The accessory’s Wi-Fi Aware model name and matching options.
- [var wifiAwareVendorNameMatch: ASPropertyCompareString?](asdiscoverydescriptor/wifiawarevendornamematch.md)
  The accessory’s Wi-Fi Aware vendor name  and matching options.
- [class ASPropertyCompareString](aspropertycomparestring.md)
  A type that specifies how to filter a property against a given string and comparison options.

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ASAccessoryEvent](asaccessoryevent.md)
  Properties of an event encountered during accessory discovery.
- [enum ASAccessoryEventType](asaccessoryeventtype.md)
  An enumeration of the types of events encountered during accessory discovery


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asdiscoverydescriptor)*