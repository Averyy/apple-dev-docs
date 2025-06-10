# CanvasRenderingContext2D

**Framework**: WebKit JS  
**Kind**: cl

The `CanvasRenderingContext2D` class provides a 2D drawing context for a canvas element. Use the methods of this class to draw on the canvas. To obtain an instance of the `CanvasRenderingContext2D`, call the `getContext('2d')` method on a canvas object. See [`Safari HTML5 Canvas Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/HTML-canvas-guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010542) for usage examples.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 1.0+

## Declaration

```swift
interface CanvasRenderingContext2D
```

## Topics

### Drawing Rectangles
- [clearRect](canvasrenderingcontext2d/1632646-clearrect.md)
  Clears the specified rectangle to transparent black—RGBa(0,0,0,0).
- [fillRect](canvasrenderingcontext2d/1633676-fillrect.md)
  Fills a specified rectangle in the current fill color, gradient, or pattern.
- [strokeRect](canvasrenderingcontext2d/1632379-strokerect.md)
  Draws a rectangle using the current stroke color, pattern, or gradient.
### Creating Paths (Lines, Curves, Arcs, and Shapes)
- [beginPath](canvasrenderingcontext2d/1632556-beginpath.md)
  Denotes the beginning of new path.
- [clip](canvasrenderingcontext2d/1631003-clip.md)
  Constrains the clipping region of the canvas to the current path.
- [isPointInPath](canvasrenderingcontext2d/1631233-ispointinpath.md)
  Determines whether a specified point is within the area defined by the current path.
### Filling and Stroking Lines and Paths
- [fill](canvasrenderingcontext2d/1631011-fill.md)
  Fills the current path using the current fill color, gradient, or pattern.
- [fillStyle](canvasrenderingcontext2d/1633959-fillstyle.md)
  A CSS color, a gradient, or a pattern used to fill shapes and text.
- [lineCap](canvasrenderingcontext2d/1629505-linecap.md)
  A string specifying the type of end cap to put on lines to be drawn using `lineTo()`.
- [lineJoin](canvasrenderingcontext2d/1629229-linejoin.md)
  A string specifying the manner in which line joins are drawn.
- [lineWidth](canvasrenderingcontext2d/1630379-linewidth.md)
  A floating-point number that controls the width of lines and strokes, in pixels.
- [miterLimit](canvasrenderingcontext2d/1631529-miterlimit.md)
  A floating-point number that controls the miter limit ratio for mitered line joins.
- [stroke](canvasrenderingcontext2d/1634233-stroke.md)
  Draws the outline of the current path using the current stroke style and line width.
- [strokeStyle](canvasrenderingcontext2d/1634470-strokestyle.md)
  A CSS color, a gradient, or a pattern used to stroke lines and shapes.
### Drawing Images
- [drawImage](canvasrenderingcontext2d/1630282-drawimage.md)
  Draws the specified image with its upper-left corner at the specified point on the canvas, optionally scaling the image to a specified width and height. Alternatively, draws a specified region of the image, mapped to a specified region of the canvas.
### Drawing Text
- [fillText](canvasrenderingcontext2d/1634243-filltext.md)
  Draws a line of text at the specified x,y coordinates, optionally scaled to a specified maximum width.
- [font](canvasrenderingcontext2d/1632249-font.md)
  A string containing font settings, such as the font family, size, and weight.
- [measureText](canvasrenderingcontext2d/1631690-measuretext.md)
  Determines the width of the bounding box required to render the specified text with the current font settings.
- [strokeText](canvasrenderingcontext2d/1630188-stroketext.md)
  Draws a line of text in outline at the specified x,y coordinates, optionally limited to a specified maximum width.
- [textAlign](canvasrenderingcontext2d/1631811-textalign.md)
  A string that specifies whether text is left-justified, right-justified, or centered.
- [textBaseline](canvasrenderingcontext2d/1629692-textbaseline.md)
  A string that specifies how the bounding box aligns vertically relative to the y-coordinate.
### Changing the Coordinate System
- [rotate](canvasrenderingcontext2d/1630553-rotate.md)
  Rotates the canvas coordinate system.
- [scale](canvasrenderingcontext2d/1631799-scale.md)
  Scales the canvas coordinate system horizontally and vertically.
- [setTransform](canvasrenderingcontext2d/1630015-settransform.md)
  Sets the transformation matrix.
- [transform](canvasrenderingcontext2d/1629911-transform.md)
  Transforms the current transformation matrix using another matrix.
- [translate](canvasrenderingcontext2d/1629441-translate.md)
  Moves the origin of the canvas coordinate system.
### Saving and Restoring Settings
- [save](canvasrenderingcontext2d/1634183-save.md)
  Saves the current context settings on the stack.
- [restore](canvasrenderingcontext2d/1628925-restore.md)
  Restores the last saved set of context settings.
### Compositing
- [globalAlpha](canvasrenderingcontext2d/1631404-globalalpha.md)
  A floating-point number controlling the degree of opacity for all drawing operations.
- [globalCompositeOperation](canvasrenderingcontext2d/1632770-globalcompositeoperation.md)
  A string representing the compositing method for drawing operations.
### Creating Gradients and Patterns
- [createLinearGradient](canvasrenderingcontext2d/1630205-createlineargradient.md)
  Creates a linear gradient object with a specified start point and a specified end point.
- [createPattern](canvasrenderingcontext2d/1628866-createpattern.md)
  Creates a pattern object using the specified image as a template. The pattern can be specified as repeating horizontally, vertically, both horizontally and vertically (the default), or not at all.
- [createRadialGradient](canvasrenderingcontext2d/1631480-createradialgradient.md)
  Creates a radial gradient object using the cone defined by the specified starting and ending circles.
### Manipulating Pixels
- [createImageData](canvasrenderingcontext2d/1632980-createimagedata.md)
  Creates an opaque object whose `data` property contains a one-dimensional array of pixel values, initialized to transparent black.
- [getImageData](canvasrenderingcontext2d/1632656-getimagedata.md)
  Gets an `imageData` object containing an RGBa pixel array corresponding to a rectangular area of the canvas.
- [putImageData](canvasrenderingcontext2d/1633082-putimagedata.md)
  Blits the contents of an `imageData` object to the canvas. Alternatively, blits a specified region of the `imageData` object to the canvas.
### Working with Shadows
- [clearShadow](canvasrenderingcontext2d/1634057-clearshadow.md)
  Turns shadows off.
- [shadowBlur](canvasrenderingcontext2d/1632236-shadowblur.md)
  A floating-point number that controls the degree of Gaussian blur applied to shadows.
- [shadowColor](canvasrenderingcontext2d/1629275-shadowcolor.md)
  A string that contains the RGBa color value of shadows. 
- [shadowOffsetX](canvasrenderingcontext2d/1632399-shadowoffsetx.md)
  A floating-point number that controls the horizontal offset of shadows from the elements casting the shadows.
- [shadowOffsetY](canvasrenderingcontext2d/1633455-shadowoffsety.md)
  A floating-point number that controls the vertical offset of shadows from the elements casting the shadows.
### Constants
- [Global Compositing Operation Constants](canvasrenderingcontext2d/global_compositing_operation_constants.md)
  Constants used to set the `globalCompositeOperation` property.
- [textBaseline Constants](canvasrenderingcontext2d/textbaseline_constants.md)
  Constants used to set the `textBaseline` property that specify the vertical alignment of the bounding box relative to its y-coordinate. 
- [textAlign Constants](canvasrenderingcontext2d/textalign_constants.md)
  Constants used with the `textAlign` property that specify the horizontal alignment of the bounding box relative to its x-coordinate. 
### Instance Properties
- [canvas](canvasrenderingcontext2d/2871229-canvas.md)
- [direction](canvasrenderingcontext2d/1629301-direction.md)
- [imageSmoothingEnabled](canvasrenderingcontext2d/1777972-imagesmoothingenabled.md)
- [imageSmoothingQuality](canvasrenderingcontext2d/1777969-imagesmoothingquality.md)
- [lineDashOffset](canvasrenderingcontext2d/1631841-linedashoffset.md)
- [webkitBackingStorePixelRatio](canvasrenderingcontext2d/1629484-webkitbackingstorepixelratio.md)
- [webkitImageSmoothingEnabled](canvasrenderingcontext2d/1628979-webkitimagesmoothingenabled.md)
- [webkitLineDash](canvasrenderingcontext2d/1630482-webkitlinedash.md)
- [webkitLineDashOffset](canvasrenderingcontext2d/1630763-webkitlinedashoffset.md)
### Instance Methods
- [commit](canvasrenderingcontext2d/1777821-commit.md)
- [drawFocusIfNeeded](canvasrenderingcontext2d/1631353-drawfocusifneeded.md)
- [drawImageFromRect](canvasrenderingcontext2d/1633575-drawimagefromrect.md)
- [getLineDash](canvasrenderingcontext2d/1630019-getlinedash.md)
- [isPointInStroke](canvasrenderingcontext2d/1629025-ispointinstroke.md)
- [resetTransform](canvasrenderingcontext2d/2871273-resettransform.md)
- [setAlpha](canvasrenderingcontext2d/1631574-setalpha.md)
- [setCompositeOperation](canvasrenderingcontext2d/1631622-setcompositeoperation.md)
- [setFillColor](canvasrenderingcontext2d/1633538-setfillcolor.md)
- [setLineCap](canvasrenderingcontext2d/1632206-setlinecap.md)
- [setLineDash](canvasrenderingcontext2d/1632699-setlinedash.md)
- [setLineJoin](canvasrenderingcontext2d/1630234-setlinejoin.md)
- [setLineWidth](canvasrenderingcontext2d/1633380-setlinewidth.md)
- [setMiterLimit](canvasrenderingcontext2d/1633659-setmiterlimit.md)
- [setShadow](canvasrenderingcontext2d/1630005-setshadow.md)
- [setStrokeColor](canvasrenderingcontext2d/1629320-setstrokecolor.md)
- [webkitGetImageDataHD](canvasrenderingcontext2d/1633452-webkitgetimagedatahd.md)
- [webkitPutImageDataHD](canvasrenderingcontext2d/1631552-webkitputimagedatahd.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/canvasrenderingcontext2d)*