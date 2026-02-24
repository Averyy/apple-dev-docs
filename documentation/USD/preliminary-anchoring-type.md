# preliminary:anchoring:type

**Framework**: USD

A option that specifies the type of anchor.

#### Overview

The [`Preliminary_AnchoringAPI`](preliminary-anchoringapi.md) specifies an anchor’s center as the prim’s origin, and the top of the anchor as its normal vector points. The runtime requires an asset to supply a value for this property.

##### Declaration

```other
uniform token preliminary:anchoring:type (
    allowedTokens = ["plane", "image", "face", "none"]
)
```

##### Anchor Types

- **`plane`**: Requests that the runtime center the prim on top of a surface.
- **`image`**: Requests that the runtime center the prim on top of an image.
- **`face`**: Requests that the runtime center the prim on a detected face.
- **`none`**: Requests that the runtime doesn’t anchor the prim. This option has the same effect as omitting the anchoring schema.

##### Anchor a Cube to a Real World Surface

By adding the anchoring schema and defining [`preliminary:anchoring:type`](preliminary-anchoring-type.md) of `plane`, the following cube instructs the runtime to place it on the first horizontal surface the runtime detects in an AR experience.

```swift
def Cube "PlaneAnchoredCube" (
    prepend apiSchemas = [ "Preliminary_AnchoringAPI" ]
)
{
    uniform token preliminary:anchoring:type = "plane"
    ...
}
```

## See Also

- [preliminary:planeAnchoring:alignment](preliminary-planeanchoring-alignment.md)
  An option that specifies the orientation of a plane.
- [preliminary:imageAnchoring:referenceImage](preliminary-imageanchoring-referenceimage.md)
  The characteristics of an image the runtime should scan for in order to attach a prim.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/preliminary-anchoring-type)*