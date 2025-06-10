# AccessorySetupKit

**Framework**: AccessorySetupKit  
**Kind**: module

Enable privacy-preserving discovery and configuration of accessories.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

#### Overview

Use AccessorySetupKit to discover and configure Bluetooth or Wi-Fi accessories with images and names provided by the app. Allow seamless, privacy-preserving user consent and control for Bluetooth, Wi-Fi, and Local Network permissions. AccessorySetupKit apps can access enhanced accessory controls including accessory pairing removal and renaming.

To use AccessorySetupKit with [`Wi-Fi Aware`](https://developer.apple.com/documentation/WiFiAware), specify Wi-Fi Aware properties in a [`ASDiscoveryDescriptor`](asdiscoverydescriptor.md) prior to beginning accessory discovery.

> ❗ **Important**: AccessorySetupKit is available for iOS and iPadOS. The accessory’s Bluetooth permission doesn’t sync to a companion watchOS app.

## Topics

### Essentials
- [Setting up and authorizing a Bluetooth accessory](setting-up-and-authorizing-a-bluetooth-accessory.md)
  Discover, select, and set up a specific Bluetooth accessory without requesting permission to use Bluetooth.
- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)
  Detect nearby accessories and facilitate their setup.
- [class ASAccessorySession](asaccessorysession.md)
  A class to coordinate accessory discovery.
### Accessory discovery
- [class ASAccessoryEvent](asaccessoryevent.md)
  Properties of an event encountered during accessory discovery.
- [enum ASAccessoryEventType](asaccessoryeventtype.md)
  An enumeration of the types of events encountered during accessory discovery
- [class ASDiscoveryDescriptor](asdiscoverydescriptor.md)
  Descriptive traits used to discover accessories.
### Accessory description
- [class ASAccessory](asaccessory.md)
  An accessory discovered by the accessory session.
- [ASAccessory.AccessoryState](asaccessory/accessorystate.md)
  An enumeration of possible authorization states of an accessory.
### Displaying picker items
- [class ASPickerDisplayItem](aspickerdisplayitem.md)
  An accessory as presented by the discovery picker.
- [class ASMigrationDisplayItem](asmigrationdisplayitem.md)
  A previously-discovered accessory as presented by the discovery picker, for use when migrating it to AccessorySetupKit.
### Information property list keys
- [NSAccessorySetupSupports](../BundleResources/Information-Property-List/NSAccessorySetupSupports.md)
  An array of strings that indicates the wireless technologies AccessorySetupKit uses when discovering and configuring accessories.
- [NSAccessorySetupBluetoothCompanyIdentifiers](../BundleResources/Information-Property-List/NSAccessorySetupBluetoothCompanyIdentifiers.md)
  An array of strings that represent the Bluetooth company identifiers for accessories that your app configures.
- [NSAccessorySetupBluetoothNames](../BundleResources/Information-Property-List/NSAccessorySetupBluetoothNames.md)
  An array of strings that represent the Bluetooth device names or substrings for accessories that your app configures.
- [NSAccessorySetupBluetoothServices](../BundleResources/Information-Property-List/NSAccessorySetupBluetoothServices.md)
  An array of strings that represent the hexadecimal values of Bluetooth SIG-defined services or custom services for accessories your app configures.
### Errors
- [struct ASError](aserror.md)
  An error encountered during accessory discovery.
- [let ASErrorDomain: String](aserrordomain.md)
  NSError domain for AccessorySetupKit errors.
- [ASError.Code](aserror/code.md)
  Codes that describe errors encountered during accessory discovery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AccessorySetupKit)*