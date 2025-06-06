# texture(from:)

**Framework**: Watchkit  
**Kind**: method

Renders the contents of a node tree and returns the rendered image as a SpriteKit texture.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func texture(from node: SKNode) -> SKTexture?
```

#### Return Value

A SpriteKit texture that holds the rendered image.

#### Discussion

The `node` being rendered does not need to appear in the interface’s presented scene. The new texture is created with a size equal to the rectangle returned by the `node`’s [`calculateAccumulatedFrame()`](https://developer.apple.com/documentation/SpriteKit/SKNode/calculateAccumulatedFrame()) method. If the `node` is not a scene node, it is rendered with a clear background color (`[SKColor clearColor]`).

## Parameters

- `node`: A node object representing the root node of the tree to be render to the texture.

## See Also

- [func texture(from: SKNode, crop: CGRect) -> SKTexture?](wkinterfaceskscene/texture(from:crop:).md)
  Renders a portion of a node’s contents and returns the rendered image as a SpriteKit texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/texture(from:))*