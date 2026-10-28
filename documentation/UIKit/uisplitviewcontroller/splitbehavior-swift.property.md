# splitBehavior

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current behavior that determines how the child view controllers appear in relation to each other.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var splitBehavior: UISplitViewController.SplitBehavior { get }
```

```objc
@property (nonatomic, readonly) UISplitViewControllerSplitBehavior splitBehavior;
```

## Discussion

This property controls how a split view controller’s secondary view controller appears in relation to the other child view controllers. To change the current split behavior, change the value of the [`preferredSplitBehavior`](./preferredsplitbehavior.md) property.

The value of this property affects which display modes are available for the split view interface. For possible configurations, see [`UISplitViewController.SplitBehavior`](./splitbehavior-swift.enum.md).

## See Also

### Managing the split behavior
- [var preferredSplitBehavior: UISplitViewController.SplitBehavior](./preferredsplitbehavior.md)
  The preferred behavior that determines how the child view controllers appear in relation to each other.
- [UISplitViewController.SplitBehavior](./splitbehavior-swift.enum.md)
  Constants that describe the possible ways that the child view controllers appear in relation to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/splitbehavior-swift.property)*