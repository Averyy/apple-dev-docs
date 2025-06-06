# Discovering and configuring accessories

**Framework**: AccessorySetupKit

Detect nearby accessories and facilitate their setup.

#### Overview

Use the AccessorySetupKit framework to simplify discovery and configuration of Bluetooth or Wi-Fi accessories. This allows the person using your app to use these devices without granting overly-broad Bluetooth or Wi-Fi access.

To discover accessories and present them in your app:

1. Declare that your app uses AccessorySetupKit in its information property list.
2. In your app, create and activate an instance of [`ASAccessorySession`](asaccessorysession.md).
3. Provide information about your supported accessories to display a picker. This lets the person using your app discover and select nearby accessories to configure.
4. When the picker sends an accessory added event, use information about the selected device to create a Bluetooth or Wi-Fi connection.

##### Declare Your Apps Accessories

To prepare your app to discover accessories, add the `NSAccessorySetupKitSupports` key to its information property list. Set its value to an array of strings that contains one or more of the following values:

If you add `Bluetooth` to the list of supported protocols, you also need to add the following keys and values to your app’s information property list:

> ❗ **Important**:  If your app tries to discover Bluetooth accessories during setup without supplying these keys and values, or uses identifiers, names, or services that it doesn’t include in its information property list, the app crashes. This only affects use of AccessorySetupKit discovery and selection; you can use other services and properties on the accessory after the person using the app selects it.

 If your app tries to discover Bluetooth accessories during setup without supplying these keys and values, or uses identifiers, names, or services that it doesn’t include in its information property list, the app crashes. This only affects use of AccessorySetupKit discovery and selection; you can use other services and properties on the accessory after the person using the app selects it.

##### Activate a Discovery Session

