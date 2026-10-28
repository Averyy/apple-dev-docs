# UIScrollViewDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The interface for the delegate of a scroll view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
@MainActor
protocol UIScrollViewDelegate : NSObjectProtocol
```

```objc
@protocol UIScrollViewDelegate <NSObject>
```

## Overview

The methods that the [`UIScrollViewDelegate`](./uiscrollviewdelegate.md) protocol declares allow the adopting delegate to respond to messages from the [`UIScrollView`](./uiscrollview.md) class. The delegate responds to and affects operations like scrolling, zooming, deceleration of scrolled content, and scrolling animations.

## Topics

### Responding to scrolling and dragging
- [func scrollViewDidScroll(UIScrollView)](./uiscrollviewdelegate/scrollviewdidscroll%28_%29.md)
  Tells the delegate when the user scrolls the content view within the scroll view.
- [func scrollViewWillBeginDragging(UIScrollView)](./uiscrollviewdelegate/scrollviewwillbegindragging%28_%29.md)
  Tells the delegate when the scroll view is about to start scrolling the content.
- [func scrollViewWillEndDragging(UIScrollView, withVelocity: CGPoint, targetContentOffset: UnsafeMutablePointer<CGPoint>)](./uiscrollviewdelegate/scrollviewwillenddragging%28_,withvelocity,targetcontentoffset%29.md)
  Tells the delegate when the user finishes scrolling the content.
- [func scrollViewDidEndDragging(UIScrollView, willDecelerate: Bool)](./uiscrollviewdelegate/scrollviewdidenddragging%28_,willdecelerate%29.md)
  Tells the delegate when dragging ended in the scroll view.
- [func scrollViewShouldScrollToTop(UIScrollView) -> Bool](./uiscrollviewdelegate/scrollviewshouldscrolltotop%28_%29.md)
  Asks the delegate if the scroll view should scroll to the top of the content.
- [func scrollViewDidScrollToTop(UIScrollView)](./uiscrollviewdelegate/scrollviewdidscrolltotop%28_%29.md)
  Tells the delegate that the scroll view scrolled to the top of the content.
- [func scrollViewWillBeginDecelerating(UIScrollView)](./uiscrollviewdelegate/scrollviewwillbegindecelerating%28_%29.md)
  Tells the delegate that the scroll view is starting to decelerate the scrolling movement.
- [func scrollViewDidEndDecelerating(UIScrollView)](./uiscrollviewdelegate/scrollviewdidenddecelerating%28_%29.md)
  Tells the delegate that the scroll view ended decelerating the scrolling movement.
### Managing zooming
- [func viewForZooming(in: UIScrollView) -> UIView?](./uiscrollviewdelegate/viewforzooming%28in%29.md)
  Asks the delegate for the view to scale when zooming is about to occur in the scroll view.
- [func scrollViewWillBeginZooming(UIScrollView, with: UIView?)](./uiscrollviewdelegate/scrollviewwillbeginzooming%28_,with%29.md)
  Tells the delegate that zooming of the content in the scroll view is about to commence.
- [func scrollViewDidEndZooming(UIScrollView, with: UIView?, atScale: CGFloat)](./uiscrollviewdelegate/scrollviewdidendzooming%28_,with,atscale%29.md)
  Tells the delegate when zooming of the content in the scroll view completed.
- [func scrollViewDidZoom(UIScrollView)](./uiscrollviewdelegate/scrollviewdidzoom%28_%29.md)
  Tells the delegate that the scroll view’s zoom factor changed.
### Responding to scrolling animations
- [func scrollViewDidEndScrollingAnimation(UIScrollView)](./uiscrollviewdelegate/scrollviewdidendscrollinganimation%28_%29.md)
  Tells the delegate when a scrolling animation in the scroll view concludes.
### Responding to inset changes
- [func scrollViewDidChangeAdjustedContentInset(UIScrollView)](./uiscrollviewdelegate/scrollviewdidchangeadjustedcontentinset%28_%29.md)
  Tells the delegate when the scroll view’s inset values change.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [UICollectionViewDelegate](./uicollectionviewdelegate.md)
- [UICollectionViewDelegateFlowLayout](./uicollectionviewdelegateflowlayout.md)
- [UIScrollViewAccessibilityDelegate](./uiscrollviewaccessibilitydelegate.md)
- [UITableViewDelegate](./uitableviewdelegate.md)
- [UITextViewDelegate](./uitextviewdelegate.md)
### Conforming Types
- [UICollectionViewController](./uicollectionviewcontroller.md)
- [UITableViewController](./uitableviewcontroller.md)
- [UIWebView](./uiwebview.md)

## See Also

### Responding to scroll view interactions
- [var delegate: (any UIScrollViewDelegate)?](./uiscrollview/delegate.md)
  The delegate of the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate)*