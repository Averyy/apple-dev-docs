# current

**Framework**: UIKit  
**Kind**: property

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

#### Discussion

This property provides a way to get a trait collection from the currently updating trait environment when your code doesn’t have direct access to the trait environment. UIKit updates the value of this property before calling the following methods of [`UIView`](uiview.md), [`UIViewController`](uiviewcontroller.md), and [`UIPresentationController`](uipresentationcontroller.md). Inside these methods, the trait collection contains the traits describing the currently updating view or controller.

The following table lists the supported methods where UIKit sets the [`current`](uitraitcollection/current.md) value:

| [`UIView`](uiview.md) | [`UIViewController`](uiviewcontroller.md) | [`UIPresentationController`](uipresentationcontroller.md) |
| --- | --- | --- |
| [`draw(_:)`](uiview/draw(_:).md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`layoutSubviews()`](uiview/layoutsubviews().md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`tintColorDidChange()`](uiview/tintcolordidchange().md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `action` method of [`registerForTraitChanges(_:target:action:)`](uitraitchangeobservable-67e94/registerfortraitchanges(_:target:action:).md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `handler` closure of [`registerForTraitChanges(_:handler:)`](uitraitchangeobservable-67e94/registerfortraitchanges(_:handler:).md)  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`traitCollectionDidChange(_:)`](uitraitenvironment/traitcollectiondidchange(_:).md) | [`viewWillLayoutSubviews()`](uiviewcontroller/viewwilllayoutsubviews().md)  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`viewDidLayoutSubviews()`](uiviewcontroller/viewdidlayoutsubviews().md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `action` method of [`registerForTraitChanges(_:target:action:)`](uitraitchangeobservable-67e94/registerfortraitchanges(_:target:action:).md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `handler` closure of [`registerForTraitChanges(_:handler:)`](uitraitchangeobservable-67e94/registerfortraitchanges(_:handler:).md)  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`traitCollectionDidChange(_:)`](uitraitenvironment/traitcollectiondidchange(_:).md) | [`containerViewWillLayoutSubviews()`](uipresentationcontroller/containerviewwilllayoutsubviews().md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`containerViewDidLayoutSubviews()`](uipresentationcontroller/containerviewdidlayoutsubviews().md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `action` method of [`registerForTraitChanges(_:target:action:)`](uitraitchangeobservable-67e94/registerfortraitchanges(_:target:action:).md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `handler` closure of [`registerForTraitChanges(_:handler:)`](uitraitchangeobservable-67e94/registerfortraitchanges(_:handler:).md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`traitCollectionDidChange(_:)`](uitraitenvironment/traitcollectiondidchange(_:).md) |

Outside these methods, you’re responsible for ensuring the [`current`](uitraitcollection/current.md) property has a valid trait collection. Otherwise, the contents of the collection are undefined. To ensure that [`current`](uitraitcollection/current.md) contains a valid trait collection, use one of these techniques:

- Use [`performAsCurrent(_:)`](uitraitcollection/performascurrent(_:).md) to execute your code inside a context with a valid [`current`](uitraitcollection/current.md) property. This is the preferred way to set [`current`](uitraitcollection/current.md).
- Set [`current`](uitraitcollection/current.md) to a known good trait collection. If you set [`current`](uitraitcollection/current.md), you need to save and restore the trait environment, as the code example below shows.

[`UIColor`](uicolor.md) implicitly uses the [`current`](uitraitcollection/current.md) trait collection when it resolves a dynamic color to a static color value, such as a [`CGColor`](https://developer.apple.com/documentation/CoreGraphics/CGColor) or an RGB value. To resolve a dynamic color, make sure that [`current`](uitraitcollection/current.md) contains a valid collection. Alternatively, the method [`resolvedColor(with:)`](uicolor/resolvedcolor(with:).md) resolves a color from a given trait collection and doesn’t rely on [`current`](uitraitcollection/current.md).

UIKit stores the value of the [`current`](uitraitcollection/current.md) property as a thread-local variable, so access is lightweight and free of side effects. Changing the traits on a nonmain thread doesn’t affect the current traits on your app’s main thread.

Whenever possible, use [`performAsCurrent(_:)`](uitraitcollection/performascurrent(_:).md) rather than manually setting [`current`](uitraitcollection/current.md). If you need to set [`current`](uitraitcollection/current.md), keep the following in mind:

- Before modifying [`current`](uitraitcollection/current.md), save the value, and restore it after you’re done.
- Always start with a trait collection from a concrete instance of [`UITraitEnvironment`](uitraitenvironment.md) rather than creating a new [`UITraitCollection`](uitraitcollection.md) instance.

The [`performAsCurrent(_:)`](uitraitcollection/performascurrent(_:).md) method handles these tasks for you.

The example below sets the [`current`](uitraitcollection/current.md) property to resolve a dynamic color into a [`CGColor`](https://developer.apple.com/documentation/CoreGraphics/CGColor):

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