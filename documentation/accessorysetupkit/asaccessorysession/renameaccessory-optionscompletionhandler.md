# renameAccessory(_:options:completionHandler:)

**Framework**: AccessorySetupKit  
**Kind**: method

Displays a view to rename an accessory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func renameAccessory(_ accessory: ASAccessory, options renameOptions: ASAccessory.RenameOptions = []) async throws
```

#### Discussion

To rename a Wi-Fi SSID with this method, use the option [`ssid`](asaccessory/renameoptions/ssid.md).

## Parameters

- `accessory`: The accessory to rename.
- `renameOptions`: Options that affect the behavior of the rename operation.
- `completionHandler`: A block or closure that executes after the rename operation completes. The completion handler receives an   instance if the rename operation encounters an error.

## See Also

- [ASAccessory.RenameOptions](asaccessory/renameoptions.md)
  Options that affect the behavior of an accessory renaming operation.
- [func removeAccessory(ASAccessory, completionHandler: ((any Error)?) -> Void)](asaccessorysession/removeaccessory(_:completionhandler:).md)
  Removes an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/renameaccessory(_:options:completionhandler:))*