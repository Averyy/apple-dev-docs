# traitCollectionDidChange(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Reports changes in the iOS interface environment.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0
- iPadOS 8.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- tvOS - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: In Swift, use [`registerForTraitChanges(_:handler:)`](../uitraitchangeobservable-67e94/registerfortraitchanges%28_,handler%29.md) or [`registerForTraitChanges(_:target:action:)`](../uitraitchangeobservable-67e94/registerfortraitchanges%28_,target,action%29.md) instead. In Objective-C, use [`registerForTraitChanges:withHandler:`](../uitraitchangeobservable-7qoet/registerfortraitchanges_withhandler_.md) or [`registerForTraitChanges:withTarget:action:`](../uitraitchangeobservable-7qoet/registerfortraitchanges_withtarget_action_.md) instead.

## Declaration

```swift
func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?)
```

```objc
- (void) traitCollectionDidChange:(UITraitCollection *) previousTraitCollection;
```

## Mentions

- [Adapting your app when traits change](../adapting-your-app-when-traits-change.md)
- [Checking the availability of 3D Touch](../checking-the-availability-of-3d-touch.md)
- [Responding to changing display modes on Apple TV](../responding-to-changing-display-modes-on-apple-tv.md)
- [Scaling fonts automatically](../scaling-fonts-automatically.md)

## Discussion

The system calls this method when the iOS interface environment changes. Implement this method in view controllers and views, according to your app’s needs, to respond to such changes. For example, you might adjust the layout of the subviews of a view controller when someone rotates from portrait to landscape orientation. The default implementation of this method is empty.

At the beginning of your implementation, call `super` to ensure that interface elements higher in the view hierarchy have an opportunity to adjust their layout first. Use code similar to this:

```objc
- (void) traitCollectionDidChange: (UITraitCollection *) previousTraitCollection {
    [super traitCollectionDidChange: previousTraitCollection];
    if ((self.traitCollection.verticalSizeClass != previousTraitCollection.verticalSizeClass)
        || (self.traitCollection.horizontalSizeClass != previousTraitCollection.horizontalSizeClass)) {
        // Your custom implementation here.
    }
}
```

## Parameters

- `previousTraitCollection`: The [`UITraitCollection`](../uitraitcollection.md) object before the interface environment changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitenvironment/traitcollectiondidchange(_:))*