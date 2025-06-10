# Selectively Focusing on an Image

**Framework**: Core Image

Focus on a part of an image by applying Gaussian blur and gradient masks.

#### Overview

You can selectively blur areas of an image using [`maskedVariableBlurFilter`](cifilter-swift.class/maskedvariableblurfilter.md) filter.

![Flowchart showing the combination of image and mask in focusing on the scoop in a photo of walnuts](https://docs-assets.developer.apple.com/published/f5b5d0be1052e72273f79f4ff27f3f94/media-2960174%402x.png)

You specify the region to blur by applying a mask image; the shape and values of the mask image determine the location and strength of the blurring. Creating this effect involves the following steps:

1. To focus on a strip across the image, create two linear gradients representing the portions of the image to blur.
2. To focus on a circular region in the image, create a radial gradient centered on the region to keep sharp.
3. Composite the gradients into a mask.
4. Apply Core Image’s [`maskedVariableBlurFilter`](cifilter-swift.class/maskedvariableblurfilter.md) filter to the original image, inputting the created mask.

##### Focusing on a Strip of the Image

You can build your mask in any shape, but the general strategy remains the same: leave the mask transparent where you want the original image to stay sharp and focused. This section covers focusing on a horizontal strip.

To build a mask that leaves out a stripe, create linear gradients from a single color, such as green or gray. Our goal is to build the mask shown in Figure 2.

![Linear gradient mask for blurring all regions of an image except a strip](https://docs-assets.developer.apple.com/published/2b1a1d757f70ba247c869887fd250383/media-2959648%402x.png)

The linear gradients cause the blur to taper smoothly as it approaches the focused stripe of the image. The Core Image [`CIFilter`](cifilter-swift.class.md) named [`linearGradientFilter`](cifilter-swift.class/lineargradientfilter.md) generates filters of the desired color. The linear gradient has four parameters:

Compute the start and stop points of the gradient as fractions of the image height, as obtained through [`extent`](ciimage/extent.md). For this particular mask and example image, focus on the area near the middle, in the second quarter of the image. Set the linear gradient’s `point0` and `point1` to reflect the region through which the gradient tapers.

```swift
const CGFloat h = inputImage.extent.size.height;
CIFilter<CILinearGradient>* topGradient = CIFilter.linearGradientFilter;
topGradient.point0 = CGPointMake(0, 0.85 * h);
topGradient.color0 = CIColor.greenColor;
topGradient.point1 = CGPointMake(0, 0.6 * h);
topGradient.color1 = [CIColor colorWithRed:0 green:1 blue:0];
```

The lower gradient should complement the upper gradient, so that their combined coverage delineates the entire area to blur. Express the starting `inputPoint0` y-value at `0.35` of the image height and taper to `0.6`, where the top gradient began. This leaves a gap in the combined mask through which the sharp image will show.

```swift
CIFilter<CILinearGradient>* bottomGradient = CIFilter.linearGradientFilter;
bottomGradient.point0 = CGPointMake(0, 0.35 * h);
bottomGradient.color0 = CIColor.greenColor;
bottomGradient.point1 = CGPointMake(0, 0.6 * h);
bottomGradient.color1 = [CIColor colorWithRed:0 green:1 blue:0 alpha:0];
```

##### Creating a Mask By Compositing Linear Gradients

To create a mask that dilineates where and how strong a blur to apply, combine the two linear gradients.

![ Graphic depicting the additive compositing of two linear gradients to form a single mask](https://docs-assets.developer.apple.com/published/fb88c718a62cfd09d342d7700fe6bc9a/media-2959647%402x.png)

Since the gradients themselves are [`CIFilter`](cifilter-swift.class.md) objects, compositing them is as simple as concatenating their filter outputs to a compositing filter.  Use the built-in [`CIFilter`](cifilter-swift.class.md) named [`additionCompositingFilter`](cifilter-swift.class/additioncompositingfilter.md) to composite two images additively.

```swift
CIFilter<CICompositeOperation> *gradientMask = CIFilter.additionCompositingFilter
gradientMask.inputImage = topGradient.outputImage;
gradientMask.backgroundImage = bottomGradient.outputImage;
```

The resulting mask is now ready to be applied as part of the [`maskedVariableBlurFilter`](cifilter-swift.class/maskedvariableblurfilter.md) filter.

##### Focusing on a Circular Region

In order to focus on a circular region of an image, you can create a Core Image [`radialGradientFilter`](cifilter-swift.class/radialgradientfilter.md) filter.

The filter takes four parameters:

1. Set the `center` to a [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint) pointing to the center of the region you want to leave unblurred.
2. Set the `radius0` to a fraction of the image’s dimension, like `0.2*h` in this example. You can tweak this parameter to determine the size of the sharp region.
3. Set the `radius1` to a larger fraction of the image’s dimension, like `0.3*h` in this example. Tweaking this parameter changes the extent of the blur’s tapering effect; a larger value makes the blur more gradual, whereas a smaller value makes the image transition more abruptly from sharp (at `inputRadius0`) to blur (at `inputRadius1`).
4. As with the linear gradients, set `color0` to transparency, and `color1` to a solid opaque color, to indicate the blur’s gradation from nonexistent to full.

```swift
CIFilter<CIRadialGradient> *radialMask = CIFilter.radialGradientFilter;
radialMask.center = CGPointMake(0.55 * w, 0.6 * h);
radialMask.radius0 = 0.2 * h;
radialMask.radius1 = 0.3 * h;
radialMask.color0 = [CIColor colorWithRed:0 green:1 blue:0 alpha:0];
radialMask.color1 = [CIColor colorWithRed:0 green:1 blue:0 alpha:1];
```

This yields a circular mask to use with the [`maskedVariableBlurFilter`](cifilter-swift.class/maskedvariableblurfilter.md) filter.

![Circular gradient mask for blurring out all pixels except those in a circular region](https://docs-assets.developer.apple.com/published/15b8844dd3a9307563c3e4ccb5c2e3fe/media-2959646%402x.png)

##### Masking the Blurred Image to Apply Selective Focus

The final step is applying your choice of mask with the input image. The [`maskedVariableBlurFilter`](cifilter-swift.class/maskedvariableblurfilter.md) built-in [`CIFilter`](cifilter-swift.class.md) accomplishes this task with the following input parameters:

```swift
CIFilter<CIMaskedVariableBlur> *maskedVariableBlur = CIFilter.maskedVariableBlurFilter;
maskedVariableBlur.inputImage = inputImage;
maskedVariableBlur.mask = radialMask.outputImage;
maskedVariableBlur.radius = 10;
CIImage *selectivelyFocusedCIImage = maskedVariableBlur.outputImage;
```

The resulting image shows the original image with portions blurred out according to the mask applied. The linear gradient mask results in an output image focused on a strip, and the radial gradient mask results in an output image focused on a circular region.

![CIMaskedVariableBlur with a linear gradient mask applied to a photo of walnuts](https://docs-assets.developer.apple.com/published/c8129c1198c636bd772217d201c8f181/media-2960173%402x.png)

![CIMaskedVariableBlur with a radial gradient mask applied to a photo of walnuts](https://docs-assets.developer.apple.com/published/11ca5e16d687bf1f93ab8322c5a58ede/media-2959645%402x.png)

## See Also

- [Applying a Chroma Key Effect](applying-a-chroma-key-effect.md)
  Replace a color in one image with the background from another.
- [Customizing Image Transitions](customizing-image-transitions.md)
  Transition between images in creative ways using Core Image filters.
- [Simulating Scratchy Analog Film](simulating-scratchy-analog-film.md)
  Degrade the quality of an image to make it look like dated, analog film.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/selectively-focusing-on-an-image)*