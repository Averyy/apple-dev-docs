# previousLocation(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the previous location of the touch in the coordinate system of the given node.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func previousLocation(in node: SKNode) -> CGPoint
```

```objc
- (CGPoint) previousLocationInNode:(SKNode *) node;
```

#### Return Value

The location of the touch in the node’s coordinate system.

## Parameters

- `node`: A node that is a descendant of a scene presented in the window that received the touch event.

## See Also

### Working with touch events in SpriteKit
- [func location(in: SKNode) -> CGPoint](./location%28in%29-44h4k.md)
  Returns the current location of the touch in the coordinate system of the given node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/previouslocation(in:)-ea29)*