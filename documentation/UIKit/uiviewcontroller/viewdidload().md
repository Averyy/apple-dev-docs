# viewDidLoad()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called after the controller’s view is loaded into memory.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func viewDidLoad()
```

```objc
- (void) viewDidLoad;
```

## Mentions

- [Displaying and managing views with a view controller](../displaying-and-managing-views-with-a-view-controller.md)
- [Customizing a document-based app’s launch experience](../customizing-a-document-based-app-s-launch-experience.md)
- [Making a view into a drag source](../making-a-view-into-a-drag-source.md)

## Discussion

This method is called after the view controller has loaded its view hierarchy into memory. This method is called regardless of whether the view hierarchy was loaded from a nib file or created programmatically in the [`loadView()`](./loadview%28%29.md) method. You usually override this method to perform additional initialization on views that were loaded from nib files.

## See Also

### Managing the view
- [var view: UIView!](./view.md)
  The view that the controller manages.
- [var viewIfLoaded: UIView?](./viewifloaded.md)
  The view controller’s view, or `nil` if the view isn’t yet loaded.
- [var isViewLoaded: Bool](./isviewloaded.md)
  A Boolean value indicating whether the view is currently loaded into memory.
- [func loadView()](./loadview%28%29.md)
  Creates the view that the controller manages.
- [func loadViewIfNeeded()](./loadviewifneeded%28%29.md)
  Loads the view controller’s view if it’s not loaded yet.
- [var title: String?](./title.md)
  A localized string that represents the view this controller manages.
- [var preferredContentSize: CGSize](./preferredcontentsize.md)
  The preferred size for the view controller’s view.
- [var ornaments: [UIOrnament]](./ornaments.md)
  SwiftUI ornaments to display adjacent to the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/viewdidload())*