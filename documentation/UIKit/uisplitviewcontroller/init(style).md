# init(style:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a split view controller with the specified column style.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(style: UISplitViewController.Style)
```

```objc
- (instancetype) initWithStyle:(UISplitViewControllerStyle) style;
```

## Parameters

- `style`: The split view controller’s style, which describes how many columns the split view controller displays. You can pass in any of the [`UISplitViewController.Style`](./style-swift.enum.md) values except [`UISplitViewController.Style.unspecified`](./style-swift.enum/unspecified.md).

## See Also

### Creating a split view controller
- [init(nibName: String?, bundle: Bundle?)](./init%28nibname,bundle%29.md)
  Creates a split view controller with the nib file in the specified bundle.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a split view controller from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/init(style:))*