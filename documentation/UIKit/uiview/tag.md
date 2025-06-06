# tag

**Framework**: UIKit  
**Kind**: property

An integer that you can use to identify view objects in your application.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var tag: Int { get set }
```

#### Discussion

The default value is `0`. You can set the value of this tag and use that value to identify the view later.

## See Also

- [func viewWithTag(Int) -> UIView?](uiview/viewwithtag(_:).md)
  Returns the view whose tag matches the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/tag)*