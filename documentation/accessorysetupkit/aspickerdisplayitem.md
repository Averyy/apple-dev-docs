# ASPickerDisplayItem

**Framework**: AccessorySetupKit  
**Kind**: class

An accessory as presented by the discovery picker.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
class ASPickerDisplayItem
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Overview

Create instances of `ASPickerDisplayItem` that describe the accessories you want to discover. Each item contains a name and product image to display, plus an [`ASDiscoveryDescriptor`](asdiscoverydescriptor.md) that identifies the kind of accessories to match. Pass these in an array to [`showPicker(for:completionHandler:)`](asaccessorysession/showpicker(for:completionhandler:).md) to display a picker that allows the person using your app to discover and select nearby accessories.

Filter the matched accessories by supplying a [`descriptor`](aspickerdisplayitem/descriptor.md), which contains various Bluetooth and Wi-Fi properties to match. The descriptor also allows you to set the [`bluetoothRange`](asdiscoverydescriptor/bluetoothrange.md) of matched accessories; set its value to [`ASDiscoveryDescriptor.Range.immediate`](asdiscoverydescriptor/range/immediate.md) to limit discovery of Bluetooth accessories to those within the immediate proximity of the device running your app.

To enable different behaviors during setup, use the [`setupOptions`](aspickerdisplayitem/setupoptions-swift.property.md) property, which is an option set (Swift) or bitfield (Objective-C) of behavior options. The defined options in [`ASPickerDisplayItem.SetupOptions`](aspickerdisplayitem/setupoptions-swift.struct.md) allow you to specify behaviors like allowing renaming of the accessory during setup, or confirming accessory authorization before showing the setup view.

## Topics

### Creating a display item
- [init(name: String, productImage: UIImage, descriptor: ASDiscoveryDescriptor)](aspickerdisplayitem/init(name:productimage:descriptor:).md)
  Creates a picker display item with a name and image to display and a descriptor to match discovered accessories.
### Specifying discovery properties
- [var descriptor: ASDiscoveryDescriptor](aspickerdisplayitem/descriptor.md)
  A descriptor that the picker uses to determine which discovered accessories to display.
### Customizing display properties
- [var name: String](aspickerdisplayitem/name.md)
  The accessory name to display in the picker.
- [var productImage: UIImage](aspickerdisplayitem/productimage.md)
  An image of the accessory to display in the picker.
### Customizing setup options
- [var setupOptions: ASPickerDisplayItem.SetupOptions](aspickerdisplayitem/setupoptions-swift.property.md)
  Custom setup options for the accessory.
- [ASPickerDisplayItem.SetupOptions](aspickerdisplayitem/setupoptions-swift.struct.md)
  Setup options offered by the accessory picker.
- [var renameOptions: ASAccessory.RenameOptions](aspickerdisplayitem/renameoptions.md)
  Options to allow renaming a matched accessory.
- [ASAccessory.RenameOptions](asaccessory/renameoptions.md)
  Options that affect the behavior of an accessory renaming operation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ASMigrationDisplayItem](asmigrationdisplayitem.md)
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

- [class ASMigrationDisplayItem](asmigrationdisplayitem.md)
  A previously-discovered accessory as presented by the discovery picker, for use when migrating it to AccessorySetupKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aspickerdisplayitem)*