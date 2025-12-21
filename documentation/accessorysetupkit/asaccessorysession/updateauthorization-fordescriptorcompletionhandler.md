# updateAuthorization(for:descriptor:completionHandler:)

**Framework**: AccessorySetupKit  
**Kind**: method

Displays a view to upgrade an accessory with additional technology permissions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func updateAuthorization(for accessory: ASAccessory, descriptor: ASDiscoveryDescriptor) async throws
```

#### Discussion

Call this method to upgrade previously-added SSID-based accessories to use WiFi Aware.

## Parameters

- `accessory`: The accessory to update.
- `descriptor`: An updated descriptor that the picker uses to add new technology authorization for the provided accessory.
- `completionHandler`: A block or closure that executes after the picker is shown. The completion handler receives an   instance if the upgrade operation encounters an error. In Swift, you can omit the completion handler by calling the method asynchronously and catching any error thrown by the method.

## See Also

- [func finishAuthorization(for: ASAccessory, settings: ASAccessorySettings, completionHandler: ((any Error)?) -> Void)](asaccessorysession/finishauthorization(for:settings:completionhandler:).md)
  Finish authorization of a partially-setup accessory.
- [class ASAccessorySettings](asaccessorysettings.md)
  Properties of an accessory.
- [func failAuthorization(for: ASAccessory, completionHandler: ((any Error)?) -> Void)](asaccessorysession/failauthorization(for:completionhandler:).md)
  End authorization of a partially-configured accessory as a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/updateauthorization(for:descriptor:completionhandler:))*