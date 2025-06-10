# restorationIdentifier

**Framework**: UIKit  
**Kind**: property

The identifier that determines whether the view controller supports state restoration.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var restorationIdentifier: String? { get set }
```

## Mentions

- [About the UI preservation process](about-the-ui-preservation-process.md)
- [About the UI restoration process](about-the-ui-restoration-process.md)

#### Discussion

This property indicates whether the view controller and its contents should be preserved and is used to identify the view controller during the restoration process. The value of this property is `nil` by default, which indicates that the view controller should not be saved. Assigning a string object to the property lets the system know that the view controller should be saved. In addition, the contents of the string are your way to identify the purpose of the view controller.

During subsequent launches, UIKit asks your app for help in recreating the view controllers that were installed the last time your app ran. When it asks for a specific view controller, UIKit provides your app with this restoration identifier and the restoration identifiers of any parent view controllers in the view controller hierarchy. Your app must use this information to create or locate the appropriate view controller object.

> ❗ **Important**:  Simply setting the value of this property is not enough to ensure that the view controller is preserved and restored. All parent view controllers must also have a restoration identifier. For more information about the preservation and restoration process, see [`View Controller Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457).

## See Also

- [Restoring your app’s state](restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [var restorationClass: (any UIViewControllerRestoration.Type)?](uiviewcontroller/restorationclass.md)
  The class responsible for recreating this view controller when restoring the app’s state.
- [func encodeRestorableState(with: NSCoder)](uiviewcontroller/encoderestorablestate(with:).md)
  Encodes state-related information for the view controller.
- [func decodeRestorableState(with: NSCoder)](uiviewcontroller/decoderestorablestate(with:).md)
  Decodes and restores state-related information for the view controller.
- [func applicationFinishedRestoringState()](uiviewcontroller/applicationfinishedrestoringstate.md)
  Called on restored view controllers after other object decoding is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/restorationidentifier)*