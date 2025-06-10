# ASAccessorySession

**Framework**: AccessorySetupKit  
**Kind**: class

A class to coordinate accessory discovery.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
class ASAccessorySession
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Overview

Use an instance of `ASAccessorySession` to interact with the AccessorySetupKit framework.

Start the session by calling [`activate(on:eventHandler:)`](asaccessorysession/activate(on:eventhandler:).md), and pass in a dispatch queue and an event-handling closure. AccessorySetupKit calls back to your event handler as the discovery session processes events.

With your event-handler prepared, create an array of [`ASPickerDisplayItem`](aspickerdisplayitem.md) instances to describe accessories your app can set up. Pass this array to the session’s [`showPicker(for:completionHandler:)`](asaccessorysession/showpicker(for:completionhandler:).md) method to allow someone using your app to choose a discovered accessory to set up. Your event handler receives events as the picker appears and dismisses, as well as when the person using the app adds an accessory.

> ❗ **Important**: Starting in iOS 18.4, apps can use AccessorySetupKit for discovery and setup of Bluetooth LE devices that conform to the Human Interface Device (HID) service, such as keyboard and mouse accessories. The HID accessory needs to advertise a custom service besides the HID service. Add the [`bluetoothHID`](asaccessory/supportoptions/bluetoothhid.md) option to the [`supportedOptions`](asdiscoverydescriptor/supportedoptions.md) and configure the [`ASDiscoveryDescriptor`](asdiscoverydescriptor.md) to discover the custom service instead of the HID service.

## Topics

### Managing the session life cycle
- [func activate(on: dispatch_queue_t, eventHandler: (ASAccessoryEvent) -> Void)](asaccessorysession/activate(on:eventhandler:).md)
  Activate the session and start delivering events to an event handler.
- [func invalidate()](asaccessorysession/invalidate.md)
  Invalidate the session by stopping any operations.
### Displaying an accessory picker
- [func showPicker(completionHandler: ((any Error)?) -> Void)](asaccessorysession/showpicker(completionhandler:).md)
  Present a picker that shows accessories managed by a Device Discovery Extension in your app.
- [func showPicker(for: [ASPickerDisplayItem], completionHandler: ((any Error)?) -> Void)](asaccessorysession/showpicker(for:completionhandler:).md)
  Present a picker that shows discovered accessories matching an array of display items.
### Customizing picker behavior
- [var pickerDisplaySettings: ASPickerDisplaySettings?](asaccessorysession/pickerdisplaysettings.md)
  Settings that affect the display of the accessory picker.
- [class ASPickerDisplaySettings](aspickerdisplaysettings.md)
  A type that contains settings to customize the display of the accessory picker
### Accessing discovered accessories
- [var accessories: [ASAccessory]](asaccessorysession/accessories.md)
  An array of previously-selected accessories for this application.
### Managing accessories
- [func renameAccessory(ASAccessory, options: ASAccessory.RenameOptions, completionHandler: ((any Error)?) -> Void)](asaccessorysession/renameaccessory(_:options:completionhandler:).md)
  Displays a view to rename an accessory.
- [ASAccessory.RenameOptions](asaccessory/renameoptions.md)
  Options that affect the behavior of an accessory renaming operation.
- [func removeAccessory(ASAccessory, completionHandler: ((any Error)?) -> Void)](asaccessorysession/removeaccessory(_:completionhandler:).md)
  Removes an accessory.
### Managing authorization
- [func finishAuthorization(for: ASAccessory, settings: ASAccessorySettings, completionHandler: ((any Error)?) -> Void)](asaccessorysession/finishauthorization(for:settings:completionhandler:).md)
  Finish authorization of a partially-setup accessory.
- [class ASAccessorySettings](asaccessorysettings.md)
  Properties of an accessory.
- [func failAuthorization(for: ASAccessory, completionHandler: ((any Error)?) -> Void)](asaccessorysession/failauthorization(for:completionhandler:).md)
  End authorization of a partially-configured accessory as a failure.
- [func updateAuthorization(for: ASAccessory, descriptor: ASDiscoveryDescriptor, completionHandler: ((any Error)?) -> Void)](asaccessorysession/updateauthorization(for:descriptor:completionhandler:).md)
  Displays a view to upgrade an accessory with additional technology permissions.

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

- [Setting up and authorizing a Bluetooth accessory](setting-up-and-authorizing-a-bluetooth-accessory.md)
  Discover, select, and set up a specific Bluetooth accessory without requesting permission to use Bluetooth.
- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)
  Detect nearby accessories and facilitate their setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession)*