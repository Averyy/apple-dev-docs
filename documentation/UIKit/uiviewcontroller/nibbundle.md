# nibBundle

**Framework**: UIKit  
**Kind**: property

The view controller’s nib bundle if it exists.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var nibBundle: Bundle? { get }
```

## See Also

- [init(nibName: String?, bundle: Bundle?)](uiviewcontroller/init(nibname:bundle:).md)
  Creates a view controller with the nib file in the specified bundle.
- [var storyboard: UIStoryboard?](uiviewcontroller/storyboard.md)
  The storyboard from which the view controller originated.
- [var nibName: String?](uiviewcontroller/nibname.md)
  The name of the view controller’s nib file, if one was specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/nibbundle)*