# restorationClass

**Framework**: UIKit  
**Kind**: property

The class responsible for recreating this view controller when restoring the app’s state.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var restorationClass: (any UIViewControllerRestoration.Type)? { get set }
```

## Mentions

- [About the UI restoration process](about-the-ui-restoration-process.md)

#### Discussion

If a view controller has an associated restoration class, the [`viewController(withRestorationIdentifierPath:coder:)`](uiviewcontrollerrestoration/viewcontroller(withrestorationidentifierpath:coder:).md) method of that class is called during state restoration. That method is responsible for returning the view controller object that matches the indicated view controller. If you do not specify a restoration class for your view controller, the state restoration engine asks your app delegate to provide the view controller object instead.

The restoration class must conform to the [`UIViewControllerRestoration`](uiviewcontrollerrestoration.md) protocol.

## See Also

- [Restoring your app’s state](restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [var restorationIdentifier: String?](uiviewcontroller/restorationidentifier.md)
  The identifier that determines whether the view controller supports state restoration.
- [func encodeRestorableState(with: NSCoder)](uiviewcontroller/encoderestorablestate(with:).md)
  Encodes state-related information for the view controller.
- [func decodeRestorableState(with: NSCoder)](uiviewcontroller/decoderestorablestate(with:).md)
  Decodes and restores state-related information for the view controller.
- [func applicationFinishedRestoringState()](uiviewcontroller/applicationfinishedrestoringstate.md)
  Called on restored view controllers after other object decoding is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/restorationclass)*