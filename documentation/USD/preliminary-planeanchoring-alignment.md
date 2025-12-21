# preliminary:planeAnchoring:alignment

**Framework**: USD

An option that specifies the orientation of a plane.

#### Overview

This property is active only for the `preliminary:anchoring:type` value `plane`. The runtime recognizes real-word surfaces such as floors, tables, ceilings as horizontal planes. Vertical planes include walls, doors, and windows.

##### Declaration

```other
uniform token preliminary:planeAnchoring:alignment (
        allowedTokens = ["horizontal", "vertical", "any"]
)
```

##### Plane Anchor Types

##### Anchor a Prim to a Horizontal Plane

The following asset definition requests that the runtime anchor this prim to the first surface the runtime detects that occupies a horizontal orientation in relation to the camera.

```swift
def Cube "PlaneAnchoredCube" (
    prepend apiSchemas = [ "Preliminary_AnchoringAPI" ]
)
{
    uniform token preliminary:anchoring:type = "plane"
    uniform token preliminary:planeAnchoring:alignment = "horizontal"
    ...
}
```

## See Also

- [preliminary:anchoring:type](preliminary-anchoring-type.md)
  A option that specifies the type of anchor.
- [preliminary:imageAnchoring:referenceImage](preliminary-imageanchoring-referenceimage.md)
  The characteristics of an image the runtime should scan for in order to attach a prim.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/preliminary-planeanchoring-alignment)*