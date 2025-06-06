# decodeRestorableState(with:)

**Framework**: UIKit  
**Kind**: method

Decodes and restores state-related information for the view controller.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func decodeRestorableState(with coder: NSCoder)
```

## Mentions

- [About the UI restoration process](about-the-ui-restoration-process.md)

#### Discussion

Do not call this method directly. The system calls this method during the state restoration process so that you can restore your view controller to its previous state.

If your app supports state restoration, override this method for any view controllers for which you also overrode the [`encodeRestorableState(with:)`](uiviewcontroller/encoderestorablestate(with:).md) method. Your implementation of this method should use any saved state information to restore the view controller to its previous configuration. If your [`encodeRestorableState(with:)`](uiviewcontroller/encoderestorablestate(with:).md) method called `super`, this method should similarly call `super` at some point in its implementation.

## Parameters

- `coder`: The coder object to use to decode the state of the view.

## See Also

- [Restoring your app’s state](restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [var restorationIdentifier: String?](uiviewcontroller/restorationidentifier.md)
  The identifier that determines whether the view controller supports state restoration.
- [var restorationClass: (any UIViewControllerRestoration.Type)?](uiviewcontroller/restorationclass.md)
  The class responsible for recreating this view controller when restoring the app’s state.
- [func encodeRestorableState(with: NSCoder)](uiviewcontroller/encoderestorablestate(with:).md)
  Encodes state-related information for the view controller.
- [func applicationFinishedRestoringState()](uiviewcontroller/applicationfinishedrestoringstate.md)
  Called on restored view controllers after other object decoding is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/decoderestorablestate(with:))*