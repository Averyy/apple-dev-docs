# location(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the current location of the touch in the coordinate system of the given node.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func location(in node: SKNode) -> CGPoint
```

```objc
- (CGPoint) locationInNode:(SKNode *) node;
```

## Return Value

The location of the touch in the node’s coordinate system.

## Parameters

- `node`: A node that is a descendant of a scene presented in the window that received the touch event.

## See Also

### Working with touch events in SpriteKit
- [func previousLocation(in: SKNode) -> CGPoint](./previouslocation%28in%29-ea29.md)
  Returns the previous location of the touch in the coordinate system of the given node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/location(in:)-44h4k)*