The [`ASAccessorySession`](asaccessorysession.md) is how your app uses the AccessorySetupKit framework. In your app, you create an instance of [`ASAccessorySession`](asaccessorysession.md) and activate it to receive callbacks with events as the session processes events. The [`activate(on:eventHandler:)`](asaccessorysession/activate(on:eventhandler:).md) method takes a [`DispatchQueue`](https://developer.apple.com/documentation/Dispatch/DispatchQueue) and an event-handling block or closure. The callbacks occur on the provided queue, which defaults to [`main`](https://developer.apple.com/documentation/Dispatch/DispatchQueue/main).

The event handler receives a single parameter of type [`ASAccessoryEvent`](asaccessoryevent.md), which has an [`eventType`](asaccessoryevent/eventtype.md) that you use to determine what to do with each callback. For example, shortly after activating the session, your callback receives the [`ASAccessoryEventType.activated`](asaccessoryeventtype/activated.md) event. The following listing comments on the meaning of these events and how you may want to handle them.

```swift
let session = ASAccessorySession()
override func viewDidLoad() {
    super.viewDidLoad()
    
    session.activate(on: DispatchQueue.main) { [weak self] event in
        guard let self else { return }
        
        switch event.eventType {
        case .activated:
            // Use previously-discovered accessories in
            // session.accessories, if necessary.
        case .accessoryAdded:
            // Handle addition of an accessory by person using the app.
        case .accessoryRemoved, .accessoryChanged:
            // Handle removal or change of previously-added
            // accessory, if necessary.
        case .invalidated:
            // The session is now invalid and you can't use it further.
        case .migrationComplete:
            // Handle migration.
        case .pickerDidPresent:
            // Update state for picker appearing, if necessary.
        case .pickerDidDismiss:
            // Update state for picker disappearing, if necessary.
        case .unknown:
            // Handle unknown event type, if appropriate.
        @unknown default:
            // Reserve this space for yet-to-be-defined event types.
        }
    }
}
```

##### Display an Accessory Picker

When the session activates, its [`accessories`](asaccessorysession/accessories.md) array contains any accessories previously authorized for the app, which you can inspect. To discover new devices, your app needs to show an accessory picker. The person using the app uses this picker to choose the accessory to configure.

> **Note**: If someone renames a previously-discovered Wi-Fi accessory, it becomes discoverable again by the picker.

If someone renames a previously-discovered Wi-Fi accessory, it becomes discoverable again by the picker.

Create instances of [`ASPickerDisplayItem`](aspickerdisplayitem.md) that describe the items in the session that your app can configure. Collect these items in an array and pass them to the session for the operating system to present a picker:

```swift
private func showMyPicker() {
    var descriptor = ASDiscoveryDescriptor()
    descriptor.bluetoothServiceUUID = CBUUID(string: MY_ACCESSORY_UUID_STRING) // If using Wi-Fi, set descriptor.ssid instead.
    
    let displayName = "My Accessory"
    guard let productImage = UIImage(named: MY_ACCESSORY_IMAGE_NAME) else { return }
    
    var items: [ASPickerDisplayItem] = []
    items.append (ASPickerDisplayItem(name: displayName,
                                      productImage: productImage,
                                      descriptor: descriptor))
    
    // Create additional picker items if you support multiple accessories
    // with different Wi-Fi SSIDs or Bluetooth service UUIDs.
    
    session.showPicker(for: items) { error in
        if let error {
            // Handle error.
        } else {
            // Perform any post-picker cleanup.
            // If the picker finished by selecting an item, the event
            // handler receives it as an event of type `.accessoryAdded`.
        }
    }
}
```

Each display item’s [`descriptor`](aspickerdisplayitem/descriptor.md), a property of type [`ASDiscoveryDescriptor`](asdiscoverydescriptor.md), needs to have a [`bluetoothCompanyIdentifier`](asdiscoverydescriptor/bluetoothcompanyidentifier.md) or [`bluetoothServiceUUID`](asdiscoverydescriptor/bluetoothserviceuuid.md), and at least one of the following accessory identifiers:

- [`bluetoothNameSubstring`](asdiscoverydescriptor/bluetoothnamesubstring.md)
- A [`bluetoothManufacturerDataBlob`](asdiscoverydescriptor/bluetoothmanufacturerdatablob.md) and [`bluetoothManufacturerDataMask`](asdiscoverydescriptor/bluetoothmanufacturerdatamask.md) set to the same length.
- A [`bluetoothServiceDataBlob`](asdiscoverydescriptor/bluetoothservicedatablob.md) and [`bluetoothServiceDataMask`](asdiscoverydescriptor/bluetoothservicedatamask.md) set to the same length.
- Either [`ssid`](asdiscoverydescriptor/ssid.md) or [`ssidPrefix`](asdiscoverydescriptor/ssidprefix.md), which needs to have a non-zero length. Only supply one of these; the app crashes if you supply both.

For Bluetooth accessories, the accessory identifiers you use in display items need to match the values you supply in the app’s information property list.

Along with filtering matched accessories to show in the picker, the display item and its descriptor allow you to control certain behaviors of the picker interaction. You can limit the [`bluetoothRange`](asdiscoverydescriptor/bluetoothrange.md) of the descriptor to only match accessories in the immediate physical proximity of the device running the app. To specify behaviors like allowing renaming of the accessory during setup, or confirming accessory authorization before showing the setup view, set the display item’s [`setupOptions`](aspickerdisplayitem/setupoptions-swift.property.md).

When the picker appears, the person using the app sees a view of all nearby accessories that match the identifiers you provide. When multiple devices match a given identifier, the picker shows a separate item for each unique device. This allows the person to select a single device with the picker.

##### Use the Picker When Migrating to Accessorysetupkit

You can also perform a one-time migration of previously-configured accessories, which adds them to the AccessorySetupKit framework’s list of known accessories. To do this, create instances of [`ASMigrationDisplayItem`](asmigrationdisplayitem.md) and include them in the array of items you send to [`showPicker(for:completionHandler:)`](asaccessorysession/showpicker(for:completionhandler:).md).

For items you want to migrate, set one or both of the following:

- A [`hotspotSSID`](asmigrationdisplayitem/hotspotssid.md), which must be a full SSID and not a prefix.
- A [`peripheralIdentifier`](asmigrationdisplayitem/peripheralidentifier.md), which corresponds to the [`identifier`](https://developer.apple.com/documentation/CoreBluetooth/CBPeer/identifier) property of the [`CBPeer`](https://developer.apple.com/documentation/CoreBluetooth/CBPeer) type.

> ❗ **Important**: Don’t initialize a [`CBCentralManager`](https://developer.apple.com/documentation/CoreBluetooth/CBCentralManager) before migration is complete. If you do, your callback handler receives an error and the picker fails to appear.

Don’t initialize a [`CBCentralManager`](https://developer.apple.com/documentation/CoreBluetooth/CBCentralManager) before migration is complete. If you do, your callback handler receives an error and the picker fails to appear.

##### Connect and Configure the Selected Device

When the person picks an accessory, the picker sends an event of type [`ASAccessoryEventType.accessoryAdded`](asaccessoryeventtype/accessoryadded.md), followed by an [`ASAccessoryEventType.pickerDidDismiss`](asaccessoryeventtype/pickerdiddismiss.md) event when they dismiss the picker. If your app presents its own UI to configure the accessory, wait for the picker to dismiss, then use the accessory from the first event. You can handle this scenario by rewriting your event handler closure from before as follows, storing the accessory on the first event and retrieving it on the second.

```swift
case .accessoryAdded:
    self.pickedAccessory = event.accessory
case .pickerDidDismiss:
    guard let accessory = self.pickedAccessory else { return }
    self.pickedAccessory = nil
    self.handleAccessoryAdded(accessory)
```

The event’s [`accessory`](asaccessoryevent/accessory.md) property contains details of the selected device, like its [`displayName`](asaccessory/displayname.md) and an [`bluetoothIdentifier`](asaccessory/bluetoothidentifier.md) for Bluetooth devices or [`ssid`](asaccessory/ssid.md) for Wi-Fi. Use this information to connect to the accessory — using [`Core Bluetooth`](https://developer.apple.com/documentation/CoreBluetooth) for Bluetooth or [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension) for Wi-Fi — and begin your device-specific setup process.

```swift
private func handleAccessoryAdded(_ accessory: ASAccessory) {
    if let btIdentifier = accessory.bluetoothIdentifier {
        // Use Core Bluetooth to communicate with and configure the accessory.
    }
    else if let ssid = accessory.ssid {
        // Create a `NEHotspotConfiguration` with this SSID to configure.
    }
}
```

Because the app discovered the device with AccessorySetupKit, connecting to the device won’t invoke the TCC or other alerts that the system normally shows when using these system frameworks.

## See Also

- [Setting up and authorizing a Bluetooth accessory](setting-up-and-authorizing-a-bluetooth-accessory.md)
  Discover, select, and set up a specific Bluetooth accessory without requesting permission to use Bluetooth.
- [class ASAccessorySession](asaccessorysession.md)
  A class to coordinate accessory discovery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/discovering-and-configuring-accessories)*