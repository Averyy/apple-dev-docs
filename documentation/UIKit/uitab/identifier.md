# identifier

**Framework**: UIKit  
**Kind**: property

A string identifier for a tab.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var identifier: String { get }
```

#### Discussion

Each identifier must be unique across all the tabs managed by a [`UITabBarController`](uitabbarcontroller.md).

## See Also

- [var title: String](uitab/title.md)
  A tab’s title.
- [var subtitle: String?](uitab/subtitle.md)
  A tab’s subtitle.
- [var image: UIImage?](uitab/image.md)
  A tab’s image.
- [var badgeValue: String?](uitab/badgevalue.md)
  A tab’s badge value.
- [var viewController: UIViewController?](uitab/viewcontroller.md)
  The view controller that the system presents when someone selects a tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitab/identifier)*