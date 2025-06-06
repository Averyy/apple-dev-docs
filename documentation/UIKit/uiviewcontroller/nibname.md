# nibName

**Framework**: UIKit  
**Kind**: property

The name of the view controller’s nib file, if one was specified.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var nibName: String? { get }
```

#### Discussion

This property contains the value specified at initialization time to the [`init(nibName:bundle:)`](uiviewcontroller/init(nibname:bundle:).md) method. The value of this property may be `nil`.

If you use a nib file to store your view controller’s view, it is recommended that you specify that nib file explicitly when initializing your view controller. However, if you do not specify a nib name, and do not override the [`loadView()`](uiviewcontroller/loadview().md) method in your custom subclass, the view controller searches for a nib file using other means. Specifically, it looks for a nib file with an appropriate name (without the `.nib` extension) and loads that nib file whenever its view is requested. Specifically, it looks (in order) for a nib file with one of the following names:

1. If the view controller class name ends with the word ‘Controller’, as in `MyViewController`, it looks for a nib file whose name matches the class name without the word ‘Controller’, as in `MyView.nib`.
2. It looks for a nib file whose name matches the name of the view controller class. For example, if the class name is `MyViewController`, it looks for a `MyViewController.nib` file.

> **Note**:  Nib names that include a platform-specific identifier such as `~iphone` or `~ipad` are loaded only on a device of the corresponding type. For example, a nib name of `MyViewController~ipad.nib` is loaded only on iPad. If your app supports both platform types, you must provide versions of your nib files for each platform.

 Nib names that include a platform-specific identifier such as `~iphone` or `~ipad` are loaded only on a device of the corresponding type. For example, a nib name of `MyViewController~ipad.nib` is loaded only on iPad. If your app supports both platform types, you must provide versions of your nib files for each platform.

## See Also

- [init(nibName: String?, bundle: Bundle?)](uiviewcontroller/init(nibname:bundle:).md)
  Creates a view controller with the nib file in the specified bundle.
- [var storyboard: UIStoryboard?](uiviewcontroller/storyboard.md)
  The storyboard from which the view controller originated.
- [var nibBundle: Bundle?](uiviewcontroller/nibbundle.md)
  The view controller’s nib bundle if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/nibname)*