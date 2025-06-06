# windowScene(_:performActionFor:completionHandler:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to perform the user-selected action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func windowScene(_ windowScene: UIWindowScene, performActionFor shortcutItem: UIApplicationShortcutItem) async -> Bool
```

#### Discussion

When the user selects one of your app’s shortcut items, use this method to perform the selected action. After you finish the action, execute the specified `completionHandler` block to report your success or failure in performing the action.

## Parameters

- `windowScene`: The window scene object receiving the shortcut item.
- `shortcutItem`: The action selected by the user. Your app defines the actions that it supports, and the user chooses from among those actions. For information about how to create and configure shortcut items for your app, see  .
- `completionHandler`: A handler block to call after you complete the action. This block has no return value and takes the following parameter:

## See Also

- [func windowScene(UIWindowScene, userDidAcceptCloudKitShareWith: CKShareMetadata)](uiwindowscenedelegate/windowscene(_:userdidacceptcloudkitsharewith:).md)
  Tells the delegate that the window scene now has access to shared information in CloudKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/windowscene(_:performactionfor:completionhandler:))*