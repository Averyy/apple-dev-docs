# putImageData

**Framework**: Webkitjs  
**Kind**: instm

Blits the contents of an `imageData` object to the canvas. Alternatively, blits a specified region of the `imageData` object to the canvas.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
void putImageData(
    ImageData imagedata, 
    float dx, 
    float dy
);
```

#### Discussion

This method blits either an `imageData` pixel array, or a region of the pixel array, to the canvas, at the specified x,y coordinates. 

If only the `imageData` object and an x,y coordinate pair are passed in, the entire `imageData` object is rendered immediately to the screen. 

If additional x, y, width, and height parameters are passed in, only the specified region of the `imageData` pixel array is rendered to the screen. The region of the `imageData` pixel array is rendered on the canvas in the same relative position on the canvas as it would be if the whole pixel array had been rendered.

No parameters are individually optional—either just three or all seven parameters must be passed in.

All x and y parameter values are in CSS pixels—they are unaffected by scaling, rotation, or other transformations to the canvas coordinate system.

## Parameters

- `imageData`: An   object, containing a pixel array.
- `x`: The x-coordinate of the section of the canvas on which to render the image data.
- `y`: The x-coordinate of the section of the canvas on which to render the image data.
- `dx`: The x-coordinate of the left edge of the region of the   pixel array to render.
- `dy`: The y-coordinate of the top of the region of the   pixel array to render.
- `dw`: The width of the region of the   pixel array to render.
- `dh`: The height of the region of the   pixel array to render.

## See Also

- [createImageData](canvasrenderingcontext2d/1632980-createimagedata.md)
  Creates an opaque object whose `data` property contains a one-dimensional array of pixel values, initialized to transparent black.
- [getImageData](canvasrenderingcontext2d/1632656-getimagedata.md)
  Gets an `imageData` object containing an RGBa pixel array corresponding to a rectangular area of the canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d/1633082-putimagedata)*