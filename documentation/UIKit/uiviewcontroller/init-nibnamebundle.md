# init(nibName:bundle:)

**Framework**: UIKit  
**Kind**: init

Creates a view controller with the nib file in the specified bundle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?)
```

#### Return Value

A newly initialized [`UIViewController`](uiviewcontroller.md) object.

#### Discussion

This is the designated initializer for this class. When using a storyboard to define your view controller and its associated views, you never initialize your view controller class directly. Instead, view controllers are instantiated by the storyboard either automatically when a segue is triggered or programmatically when your app calls the [`instantiateViewController(withIdentifier:)`](uistoryboard/instantiateviewcontroller(withidentifier:).md) method of a storyboard object. When instantiating a view controller from a storyboard, iOS initializes the new view controller by calling its doc://com.apple.documentation/documentation/oslog/oslogentry/init(coder:) method instead of this method and sets the [`nibName`](uiviewcontroller/nibname.md) property to a nib file stored inside the storyboard.

The nib file you specify is not loaded right away. It is loaded the first time the view controller’s view is accessed. If you want to perform additional initialization after the nib file is loaded, override the [`viewDidLoad()`](uiviewcontroller/viewdidload().md) method and perform your tasks there.

If you specify `nil` for the `nibName` parameter and you do not override the [`loadView()`](uiviewcontroller/loadview().md) method, the view controller searches for a nib file as described in the [`nibName`](uiviewcontroller/nibname.md) property.

For more information about how a view controller loads its view, see [`View Controller Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457).

## Parameters

- `nibNameOrNil`: The name of the nib file to associate with the view controller. The nib file name should not contain any leading path information. If you specify  , the   property is set to  .
- `nibBundleOrNil`: The bundle in which to search for the nib file. This method looks for the nib file in the bundle’s language-specific project directories first, followed by the Resources directory.

## See Also

- [func loadView()](uiviewcontroller/loadview.md)
  Creates the view that the controller manages.
- [var nibBundle: Bundle?](uiviewcontroller/nibbundle.md)
  The view controller’s nib bundle if it exists.
- [var nibName: String?](uiviewcontroller/nibname.md)
  The name of the view controller’s nib file, if one was specified.
- [var storyboard: UIStoryboard?](uiviewcontroller/storyboard.md)
  The storyboard from which the view controller originated.
- [init?(coder: NSCoder)](uiviewcontroller/init(coder:).md)
  Creates a view controller with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/init(nibname:bundle:))*