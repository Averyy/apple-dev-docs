# init(items:)

**Framework**: UIKit  
**Kind**: init

Creates a segmented control with segments having the given titles or images.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
init(items: [Any]?)
```

#### Return Value

A `UISegmentedControl` object or `nil` if there was a problem in initializing the object.

#### Discussion

The system automatically sizes the returned segmented control to fit its content within the width of its superview.

## Parameters

- `items`: An array of [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) objects (for segment titles), [`UIImage`](uiimage.md) objects (for segment images), or in iOS 14.0 and later [`UIAction`](uiaction.md) objects.

## See Also

- [convenience init(frame: CGRect, actions: [UIAction])](uisegmentedcontrol/init(frame:actions:).md)
  Creates a segmented control with the given frame and adds segments for the actions you specify.
- [init(frame: CGRect)](uisegmentedcontrol/init(frame:).md)
  Creates an empty segmented control with the frame you specify.
- [init?(coder: NSCoder)](uisegmentedcontrol/init(coder:).md)
  Creates a segmented control with data from an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/init(items:))*