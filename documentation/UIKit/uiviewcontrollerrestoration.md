# UIViewControllerRestoration

**Framework**: UIKit  
**Kind**: protocol

The methods that objects adopt so that they can act as a restoration class for view controllers during state restoration.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIViewControllerRestoration
```

#### Overview

To use a class that adopts this protocol, you must assign that class to the [`restorationClass`](uiviewcontroller/restorationclass.md) property of one of your app’s view controllers. The method in this protocol should be used to create the view controller, if it doesn’t yet exist, or return an existing view controller object, if one does exist.

## Topics

### Creating the view controller
- [static func viewController(withRestorationIdentifierPath: [String], coder: NSCoder) -> UIViewController?](uiviewcontrollerrestoration/viewcontroller(withrestorationidentifierpath:coder:).md)
  Requests the view controller that corresponds to the specified identifier information.

## See Also

- [Restoring your app’s state](restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [Restoring your app’s state with SwiftUI](../SwiftUI/restoring-your-app-s-state-with-swiftui.md)
  Provide app continuity for users by preserving their current activities.
- [Preserving your app’s UI across launches](preserving-your-app-s-ui-across-launches.md)
  Return your app to its previous state after the system terminates it.
- [protocol UIObjectRestoration](uiobjectrestoration.md)
  The interface that restoration classes use to restore preserved objects.
- [protocol UIStateRestoring](uistaterestoring.md)
  Methods for adding objects to your state restoration archives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerrestoration)*