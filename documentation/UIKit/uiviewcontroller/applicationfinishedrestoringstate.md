# applicationFinishedRestoringState()

**Framework**: UIKit  
**Kind**: method

Called on restored view controllers after other object decoding is complete.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func applicationFinishedRestoringState()
```

#### Discussion

After other object decoding has completed, the system calls this method. This allows a view controller to complete setup after other state restoration, relying on the system to ensure that the states of all objects from the restoration archive have been decoded.

## See Also

- [Restoring your app’s state](restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [var restorationIdentifier: String?](uiviewcontroller/restorationidentifier.md)
  The identifier that determines whether the view controller supports state restoration.
- [var restorationClass: (any UIViewControllerRestoration.Type)?](uiviewcontroller/restorationclass.md)
  The class responsible for recreating this view controller when restoring the app’s state.
- [func encodeRestorableState(with: NSCoder)](uiviewcontroller/encoderestorablestate(with:).md)
  Encodes state-related information for the view controller.
- [func decodeRestorableState(with: NSCoder)](uiviewcontroller/decoderestorablestate(with:).md)
  Decodes and restores state-related information for the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/applicationfinishedrestoringstate())*