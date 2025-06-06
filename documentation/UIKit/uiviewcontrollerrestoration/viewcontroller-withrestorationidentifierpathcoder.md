# viewController(withRestorationIdentifierPath:coder:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Requests the view controller that corresponds to the specified identifier information.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func viewController(withRestorationIdentifierPath identifierComponents: [String], coder: NSCoder) -> UIViewController?
```

## Mentions

- [About the UI preservation process](about-the-ui-preservation-process.md)
- [About the UI restoration process](about-the-ui-restoration-process.md)

#### Return Value

The view controller object to use or `nil` if you do not want to restore this view controller now.

#### Discussion

Your implementation of this method should create (or find) the corresponding view controller object and return it. If your restoration class determines that it doesn’t make sense to display this view controller now, it may return `nil` from this method to prevent that view controller (and its children) from being added to your interface during the restoration process.

You use the strings in the `identifierComponents` parameter to identify the view controller being requested. The view controllers in your app form a hierarchy. At the root of this hierarchy is the window’s root view controller, which itself may present or embed other view controllers. Those presented or embedded view controllers may themselves present and embed other view controllers. The result is a hierarchy of view controller relationships, with each presented or embedded view controller becoming a child of the view controller that presented or embedded it. The strings in the `identifierComponents` array identify the path through this hierarchy from the root view controller to the desired view controller.

It isn’t always necessary to create a new view controller object in your implementation of this method. You can also return an existing view controller object that was created by another means. For example, if the view controller had already been loaded from a storyboard file, you’d return that object rather than create a new one.

Your implementation of this method may use any data in the provided `coder` to assist in the restoration process. However, you don’t need to restore the entire state of the view controller at this point. During a later pass, view controllers that define a [`decodeRestorableState(with:)`](uiviewcontroller/decoderestorablestate(with:).md) method are given a chance to restore their state from the same coder object.

> **Note**:  If you return an object whose class doesn’t match the class of the originally preserved object, or whose class isn’t a direct subclass of the original, the restoration system doesn’t call the [`decodeRestorableState(with:)`](uiviewcontroller/decoderestorablestate(with:).md) method of the view controller.

 If you return an object whose class doesn’t match the class of the originally preserved object, or whose class isn’t a direct subclass of the original, the restoration system doesn’t call the [`decodeRestorableState(with:)`](uiviewcontroller/decoderestorablestate(with:).md) method of the view controller.

## Parameters

- `identifierComponents`: An array of   objects corresponding to the restoration identifiers of the desired view controller and all of its ancestors in the view controller hierarchy. The last value in the array is the restoration identifier of the desired view controller. Earlier entries represent the restoration identifiers of its ancestors.
- `coder`: The keyed archiver containing the app’s saved state information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerrestoration/viewcontroller(withrestorationidentifierpath:coder:))*