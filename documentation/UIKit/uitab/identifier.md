# identifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A string identifier for a tab.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (nonatomic, strong, readonly) NSString * identifier;
```

#### Discussion

Each identifier must be unique across all the tabs managed by a [`UITabBarController`](../uitabbarcontroller.md).

## See Also

### Accessing a tab’s appearance
- [var title: String](./title.md)
  A tab’s title.
- [var subtitle: String?](./subtitle.md)
  A tab’s subtitle.
- [var image: UIImage?](./image.md)
  A tab’s image.
- [var badgeValue: String?](./badgevalue.md)
  A tab’s badge value.
- [var viewController: UIViewController?](./viewcontroller.md)
  The view controller that the system presents when someone selects a tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitab/identifier)*