# UIViewAnimatingPosition

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating positions within the animation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum UIViewAnimatingPosition
```

```c
enum UIViewAnimatingPosition : NSInteger;
```

## Topics

### Constants
- [UIViewAnimatingPosition.end](./uiviewanimatingposition/end.md)
  The end point of the animation. Use this constant when you want the final values for any animatable properties—that is, you want to refer to the values you specified in your animation blocks.
- [UIViewAnimatingPosition.start](./uiviewanimatingposition/start.md)
  The beginning of the animation. Use this constant when you want the starting values for any animatable properties—that is, the values of the properties before you applied any animations.
- [UIViewAnimatingPosition.current](./uiviewanimatingposition/current.md)
  The current position. Use this constant when you want the most recent value set by an animator object.
### Initializers
- [init?(rawValue: Int)](./uiviewanimatingposition/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum UIViewAnimatingState](./uiviewanimatingstate.md)
  Constants indicating the current state of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimatingposition)*