# previousLocation(in:)

**Framework**: UIKit  
**Kind**: method

Returns the previous location of the touch in the coordinate system of the given node.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func previousLocation(in node: SKNode) -> CGPoint
```

#### Return Value

The location of the touch in the node’s coordinate system.

## Parameters

- `node`: A node that is a descendant of a scene presented in the window that received the touch event.

## See Also

- [func location(in: SKNode) -> CGPoint](uitouch/location(in:)-44h4k.md)
  Returns the current location of the touch in the coordinate system of the given node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/previouslocation(in:)-ea29)*