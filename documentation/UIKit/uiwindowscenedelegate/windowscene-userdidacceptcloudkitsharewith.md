# windowScene(_:userDidAcceptCloudKitShareWith:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the window scene now has access to shared information in CloudKit.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func windowScene(_ windowScene: UIWindowScene, userDidAcceptCloudKitShareWith cloudKitShareMetadata: CKShareMetadata)
```

#### Discussion

Use this method to respond to a CloudKit Sharing invitation. In your implementation, accept the share by scheduling a [`CKAcceptSharesOperation`](https://developer.apple.com/documentation/CloudKit/CKAcceptSharesOperation) object that contains the metadata object in the `cloudKitShareMetadata` parameter. After your operation object finishes successfully, you can begin fetching records and incorporating the resulting data into your app. Alternatively, if your app uses Core Data and [`NSPersistentCloudKitContainer`](https://developer.apple.com/documentation/CoreData/NSPersistentCloudKitContainer), accept the share by calling the container’s [`acceptShareInvitations(from:into:completion:)`](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/3746828-acceptshareinvitations) method.

> **Note**:  To use this method in a SwiftUI app, you must first add scene and application delegates to your project and configure your app to use them. For more information, see [`Accepting Share Invitations in a SwiftUI App`](https://developer.apple.com/documentation/CoreData/accepting-share-invitations-in-a-swiftui-app).

 To use this method in a SwiftUI app, you must first add scene and application delegates to your project and configure your app to use them. For more information, see [`Accepting Share Invitations in a SwiftUI App`](https://developer.apple.com/documentation/CoreData/accepting-share-invitations-in-a-swiftui-app).

The system calls this method only when your app is running and has an existing scene. If your app isn’t running, the system includes the share metadata in the [`UIScene.ConnectionOptions`](uiscene/connectionoptions.md) object it passes to the [`init(session:connectionOptions:)`](uiscene/init(session:connectionoptions:).md) method when it creates your app’s first scene.

## Parameters

- `windowScene`: The window scene object receiving the metadata.
- `cloudKitShareMetadata`: Information about the CloudKit data that is now available to the app. Use this object to retrieve information about the   object and the associated records.

## See Also

- [func windowScene(UIWindowScene, performActionFor: UIApplicationShortcutItem, completionHandler: (Bool) -> Void)](uiwindowscenedelegate/windowscene(_:performactionfor:completionhandler:).md)
  Asks the delegate to perform the user-selected action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/windowscene(_:userdidacceptcloudkitsharewith:))*