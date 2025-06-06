# Selectively Focusing on an Image

**Framework**: Core Image

Focus on a part of an image by applying Gaussian blur and gradient masks.

#### Overview

You can selectively blur areas of an image using [`maskedVariableBlur()`](cifilter/3228355-maskedvariableblur.md) filter.

![Flowchart showing the combination of image and mask in focusing on the scoop in a photo of walnuts](https://docs-assets.developer.apple.com/published/59d757a3ea/d923e88a-f1ca-4327-b3a9-637db674e880.png)

You specify the region to blur by applying a mask image; the shape and values of the mask image determine the location and strength of the blurring. Creating this effect involves the following steps:

1. To focus on a strip across the image, create two linear gradients representing the portions of the image to blur.
2. To focus on a circular region in the image, create a radial gradient centered on the region to keep sharp.
3. Composite the gradients into a mask.
4. Apply Core Image’s [`maskedVariableBlur()`](cifilter/3228355-maskedvariableblur.md) filter to the original image, inputting the created mask.

##### 2953470

You can build your mask in any shape, but the general strategy remains the same: leave the mask transparent where you want the original image to stay sharp and focused. This section covers focusing on a horizontal strip. 

To build a mask that leaves out a stripe, create linear gradients from a single color, such as green or gray. Our goal is to build the mask shown in Figure 2.

![Linear gradient mask for blurring all regions of an image except a strip](https://docs-assets.developer.apple.com/published/ade94388d0/01f73fd4-6834-45fa-b243-810efd0dcf6e.png)

The linear gradients cause the blur to taper smoothly as it approaches the focused stripe of the image. The Core Image [`CIFilter`](cifilter.md) named [`linearGradient()`](cifilter/3228351-lineargradient.md) generates filters of the desired color. The linear gradient has four parameters:

Compute the start and stop points of the gradient as fractions of the image height, as obtained through [`extent`](ciimage/1437996-extent.md). For this particular mask and example image, focus on the area near the middle, in the second quarter of the image. Set the linear gradient’s `point0` and `point1` to reflect the region through which the gradient tapers.

```swift
let h = inputImage.extent.size.height
let topGradient = CIFilter.linearGradient()
topGradient.point0 = CGPoint(x:0, y:0.85 * h)
topGradient.color0 = CIColor.green
topGradient.point1 = CGPoint(x:0, y:0.6 * h)
topGradient.color1 = CIColor(red:0, green:1, blue:0, alpha:0)
```

The lower gradient should complement the upper gradient, so that their combined coverage delineates the entire area to blur. Express the starting `inputPoint0` y-value at `0.35` of the image height and taper to `0.6`, where the top gradient began. This leaves a gap in the combined mask through which the sharp image will show.

```swift
let bottomGradient = CIFilter.linearGradient()
bottomGradient.point0 = CGPoint(x:0, y:0.35 * h)
bottomGradient.color0 = CIColor.green
bottomGradient.point1 = CGPoint(x:0, y:0.6 * h)
bottomGradient.color1 = CIColor(red:0, green:1, blue:0, alpha:0)
```

##### 2953465

To create a mask that dilineates where and how strong a blur to apply, combine the two linear gradients.

![ Graphic depicting the additive compositing of two linear gradients to form a single mask](https://docs-assets.developer.apple.com/published/92e064239d/12bca933-f2e0-4826-97b3-12753b75587f.png)

Since the gradients themselves are [`CIFilter`](cifilter.md) objects, compositing them is as simple as concatenating their filter outputs to a compositing filter.  Use the built-in [`CIFilter`](cifilter.md) named [`additionCompositing()`](cifilter/3228264-additioncompositing.md) to composite two images additively.

```swift
let gradientMask = CIFilter.additionCompositing()
gradientMask.inputImage = topGradient.outputImage
gradientMask.backgroundImage = bottomGradient.outputImage
```

The resulting mask is now ready to be applied as part of the [`maskedVariableBlur()`](cifilter/3228355-maskedvariableblur.md) filter.

##### 2953467

In order to focus on a circular region of an image, you can create a Core Image [`radialGradient()`](cifilter/3228395-radialgradient.md) filter.

The filter takes four parameters:

1. Set the `center` to a [`CGPoint`](https://developer.apple.com/documentation/corefoundation/cgpoint) pointing to the center of the region you want to leave unblurred.
2. Set the `radius0` to a fraction of the image’s dimension, like `0.2*h` in this example. You can tweak this parameter to determine the size of the sharp region.
3. Set the `radius1` to a larger fraction of the image’s dimension, like `0.3*h` in this example. Tweaking this parameter changes the extent of the blur’s tapering effect; a larger value makes the blur more gradual, whereas a smaller value makes the image transition more abruptly from sharp (at `inputRadius0`) to blur (at `inputRadius1`).
4. As with the linear gradients, set `color0` to transparency, and `color1` to a solid opaque color, to indicate the blur’s gradation from nonexistent to full.

```swift
let h = inputImage.extent.size.height
let w = inputImage.extent.size.width
let radialMask = CIFilter.radialGradient()
radialMask.center = CGPoint(x:0.55 * w, y:0.6 * h)
radialMask.radius0 = Float(0.2 * h)
radialMask.radius1 = Float(0.3 * h)
radialMask.color0 = CIColor(red:0, green:1, blue:0, alpha:0)
radialMask.color1 = CIColor(red:0, green:1, blue:0, alpha:1)
```

This yields a circular mask to use with the [`maskedVariableBlur()`](cifilter/3228355-maskedvariableblur.md) filter. 

![Circular gradient mask for blurring out all pixels except those in a circular region](https://docs-assets.developer.apple.com/published/6450f86006/02e2331a-016c-4716-83fd-1a185b6bbf0c.png)

##### 2953468

The final step is applying your choice of mask with the input image. The [`maskedVariableBlur()`](cifilter/3228355-maskedvariableblur.md) built-in [`CIFilter`](cifilter.md) accomplishes this task with the following input parameters:

```swift
let maskedVariableBlur = CIFilter.maskedVariableBlur()
maskedVariableBlur.inputImage = inputImage
maskedVariableBlur.mask = radialMask.outputImage
maskedVariableBlur.radius = 10
let selectivelyFocusedCIImage = maskedVariableBlur.outputImage
```

The resulting image shows the original image with portions blurred out according to the mask applied. The linear gradient mask results in an output image focused on a strip, and the radial gradient mask results in an output image focused on a circular region.

![CIMaskedVariableBlur with a linear gradient mask applied to a photo of walnuts](https://docs-assets.developer.apple.com/published/2f30fb7085/e003b5d6-55df-40a7-be10-05e42717d02a.png)

![CIMaskedVariableBlur with a radial gradient mask applied to a photo of walnuts](https://docs-assets.developer.apple.com/published/1ea630def9/2d3f24d8-df1a-462a-8a04-ecbdbcde833f.png)

## See Also

- [Applying a Chroma Key Effect](applying_a_chroma_key_effect.md)
  Replace a color in one image with the background from another.
- [Customizing Image Transitions](customizing_image_transitions.md)
  Transition between images in creative ways using Core Image filters.
- [Simulating Scratchy Analog Film](simulating_scratchy_analog_film.md)
  Degrade the quality of an image to make it look like dated, analog film.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/selectively_focusing_on_an_image)*