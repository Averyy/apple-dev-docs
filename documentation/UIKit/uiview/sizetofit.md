# sizeToFit()

**Framework**: UIKit  
**Kind**: method

Resizes and moves the receiver view so it just encloses its subviews.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func sizeToFit()
```

## Mentions

- [Displaying a checkbox in your Mac app built with Mac Catalyst](displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md)

#### Discussion

Call this method when you want to resize the current view so that it uses the most appropriate amount of space. Specific UIKit views resize themselves according to their own internal needs. In some cases, if a view does not have a superview, it may size itself to the screen bounds. Thus, if you want a given view to size itself to its parent view, you should add it to the parent view before calling this method.

You should not override this method. If you want to change the default sizing information for your view, override the [`sizeThatFits(_:)`](uiview/sizethatfits(_:).md) instead. That method performs any needed calculations and returns them to this method, which then makes the change.

## See Also

- [var contentMode: UIView.ContentMode](uiview/contentmode-swift.property.md)
  A flag used to determine how a view lays out its content when its bounds change.
- [UIView.ContentMode](uiview/contentmode-swift.enum.md)
  Options to specify how a view adjusts its content when its size changes.
- [func sizeThatFits(CGSize) -> CGSize](uiview/sizethatfits(_:).md)
  Asks the view to calculate and return the size that best fits the specified size.
- [var autoresizesSubviews: Bool](uiview/autoresizessubviews.md)
  A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.
- [var autoresizingMask: UIView.AutoresizingMask](uiview/autoresizingmask-swift.property.md)
  An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/sizetofit())*