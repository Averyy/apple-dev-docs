# current

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The trait collection for the current execution context.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class var current: UITraitCollection { get set }
```

```objc
@property (class, nonatomic, strong) UITraitCollection * currentTraitCollection;
```

## Discussion

This property provides a way to get a trait collection from the currently updating trait environment when your code doesn’t have direct access to the trait environment. UIKit updates the value of this property before calling the following methods of [`UIView`](../uiview.md), [`UIViewController`](../uiviewcontroller.md), and [`UIPresentationController`](../uipresentationcontroller.md). Inside these methods, the trait collection contains the traits describing the currently updating view or controller.

The following table lists the supported methods where UIKit sets the [`current`](./current.md) value:

| [`UIView`](../uiview.md) | [`UIViewController`](../uiviewcontroller.md) | [`UIPresentationController`](../uipresentationcontroller.md) |
| --- | --- | --- |
| [`draw(_:)`](../uiview/draw%28_%29.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`layoutSubviews()`](../uiview/layoutsubviews%28%29.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`tintColorDidChange()`](../uiview/tintcolordidchange%28%29.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) The `action` method of [`registerForTraitChanges(_:target:action:)`](../uitraitchangeobservable-67e94/registerfortraitchanges%28_,target,action%29.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) The `handler` closure of [`registerForTraitChanges(_:handler:)`](../uitraitchangeobservable-67e94/registerfortraitchanges%28_,handler%29.md)  ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`traitCollectionDidChange(_:)`](../uitraitenvironment/traitcollectiondidchange%28_%29.md) | [`viewWillLayoutSubviews()`](../uiviewcontroller/viewwilllayoutsubviews%28%29.md)  ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`viewDidLayoutSubviews()`](../uiviewcontroller/viewdidlayoutsubviews%28%29.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) The `action` method of [`registerForTraitChanges(_:target:action:)`](../uitraitchangeobservable-67e94/registerfortraitchanges%28_,target,action%29.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) The `handler` closure of [`registerForTraitChanges(_:handler:)`](../uitraitchangeobservable-67e94/registerfortraitchanges%28_,handler%29.md)  ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`traitCollectionDidChange(_:)`](../uitraitenvironment/traitcollectiondidchange%28_%29.md) | [`containerViewWillLayoutSubviews()`](../uipresentationcontroller/containerviewwilllayoutsubviews%28%29.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`containerViewDidLayoutSubviews()`](../uipresentationcontroller/containerviewdidlayoutsubviews%28%29.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) The `action` method of [`registerForTraitChanges(_:target:action:)`](../uitraitchangeobservable-67e94/registerfortraitchanges%28_,target,action%29.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) The `handler` closure of [`registerForTraitChanges(_:handler:)`](../uitraitchangeobservable-67e94/registerfortraitchanges%28_,handler%29.md) ![](https://developer.apple.com/tutorials/images/com.apple.uikit/spacer.png) [`traitCollectionDidChange(_:)`](../uitraitenvironment/traitcollectiondidchange%28_%29.md) |

Outside these methods, you’re responsible for ensuring the [`current`](./current.md) property has a valid trait collection. Otherwise, the contents of the collection are undefined. To ensure that [`current`](./current.md) contains a valid trait collection, use one of these techniques:

- Use [`performAsCurrent(_:)`](./performascurrent%28_%29.md) to execute your code inside a context with a valid [`current`](./current.md) property. This is the preferred way to set [`current`](./current.md).
- Set [`current`](./current.md) to a known good trait collection. If you set [`current`](./current.md), you need to save and restore the trait environment, as the code example below shows.

[`UIColor`](../uicolor.md) implicitly uses the [`current`](./current.md) trait collection when it resolves a dynamic color to a static color value, such as a [`CGColor`](../../CoreGraphics/cgcolor.md) or an RGB value. To resolve a dynamic color, make sure that [`current`](./current.md) contains a valid collection. Alternatively, the method [`resolvedColor(with:)`](../uicolor/resolvedcolor%28with%29.md) resolves a color from a given trait collection and doesn’t rely on [`current`](./current.md).

UIKit stores the value of the [`current`](./current.md) property as a thread-local variable, so access is lightweight and free of side effects. Changing the traits on a nonmain thread doesn’t affect the current traits on your app’s main thread.

Whenever possible, use [`performAsCurrent(_:)`](./performascurrent%28_%29.md) rather than manually setting [`current`](./current.md). If you need to set [`current`](./current.md), keep the following in mind:

- Before modifying [`current`](./current.md), save the value, and restore it after you’re done.
- Always start with a trait collection from a concrete instance of [`UITraitEnvironment`](../uitraitenvironment.md) rather than creating a new [`UITraitCollection`](../uitraitcollection.md) instance.

The [`performAsCurrent(_:)`](./performascurrent%28_%29.md) method handles these tasks for you.

The example below sets the [`current`](./current.md) property to resolve a dynamic color into a [`CGColor`](../../CoreGraphics/cgcolor.md):

```swift
func updateBorderColor(layer: CALayer) {
    let savedTraitCollection = UITraitCollection.current
    // Set the property with a trait collection from a view.
    UITraitCollection.current = view.traitCollection
    // Methods and properties relying on current are safe to use here.
    layer.borderColor = UIColor.label.cgColor
    // Restore the saved collection.
    UITraitCollection.current = savedTraitCollection
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/current)*