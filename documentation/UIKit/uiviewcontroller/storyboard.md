# storyboard

**Framework**: UIKit  
**Kind**: property

The storyboard from which the view controller originated.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var storyboard: UIStoryboard? { get }
```

#### Discussion

If the view controller was not instantiated from a storyboard, this property is `nil`.

## See Also

- [var nibName: String?](uiviewcontroller/nibname.md)
  The name of the view controller’s nib file, if one was specified.
- [var nibBundle: Bundle?](uiviewcontroller/nibbundle.md)
  The view controller’s nib bundle if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/storyboard)*