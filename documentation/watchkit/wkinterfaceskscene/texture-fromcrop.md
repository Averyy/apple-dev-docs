# texture(from:crop:)

**Framework**: Watchkit  
**Kind**: method

Renders a portion of a node’s contents and returns the rendered image as a SpriteKit texture.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func texture(from node: SKNode, crop: CGRect) -> SKTexture?
```

## Overview

A SpriteKit texture that holds the rendered image.

## Parameters

- `node`: A node object representing the root node of the tree to be render to the texture.
- `crop`: A rectangle in the  ’s coordinate system that describes the area to be rendered.

## Discussion

The `node` being rendered does not need to appear in the interface’s presented scene. The new texture is created with a size equal to the size of the `crop` rectangle. If the `node` is not a scene node, it is rendered with a clear background color (`[SKColor clearColor]`).

## See Also

- [func texture(from: SKNode) -> SKTexture?](texture(from:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/texture(from:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/texture(from:crop:))*