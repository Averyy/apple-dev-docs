# UIStoryboardSegue

**Framework**: UIKit  
**Kind**: class

An object that prepares for and performs the visual transition between two view controllers.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIStoryboardSegue
```

## Mentions

- [Customizing the behavior of segue-based presentations](customizing-the-behavior-of-segue-based-presentations.md)
- [Dismissing a view controller with an unwind segue](dismissing-a-view-controller-with-an-unwind-segue.md)

#### Overview

The [`UIStoryboardSegue`](uistoryboardsegue.md) class supports the standard visual transitions available in UIKit. You can also subclass to define custom transitions between the view controllers in your storyboard file.

Segue objects contain information about the view controllers involved in a transition. When a segue is triggered, but before the visual transition occurs, the storyboard runtime calls the current view controller’s [`prepare(for:sender:)`](uiviewcontroller/prepare(for:sender:).md) method so that it can pass any needed data to the view controller that’s about to be displayed.

You don’t create segue objects directly. Instead, the storyboard runtime creates them when it must perform a segue between two view controllers. You can still initiate a segue programmatically using the [`performSegue(withIdentifier:sender:)`](uiviewcontroller/performsegue(withidentifier:sender:).md) method of [`UIViewController`](uiviewcontroller.md) if you want. You might do so to initiate a segue from a source that was added programmatically and therefore not available in Interface Builder.

##### Subclassing Notes

You can subclass [`UIStoryboardSegue`](uistoryboardsegue.md) in situations where you want to provide a custom transition between view controllers in your application. To use your custom segue, create a segue line between the appropriate view controllers in Interface Builder and set its type to Custom in the inspector; you must also specify the class name of the segue to use in the inspector.

When the storyboard runtime detects a custom segue, it creates a new instance of your class, configures it with the view controller objects, asks the view controller source to prepare for the segue, and then performs the segue.

###### Methods to Override

For custom segues, the main method you need to override is the [`perform()`](uistoryboardsegue/perform().md) method. The storyboard runtime calls this method when it’s time to perform the visual transition from the view controller in [`source`](uistoryboardsegue/source.md) to the view controller in [`destination`](uistoryboardsegue/destination.md). If you need to initialize any variables in your custom segue subclass, you can also override the [`init(identifier:source:destination:)`](uistoryboardsegue/init(identifier:source:destination:).md) method and initialize them in your custom implementation.

###### Alternatives to Subclassing

If your segue doesn’t need to store additional information or provide anything other than a [`perform()`](uistoryboardsegue/perform().md) method, consider using the [`init(identifier:source:destination:performHandler:)`](uistoryboardsegue/init(identifier:source:destination:performhandler:).md) method instead.

## Topics

### Initializing a storyboard segue
- [init(identifier: String?, source: UIViewController, destination: UIViewController)](uistoryboardsegue/init(identifier:source:destination:).md)
  Initializes and returns a storyboard segue object for use in performing a segue.
### Accessing the segue attributes
- [var source: UIViewController](uistoryboardsegue/source.md)
  The source view controller for the segue.
- [var destination: UIViewController](uistoryboardsegue/destination.md)
  The destination view controller for the segue.
- [var identifier: String?](uistoryboardsegue/identifier.md)
  The identifier for the segue object.
### Performing the segue
- [func perform()](uistoryboardsegue/perform.md)
  Performs the visual transition for the segue.
### Creating a custom segue
- [convenience init(identifier: String?, source: UIViewController, destination: UIViewController, performHandler: () -> Void)](uistoryboardsegue/init(identifier:source:destination:performhandler:).md)
  Creates a segue that calls a block to perform the segue transition.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIStoryboardPopoverSegue](uistoryboardpopoversegue.md)
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
- [class UIStoryboardUnwindSegueSource](uistoryboardunwindseguesource.md)
  An encapsulation of information about an unwind segue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboardsegue)*