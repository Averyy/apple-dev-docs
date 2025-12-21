# physicalWidth

**Framework**: USD

An image’s width in centimeters.

#### Overview

This property informs the runtime how wide the image is in the physical environment. The runtime calculates the height based on the image’s aspect ratio.

Because this property describes a real-world width, the prim’s transform hierarchy doesn’t modify this property’s value.

##### Declaration

```other
uniform double physicalWidth
```

##### Define a Reference Images Width

To recognize an image in the real world, the runtime requires a prim to specify how wide the image is in the physical environment.

```other
def Preliminary_ReferenceImage "ImageReference"
{
    uniform double physicalWidth = 12
    ...
}
```

## See Also

- [image](image.md)
  An image file for which the runtime should search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/physicalwidth)*