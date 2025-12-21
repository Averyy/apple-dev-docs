# finishPickerDiscovery(completionHandler:)

**Framework**: AccessorySetupKit  
**Kind**: method

Finish the discovery session in the picker and show a timeout error.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
func finishPickerDiscovery() async throws
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Discussion

Use this method if you previously set the picker display setting [`discoveryTimeout`](aspickerdisplaysettings/discoverytimeout-swift.property.md) to [`unbounded`](aspickerdisplaysettings/discoverytimeout-swift.struct/unbounded.md) in order to perform manual filtering of discovered accessories. Calling this method finishes the discovery session in the picker and shows a timeout error if the session didn’t find any desired accessories.

Calling this method after updating the picker with discovered accessories has no effect.

## Parameters

- `completionHandler`: A block or closure that executes after this operation completes. The completion handler receives an   instance if the operation encounters an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/finishpickerdiscovery(completionhandler:))*