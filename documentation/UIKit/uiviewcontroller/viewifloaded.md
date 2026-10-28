# viewIfLoaded

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view controller’s view, or `nil` if the view isn’t yet loaded.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var viewIfLoaded: UIView? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIView * viewIfLoaded;
```

## Discussion

If the view controller’s view has already been loaded, this property contains that view. If the view has not yet been loaded, this property is set to `nil`.

## See Also

### Managing the view
- [var view: UIView!](./view.md)
  The view that the controller manages.
- [var isViewLoaded: Bool](./isviewloaded.md)
  A Boolean value indicating whether the view is currently loaded into memory.
- [func loadView()](./loadview%28%29.md)
  Creates the view that the controller manages.
- [func viewDidLoad()](./viewdidload%28%29.md)
  Called after the controller’s view is loaded into memory.
- [func loadViewIfNeeded()](./loadviewifneeded%28%29.md)
  Loads the view controller’s view if it’s not loaded yet.
- [var title: String?](./title.md)
  A localized string that represents the view this controller manages.
- [var preferredContentSize: CGSize](./preferredcontentsize.md)
  The preferred size for the view controller’s view.
- [var ornaments: [UIOrnament]](./ornaments.md)
  SwiftUI ornaments to display adjacent to the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/viewifloaded)*