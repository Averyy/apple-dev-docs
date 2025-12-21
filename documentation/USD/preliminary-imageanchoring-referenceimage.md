# preliminary:imageAnchoring:referenceImage

**Framework**: USD

The characteristics of an image the runtime should scan for in order to attach a prim.

#### Overview

An asset assigns this property a prim with type `Preliminary_ReferenceImage`.

The runtime searches for an image described by this property in the physical environment. If the runtime finds a match, it places a prim at the image’s real-world location. When a runtime places a prim in the physical environment, the prim’s children also attach to that location.

The runtime employs the information contained in this property only when [`preliminary:anchoring:type`](preliminary-anchoring-type.md) is `image`.

##### Declaration

```other
rel preliminary:imageAnchoring:referenceImage
```

##### Anchor a Cube to an Image

The following example demonstrates how an asset defines a reference image (`ImageReference`) that the runtime should look for in the physical environment. The asset includes a cube that assigns an [`Preliminary_ReferenceImage`](preliminary-referenceimage.md) to its [`preliminary:imageAnchoring:referenceImage`](preliminary-imageanchoring-referenceimage.md) property, instructing the runtime to anchor it to a real-world object that matches the image criteria.

```other
def Cube "ImageAnchoredCube" (
    prepend apiSchemas = [ "Preliminary_AnchoringAPI" ]
)
{
    uniform token preliminary:anchoring:type = "image"
    rel preliminary:imageAnchoring:referenceImage = <ImageReference>
    ...

    def Preliminary_ReferenceImage "ImageReference"
    {
      uniform asset image = @image.png@
      uniform double physicalWidth = 0.12
    }
}
```

## See Also

- [preliminary:anchoring:type](preliminary-anchoring-type.md)
  A option that specifies the type of anchor.
- [preliminary:planeAnchoring:alignment](preliminary-planeanchoring-alignment.md)
  An option that specifies the orientation of a plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/preliminary-imageanchoring-referenceimage)*