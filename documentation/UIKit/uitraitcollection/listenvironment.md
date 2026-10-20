# listEnvironment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The list environment represents whether a given trait collection is from a view in a UITableView or a UICollectionView list section.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var listEnvironment: UIListEnvironment { get }
```

```objc
@property (nonatomic, readonly) UIListEnvironment listEnvironment;
```

## See Also

### Retrieving layout environment traits
- [enum UIListEnvironment](../uilistenvironment.md)
  Constants that indicate the style of the containing list in a collection view or table view.
- [var splitViewControllerLayoutEnvironment: UISplitViewController.LayoutEnvironment](./splitviewcontrollerlayoutenvironment.md)
  The split view controller layout environment represents whether an ancestor split view controller is expanded or collapsed.
- [UISplitViewController.LayoutEnvironment](../uisplitviewcontroller/layoutenvironment.md)
  Constants that indicate the current layout of the containing split view controller.
- [var tabAccessoryEnvironment: UITabAccessory.Environment](./tabaccessoryenvironment.md)
  The tab accessory environment represents whether a given trait collection is from a view in a `UITabAccessory` content view.
- [UITabAccessory.Environment](../uitabaccessory/environment.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/listenvironment)*