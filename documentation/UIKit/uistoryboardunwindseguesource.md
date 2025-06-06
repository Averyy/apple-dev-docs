# UIStoryboardUnwindSegueSource

**Framework**: UIKit  
**Kind**: class

An encapsulation of information about an unwind segue.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIStoryboardUnwindSegueSource
```

#### Overview

You don’t create instances of this class yourself. UIKit creates an unwind segue source object in response to the triggering of an unwind segue. It passes the source object to other view controller methods that determine the destination of the unwind segue. The information in an unwind segue source object includes the view controller being dismissed by the segue and the action method responsible for the dismissal.

## Topics

### Getting the unwind segue attributes
- [var source: UIViewController](uistoryboardunwindseguesource/source.md)
  The view controller being dismissed by the unwind segue.
- [var unwindAction: Selector](uistoryboardunwindseguesource/unwindaction.md)
  The action method associated with the unwind segue.
- [var sender: Any?](uistoryboardunwindseguesource/sender.md)
  The object that performed the unwind action.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Customizing the behavior of segue-based presentations](customizing-the-behavior-of-segue-based-presentations.md)
  Pass data between view controllers during a segue, and programmatically control when segues occur.
- [Dismissing a view controller with an unwind segue](dismissing-a-view-controller-with-an-unwind-segue.md)
  Configure an unwind segue in your storyboard file that dynamically chooses the most appropriate view controller to display next.
- [class UIStoryboard](uistoryboard.md)
  An encapsulation of the design-time view controller graph represented in an Interface Builder storyboard resource file.
- [class UIStoryboardSegue](uistoryboardsegue.md)
  An object that prepares for and performs the visual transition between two view controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource)*