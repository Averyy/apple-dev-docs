# performAsCurrent(_:)

**Framework**: UIKit  
**Kind**: method

Executes custom code using the traits of the receiving trait collection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func performAsCurrent(_ actions: () -> Void)
```

#### Discussion

The [`current`](uitraitcollection/current.md) property is undefined outside the documented methods where UIKit sets it. Use this method when you want to execute code that relies on the [`current`](uitraitcollection/current.md) property from outside these methods. You can also use this method if you want to execute some code using the traits of a different trait environment. Prefer this method over manually setting the [`current`](uitraitcollection/current.md) property yourself.

This method temporarily replaces the traits of the current environment with the ones in the targeted [`UITraitCollection`](uitraitcollection.md). After the `actions` block finishes, the method restores the original traits to the environment. You can call this method from any thread of your app.

The example below shows how you can safely resolve dynamic [`UIColor`](uicolor.md) that relies on [`current`](uitraitcollection/current.md):

```swift
func updateBorderColor(layer: CALayer) {
    
    // Read the trait collection from the view.
    let traitCollection = view.traitCollection
    traitCollection.performAsCurrent {
        // Inside the closure, the current property is set to traitCollection,
        // which UIColor uses to resolve the dynamic color borderColor.
        layer.borderColor = UIColor.label.cgColor
    }
}
```

## Parameters

- `actions`: A closure containing the code you want to execute. This closure has no return value and takes no parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/performascurrent(_:))*