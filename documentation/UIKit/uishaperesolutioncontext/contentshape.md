# contentShape

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The resolved shape of the content to which this shape can apply.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) UIResolvedShape * contentShape;
```

#### Discussion

For example, if this shape applies an effect to a button, the [`contentShape`](./contentshape.md) might represent the bounding shape of that button’s background. You typically size a dynamic shape relative to the bounding rectangle of the [`contentShape`](./contentshape.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uishaperesolutioncontext/contentshape)*