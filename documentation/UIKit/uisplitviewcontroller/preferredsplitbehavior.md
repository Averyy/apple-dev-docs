# preferredSplitBehavior

**Framework**: UIKit  
**Kind**: property

The preferred behavior that determines how the child view controllers appear in relation to each other.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredSplitBehavior: UISplitViewController.SplitBehavior { get set }
```

#### Discussion

Use this property to specify the split behavior that you prefer to use. The split view controller makes every effort to adopt the behavior you specify, but may use a different type of interface if there isn’t enough space to support your preferred choice. If changing the value of this property leads to an actual change in the current split behavior, the split view controller reflects the actual split behavior in the [`splitBehavior`](uisplitviewcontroller/splitbehavior-swift.property.md) property. This change takes effect after the next layout occurs.

You do not set the split behavior directly; instead, you set a preferred split behavior by using the [`preferredSplitBehavior`](uisplitviewcontroller/preferredsplitbehavior.md) property. This change takes effect after the next layout occurs. The split view controller reflects the actual split behavior in the [`splitBehavior`](uisplitviewcontroller/splitbehavior-swift.property.md) property. The value of the [`splitBehavior`](uisplitviewcontroller/splitbehavior-swift.property.md) property affects which display modes are available for the split view controller. For possible configurations, see [`UISplitViewController.SplitBehavior`](uisplitviewcontroller/splitbehavior-swift.enum.md).

Setting the value of this property to [`UISplitViewController.SplitBehavior.automatic`](uisplitviewcontroller/splitbehavior-swift.enum/automatic.md) causes the split view controller to choose the most appropriate display mode for the currently available space. The default value of this property is [`UISplitViewController.SplitBehavior.automatic`](uisplitviewcontroller/splitbehavior-swift.enum/automatic.md).

## See Also

- [var splitBehavior: UISplitViewController.SplitBehavior](uisplitviewcontroller/splitbehavior-swift.property.md)
  The current behavior that determines how the child view controllers appear in relation to each other.
- [UISplitViewController.SplitBehavior](uisplitviewcontroller/splitbehavior-swift.enum.md)
  Constants that describe the possible ways that the child view controllers appear in relation to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/preferredsplitbehavior)*