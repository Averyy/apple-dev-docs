# UIWindowScene

**Framework**: UIKit  
**Kind**: class

A scene that manages one or more windows for your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIWindowScene
```

## Mentions

- [Specifying the scenes your app supports](specifying-the-scenes-your-app-supports.md)
- [Presenting content on a connected display](presenting-content-on-a-connected-display.md)

#### Overview

A [`UIWindowScene`](uiwindowscene.md) object manages one instance of your app’s UI, including one or more windows that you display from that scene. The scene object manages the display of your windows on the user’s device, and the life cycle of that scene as the user interacts with it. When the state of the scene changes, the scene object notifies its delegate object, which adopts the [`UIWindowSceneDelegate`](uiwindowscenedelegate.md) protocol. The scene also posts appropriate notifications to registered observers. Use the delegate object or notification observers to respond to any changes.

Don’t create window scene objects directly. Instead, specify that you want a [`UIWindowScene`](uiwindowscene.md) object at configuration time by including the class name for the scene in the scene configuration details of your app’s `Info.plist` file. You can also specify the class name when creating a [`UISceneConfiguration`](uisceneconfiguration.md) object in your app delegate’s [`application(_:configurationForConnecting:options:)`](uiapplicationdelegate/application(_:configurationforconnecting:options:).md) method. When the user interacts with your app, the system creates an appropriate scene object based on the configuration data you provided. To create a scene programmatically, call the [`requestSceneSessionActivation(_:userActivity:options:errorHandler:)`](uiapplication/requestscenesessionactivation(_:useractivity:options:errorhandler:).md) method of [`UIApplication`](uiapplication.md).

## Topics

### Getting the active windows
- [var windows: [UIWindow]](uiwindowscene/windows.md)
  The windows associated with the scene.
- [var keyWindow: UIWindow?](uiwindowscene/keywindow.md)
  The key window associated with the scene.
- [var screen: UIScreen](uiwindowscene/screen.md)
  The screen that displays the contents of the scene.
### Getting the interface attributes
- [var traitCollection: UITraitCollection](uiwindowscene/traitcollection.md)
  The traits that describe the current environment of the scene.
- [var coordinateSpace: any UICoordinateSpace](uiwindowscene/coordinatespace.md)
  The coordinate space occupied by the scene.
- [var interfaceOrientation: UIInterfaceOrientation](uiwindowscene/interfaceorientation.md)
  The orientation to use when displaying content in your windows.
- [var sizeRestrictions: UISceneSizeRestrictions?](uiwindowscene/sizerestrictions.md)
  The minimum and maximum size of the app’s windows.
- [class UISceneSizeRestrictions](uiscenesizerestrictions.md)
  An object that specifies the minimum and maximum sizes for resizable windows.
### Observing trait changes
- [protocol UITraitChangeObservable](uitraitchangeobservable-67e94.md)
  A type that calls your code in reaction to changes in the trait environment.
### Overriding trait values
- [var traitOverrides: UITraitOverrides](uiwindowscene/traitoverrides-1klo1.md)
- [struct UITraitOverrides](uitraitoverrides-swift.struct.md)
### Providing a PDF version of your scene
- [var screenshotService: UIScreenshotService?](uiwindowscene/screenshotservice.md)
  An object that generates a high-fidelity version of your app’s content.
- [class UIScreenshotService](uiscreenshotservice.md)
  An object that coordinates the creation of PDF screenshots of an app’s content.
### Sharing content
- [var activityItemsConfigurationSource: (any UIActivityItemsConfigurationProviding)?](uiwindowscene/activityitemsconfigurationsource.md)
  An object that can provide shareable items for a scene.
- [protocol UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
  An interface that provides a source for shareable content to fulfill user requests to share current content.
### Determining window behaviors
- [var isFullScreen: Bool](uiwindowscene/isfullscreen.md)
  A Boolean value that indicates whether the window scene is full screen or windowed.
- [var windowingBehaviors: UISceneWindowingBehaviors?](uiwindowscene/windowingbehaviors.md)
  An object that specifies the behaviors of the window.
- [class UISceneWindowingBehaviors](uiscenewindowingbehaviors.md)
  An object with properties that determine the behavior of a window.
### Working with window geometry
- [var effectiveGeometry: UIWindowScene.Geometry](uiwindowscene/effectivegeometry.md)
  The current values for the window scene’s geometry in system space.
- [func requestGeometryUpdate(UIWindowScene.GeometryPreferences, errorHandler: ((any Error) -> Void)?)](uiwindowscene/requestgeometryupdate(_:errorhandler:).md)
  Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [UIWindowScene.Geometry](uiwindowscene/geometry.md)
  An object that provides geometry information about the window scene.
- [UIWindowScene.GeometryPreferences](uiwindowscene/geometrypreferences.md)
  An abstract superclass for representing window scene geometry preferences.
- [UIWindowScene.GeometryPreferences.iOS](uiwindowscene/geometrypreferences/ios.md)
  An object that represents the geometry preferences for a window scene in an iOS app.
- [UIWindowScene.GeometryPreferences.Mac](uiwindowscene/geometrypreferences/mac.md)
  An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [UIWindowScene.GeometryPreferences.Vision](uiwindowscene/geometrypreferences/vision.md)
- [let UIProposedSceneSizeNoPreference: CGFloat](uiproposedscenesizenopreference.md)
### Working with focus
- [var focusSystem: UIFocusSystem?](uiwindowscene/focussystem.md)
  The focus system that’s responsible for the window scene.
### Getting the status bar configuration
- [var statusBarManager: UIStatusBarManager?](uiwindowscene/statusbarmanager.md)
  The current configuration of the status bar.
- [class UIStatusBarManager](uistatusbarmanager.md)
  An object that describes the configuration of the status bar.
### Configuring a window’s title bar
- [var titlebar: UITitlebar?](uiwindowscene/titlebar.md)
  The title bar displayed in a window of a Mac app.
- [class UITitlebar](uititlebar.md)
  An object that you use to configure the title bar of a window in a Mac app built with Mac Catalyst.
### Supporting types
- [UIWindowScene.ActivationAction](uiwindowscene/activationaction.md)
  A menu element that requests a window scene.
- [UIWindowScene.ActivationConfiguration](uiwindowscene/activationconfiguration.md)
  An object that provides configuration options for a window scene request.
- [UIWindowScene.ActivationInteraction](uiwindowscene/activationinteraction.md)
  An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [UIWindowScene.ActivationRequestOptions](uiwindowscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating a new window scene.
- [class UIWindowSceneDestructionRequestOptions](uiwindowscenedestructionrequestoptions.md)
  An object that contains information to use when removing a window scene from your app.
- [UIWindowScene.DismissalAnimation](uiwindowscene/dismissalanimation.md)
  Constants that indicate the types of animations available for dismissing a scene’s windows.
- [class UIWindowSceneDragInteraction](uiwindowscenedraginteraction.md)
  An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [UIWindowScene.ResizingRestrictions](uiwindowscene/resizingrestrictions.md)
- [enum UIWindowSceneResizingRestrictions](uiwindowsceneresizingrestrictions.md)
- [UIWindowScene.PresentationStyle](uiwindowscene/presentationstyle.md)
  The placement of a window scene relative to other scenes in the workspace.

## Relationships

### Inherits From
- [UIScene](uiscene.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Supporting multiple windows on iPad](supporting-multiple-windows-on-ipad.md)
  Support side-by-side instances of your app’s interface and create new windows.
- [protocol UIWindowSceneDelegate](uiwindowscenedelegate.md)
  Additional methods that you use to manage app-specific tasks occurring in a scene.
- [class UIScene](uiscene.md)
  An object that represents one instance of your app’s user interface.
- [protocol UISceneDelegate](uiscenedelegate.md)
  The core methods you use to respond to life-cycle events occurring within a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene)*