# showPicker(completionHandler:)

**Framework**: AccessorySetupKit  
**Kind**: method

Present a picker that shows accessories managed by a Device Discovery Extension in your app.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func showPicker() async throws
```

#### Discussion

Use this method when your app includes a [`DeviceDiscoveryExtension`](https://developer.apple.com/documentation/DeviceDiscoveryExtension) for its supported accessories. If your app doesn’t use DDE, call [`showPicker(for:completionHandler:)`](asaccessorysession/showpicker(for:completionhandler:).md) with an array of [`ASPickerDisplayItem`](aspickerdisplayitem.md) instances instead.

The session’s event handler receives events when this picker displays and dismisses, as well as when the person using the app picks an accessory.

## Parameters

- `completionHandler`: A block or closure that the picker calls when it completes the operation. The completion handler receives an   instance if the picker encounters an error.

## See Also

- [func showPicker(for: [ASPickerDisplayItem], completionHandler: ((any Error)?) -> Void)](asaccessorysession/showpicker(for:completionhandler:).md)
  Present a picker that shows discovered accessories matching an array of display items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/showpicker(completionhandler:))*