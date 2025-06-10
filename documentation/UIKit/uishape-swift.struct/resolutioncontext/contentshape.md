# contentShape

**Framework**: UIKit  
**Kind**: property

The resolved shape of the content to which this shape can apply.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS 1.0+

## Declaration

```swift
var contentShape: UIShape.Resolved
```

#### Discussion

For example, if this shape applies an effect to a button, the [`contentShape`](uishape-swift.struct/resolutioncontext/contentshape.md) might represent the bounding shape of that button’s background. You typically size a dynamic shape relative to the bounding rectangle of the [`contentShape`](uishape-swift.struct/resolutioncontext/contentshape.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishape-swift.struct/resolutioncontext/contentshape)*