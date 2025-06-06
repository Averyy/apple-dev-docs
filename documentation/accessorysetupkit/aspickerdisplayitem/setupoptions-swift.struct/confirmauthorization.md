# confirmAuthorization

**Framework**: AccessorySetupKit  
**Kind**: property

An option to require the app to finish accessory authorization before showing the setup view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
static var confirmAuthorization: ASPickerDisplayItem.SetupOptions { get }
```

#### Discussion

If the accessory supports [`bluetoothPairingLE`](asaccessory/supportoptions/bluetoothpairingle.md), then the app needs to start pairing by accessing a protected GATT characteristic.

## See Also

- [static var rename: ASPickerDisplayItem.SetupOptions](aspickerdisplayitem/setupoptions-swift.struct/rename.md)
  An option to ask the person using the app to rename the accessory.
- [static var finishInApp: ASPickerDisplayItem.SetupOptions](aspickerdisplayitem/setupoptions-swift.struct/finishinapp.md)
  An option to ask the person setting up the accessory to finish additional setup in the app after the accessory is authorized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aspickerdisplayitem/setupoptions-swift.struct/confirmauthorization)*