# isViewLoaded

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view is currently loaded into memory.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isViewLoaded: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isViewLoaded) BOOL viewLoaded;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the view is in memory or [`false`](../../Swift/false.md) when it is not. Accessing this property does not attempt to load the view if it is not currently in memory.

## See Also

### Managing the view
- [var view: UIView!](./view.md)
  The view that the controller manages.
- [var viewIfLoaded: UIView?](./viewifloaded.md)
  The view controller’s view, or `nil` if the view isn’t yet loaded.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/isviewloaded)*