# updatePicker(showing:completionHandler:)

**Framework**: AccessorySetupKit  
**Kind**: method

Updates the picker with app-filtered accessories.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
func updatePicker(showing displayItems: [ASDiscoveredDisplayItem]) async throws
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Discussion

You use this method when your picker uses the [`filterDiscoveryResults`](aspickerdisplaysettings/options-swift.struct/filterdiscoveryresults.md) option to enable manual filtering of discovered accessories. After creating customized [`ASDiscoveredDisplayItem`](asdiscovereddisplayitem.md) instances for included accessories, call this method to update the picker to show your app-filtered accessories with updated assets.

## Parameters

- `displayItems`: The app-filtered accessories to show in the picker.
- `completionHandler`: A block or closure that executes after the updatePicker operation completes. The completion handler receives an   instance if the operation encounters an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/updatepicker(showing:completionhandler:))*