# createImageData

**Framework**: Webkitjs  
**Kind**: instm

Creates an opaque object whose `data` property contains a one-dimensional array of pixel values, initialized to transparent black.

**Availability**:
- Safari Desktop 4.0+
- Safari Mobile 3.0+

## Declaration

```swift
ImageData createImageData(
    ImageData? imagedata
);
```

#### Return_value

An `imageData` object.

#### Discussion

This method is typically used to create additional pixel arrays that can be blitted to the canvas in a single operation. You can optionally pass in another `imageData` object as a parameter, instead of a width and height, to create a new `imageData` object with the same pixel dimensions as the specified object.

## Parameters

- `sw`: The width of the pixel array.
- `sh`: The height of the pixel array.

## See Also

- [getImageData](canvasrenderingcontext2d/1632656-getimagedata.md)
  Gets an `imageData` object containing an RGBa pixel array corresponding to a rectangular area of the canvas.
- [putImageData](canvasrenderingcontext2d/1633082-putimagedata.md)
  Blits the contents of an `imageData` object to the canvas. Alternatively, blits a specified region of the `imageData` object to the canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1632980-createimagedata)*