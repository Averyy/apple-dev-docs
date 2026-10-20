# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delegate of the scroll view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UIScrollViewDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UIScrollViewDelegate> delegate;
```

#### Discussion

The delegate must adopt the [`UIScrollViewDelegate`](../uiscrollviewdelegate.md) protocol. The [`UIScrollView`](../uiscrollview.md) class, which doesn’t retain the delegate, invokes each protocol method the delegate implements.

## See Also

### Responding to scroll view interactions
- [protocol UIScrollViewDelegate](../uiscrollviewdelegate.md)
  The interface for the delegate of a scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/delegate)*