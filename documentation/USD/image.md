# image

**Framework**: USD  
**Role**: Article

An image file for which the runtime should search.

#### Overview

Assign this property a path to a PNG or JPEG file.

##### Declaration

```other
uniform asset image
```

##### Define a reference image

The following [Preliminary_ReferenceImage](./preliminary-referenceimage.md) assigns this property a file named `image.png`.

```other
def Preliminary_ReferenceImage "ImageReference"
{
    uniform asset image = @image.png@
    ...
}
```

## See Also

### Properties
- [physicalWidth](./physicalwidth.md)
  An image’s width in centimeters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/image)*