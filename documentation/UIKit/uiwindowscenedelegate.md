# UIWindowSceneDelegate

**Framework**: UIKit  
**Kind**: protocol

Additional methods that you use to manage app-specific tasks occurring in a scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIWindowSceneDelegate : UISceneDelegate
```

## Mentions

- [Specifying the scenes your app supports](specifying-the-scenes-your-app-supports.md)

#### Overview

Use your [`UIWindowSceneDelegate`](uiwindowscenedelegate.md) object to manage the life cycle of one instance of your app’s user interface. The window scene delegate conforms to the [`UISceneDelegate`](uiscenedelegate.md) protocol, and you use it to receive notifications when its scene connects to the app, enters the foreground, and so on. You also use it to respond to changes in the underlying environment of the scene. For example, if the user resizes a scene, use your delegate to make any needed changes to your content to accommodate the new size.

Don’t create [`UIWindowSceneDelegate`](uiwindowscenedelegate.md) objects directly. Instead, specify the name of your delegate class as part of the configuration data for your scene. You can specify this information in your app’s `Info.plist` file, or in the [`UISceneConfiguration`](uisceneconfiguration.md) object you return from your app delegate’s [`application(_:configurationForConnecting:options:)`](uiapplicationdelegate/application(_:configurationforconnecting:options:).md) method. For more information about how to configure scenes, see [`Specifying the scenes your app supports`](specifying-the-scenes-your-app-supports.md).

For an example on using `UIWindowSceneDelegate` in your app, see [`Supporting multiple windows on iPad`](supporting-multiple-windows-on-ipad.md).

## Topics

### Managing the scene’s main window
- [var window: UIWindow?](uiwindowscenedelegate/window.md)
  The main window associated with the scene.
### Responding to scene changes
- [func windowScene(UIWindowScene, didUpdateEffectiveGeometry: UIWindowScene.Geometry)](uiwindowscenedelegate/windowscene(_:didupdateeffectivegeometry:).md)
  Called when the window scene’s effective geometry has changed.
### Performing tasks
- [func windowScene(UIWindowScene, performActionFor: UIApplicationShortcutItem, completionHandler: (Bool) -> Void)](uiwindowscenedelegate/windowscene(_:performactionfor:completionhandler:).md)
  Asks the delegate to perform the user-selected action.
- [func windowScene(UIWindowScene, userDidAcceptCloudKitShareWith: CKShareMetadata)](uiwindowscenedelegate/windowscene(_:userdidacceptcloudkitsharewith:).md)
  Tells the delegate that the window scene now has access to shared information in CloudKit.
### Deprecated methods
- [func windowScene(UIWindowScene, didUpdate: any UICoordinateSpace, interfaceOrientation: UIInterfaceOrientation, traitCollection: UITraitCollection)](uiwindowscenedelegate/windowscene(_:didupdate:interfaceorientation:traitcollection:).md)
  Notifies you when the size, orientation, or traits of a scene change.
### Instance Methods
- [func preferredWindowingControlStyle(for: UIWindowScene) -> UIWindowScene.WindowingControlStyle](uiwindowscenedelegate/preferredwindowingcontrolstyle(for:).md)
  Called by the system to determine the windowing control style for the provided scene. `automaticStyle` will be used if this method is not implemented.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UISceneDelegate](uiscenedelegate.md)

## See Also

- [Supporting multiple windows on iPad](supporting-multiple-windows-on-ipad.md)
  Support side-by-side instances of your app’s interface and create new windows.
- [class UIWindowScene](uiwindowscene.md)
  A scene that manages one or more windows for your app.
- [class UIScene](uiscene.md)
  An object that represents one instance of your app’s user interface.
- [protocol UISceneDelegate](uiscenedelegate.md)
  The core methods you use to respond to life-cycle events occurring within a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate)*