# filterDiscoveryResults

**Framework**: AccessorySetupKit  
**Kind**: property

An option to pass discovered accessories to the app for more custom filtering, before they’re displayed in the picker for selection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
static var filterDiscoveryResults: ASPickerDisplaySettings.Options { get }
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Discussion

When your picker uses this option, your [`ASAccessorySession`](asaccessorysession.md) receives events of type [`ASAccessoryEventType.accessoryDiscovered`](asaccessoryeventtype/accessorydiscovered.md). Handle this event by examining the discovered accessory. To include it in the picker, create a new [`ASDiscoveredDisplayItem`](asdiscovereddisplayitem.md) for it and call [`updatePicker(showing:completionHandler:)`](asaccessorysession/updatepicker(showing:completionhandler:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aspickerdisplaysettings/options-swift.struct/filterdiscoveryresults)*