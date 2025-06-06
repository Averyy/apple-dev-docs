# location(in:)

**Framework**: UIKit  
**Kind**: method

Returns the current location of the touch in the coordinate system of the given node.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func location(in node: SKNode) -> CGPoint
```

#### Return Value

The location of the touch in the node’s coordinate system.

## Parameters

- `node`: A node that is a descendant of a scene presented in the window that received the touch event.

## See Also

- [func previousLocation(in: SKNode) -> CGPoint](uitouch/previouslocation(in:)-ea29.md)
  Returns the previous location of the touch in the coordinate system of the given node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/location(in:)-44h4k)*