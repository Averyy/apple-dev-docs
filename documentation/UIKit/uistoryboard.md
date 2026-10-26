# UIStoryboard

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An encapsulation of the design-time view controller graph represented in an Interface Builder storyboard resource file.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Loading Interface Builder products will not be supported in a future version of visionOS.

## Declaration

```swift
@MainActor
class UIStoryboard
```

```objc
@interface UIStoryboard : NSObject
```

## Mentions

- [Displaying and managing views with a view controller](./displaying-and-managing-views-with-a-view-controller.md)

#### Overview

A [`UIStoryboard`](./uistoryboard.md) object manages archived versions of your app’s view controllers. At design time, you configure the content of your view controllers visually, and Xcode saves the data needed to recreate that interface in a storyboard file in your app’s bundle. When you want to create a new view controller programmatically, first create a [`UIStoryboard`](./uistoryboard.md) object and specify the appropriate name and bundle information. Then use that object to instantiate the specific view controller that you want.

During the instantiation process, [`UIStoryboard`](./uistoryboard.md) creates your view controller programmatically using its [`init(coder:)`](./uiviewcontroller/init%28coder%29.md) method. The storyboard passes the view controller’s data archive to that method, which then uses the data to recreate the state of the view controller and its views. If you have a custom initialization method for your view controller, you can ask the storyboard to instantiate your view controller using a block you provide. You can use this block to call your custom initialization method, passing any extra data your view controller needs.

For visionOS apps, you can load existing storyboards, but you can’t add content specific to the platform. Migrate your interface code to SwiftUI as soon as possible.

## Topics

### Getting a Storyboard Object
- [init(name: String, bundle: Bundle?)](./uistoryboard/init%28name,bundle%29.md)
  Creates and returns a storyboard object for the specified resource file.
### Loading the Initial View Controller
- [func instantiateInitialViewController() -> UIViewController?](./uistoryboard/instantiateinitialviewcontroller%28%29.md)
  Creates the initial view controller and initializes it with the data from the storyboard.
- [func instantiateInitialViewController<ViewController>(creator: ((NSCoder) -> ViewController?)?) -> ViewController?](./uistoryboard/instantiateinitialviewcontroller%28creator%29.md)
  Creates the initial view controller from the storyboard and initializes it using your custom initialization code.
- [- instantiateInitialViewControllerWithCreator:](./uistoryboard/instantiateinitialviewcontrollerwithcreator_.md)
  Creates the initial view controller from the storyboard and initializes it using your custom initialization code.
### Instantiating Storyboard View Controllers
- [func instantiateViewController(withIdentifier: String) -> UIViewController](./uistoryboard/instantiateviewcontroller%28withidentifier%29.md)
  Creates the view controller with the specified identifier and initializes it with the data from the storyboard.
- [func instantiateViewController<ViewController>(identifier: String, creator: ((NSCoder) -> ViewController?)?) -> ViewController](./uistoryboard/instantiateviewcontroller%28identifier,creator%29.md)
  Creates the specified view controller from the storyboard and initializes it using your custom initialization code.
- [- instantiateViewControllerWithIdentifier:creator:](./uistoryboard/instantiateviewcontrollerwithidentifier_creator_.md)
  Creates the specified view controller from the storyboard and initializes it using your custom initialization code.
- [UIStoryboardViewControllerCreator](./uistoryboardviewcontrollercreator.md)
  A handler block that contains the custom initialization code for a view controller you instantiate from a storyboard.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Storyboards
- [Customizing the behavior of segue-based presentations](./customizing-the-behavior-of-segue-based-presentations.md)
  Pass data between view controllers during a segue, and programmatically control when segues occur.
- [Dismissing a view controller with an unwind segue](./dismissing-a-view-controller-with-an-unwind-segue.md)
  Configure an unwind segue in your storyboard file that dynamically chooses the most appropriate view controller to display next.
- [class UIStoryboardSegue](./uistoryboardsegue.md)
  An object that prepares for and performs the visual transition between two view controllers.
- [class UIStoryboardUnwindSegueSource](./uistoryboardunwindseguesource.md)
  An encapsulation of information about an unwind segue.
- [UIStoryboardViewControllerCreator](./uistoryboardviewcontrollercreator.md)
  A handler block that contains the custom initialization code for a view controller you instantiate from a storyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistoryboard)*