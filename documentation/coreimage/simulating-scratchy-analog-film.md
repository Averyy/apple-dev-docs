# Simulating Scratchy Analog Film

**Framework**: Core Image

Degrade the quality of an image to make it look like dated, analog film.

#### Overview

The [`sepiaToneFilter`](cifilter-swift.class/sepiatonefilter.md) filter changes the tint of an image to a reddish-brownish hue resembling old analog photographs. You can enhance the effect by applying random specks and scratches.

![Compositing scratchy analog film by compositing results from CIFilter objects](https://docs-assets.developer.apple.com/published/dc7ad8bd835b76a7a4439a1d5f7f95dd/media-2959650%402x.png)

The following steps leverage built-in Core Image filters to tint and texture an image to look as if it were analog film:

1. Apply the [`sepiaToneFilter`](cifilter-swift.class/sepiatonefilter.md) filter.
2. Create randomly varying white specks to simulate grain.
3. Create randomly varying dark scratches to simulate scratchy film.
4. Composite the speckle image and scratches onto the sepia-toned image.

##### Apply the Sepia Tone Filter to the Original Image

Tint the original image by applying the [`sepiaToneFilter`](cifilter-swift.class/sepiatonefilter.md) filter.

```swift
CIFilter<CISepiaTone> *sepiaFilter = CIFilter.sepiaToneFilter;
sepiaFilter.inputImage = inputImage;
sepiaFilter.intensity = 1.0;
CIImage *sepiaCIImage = sepiaFilter.outputImage;
```

##### Simulate Grain By Creating Randomly Varying Specks

You can use the output of the [`randomGeneratorFilter`](cifilter-swift.class/randomgeneratorfilter.md) filter to generate images containing random noise. Even though the noise pattern isn’t customizable in size, you can extend and crop it to fit the image.

> **Note**:  The image output from [`randomGeneratorFilter`](cifilter-swift.class/randomgeneratorfilter.md) is always the same; even if you reseed your random number generator, the image output from this filter is always the same 512x512 pattern. However, it’s suitable for giving the appearance of randomness. For truly random noise generation, see [`GameplayKit`](https://developer.apple.com/documentation/GameplayKit).

The filter takes no inputs.

```swift
CIFilter<CIRandomGenerator> *colorNoise = CIFilter.randomGeneratorFilter;
CIImage* noiseImage = colorNoise.outputImage;
```

Next, apply a whitening effect by chaining the noise output to a [`colorMatrixFilter`](cifilter-swift.class/colormatrixfilter.md) filter. This built-in filter multiplies the noise color values individually and applies a bias to each component. For white grain, apply whitening to the y-component of RGB and no bias.

```swift
CIVector *whitenVector = [CIVector vectorWithX:0 Y:1 Z:0 W:0];
CIVector *fineGrain = [CIVector vectorWithX:0 Y:0.005 Z:0 W:0];
CIVector *zeroVector = [CIVector vectorWithX:0 Y:0 Z:0 W: 0];
CIFilter<CIColorMatrix> *whiteningFilter = CIFilter.colorMatrixFilter;
whiteningFilter.inputImage = noiseImage;
whiteningFilter.RVector = whitenVector;
whiteningFilter.RVector = whitenVector;
whiteningFilter.BVector = whitenVector;
whiteningFilter.AVector = fineGrain;
whiteningFilter.biasVector = zeroVector;
CIImage *whiteSpecks = whiteningFilter.outputImage;
```

The `whiteSpecks` resulting from this filter have the appearance of spotty grain when viewed as an image.

![Image of white dots on a transaprent background, used to simulate grain on an old photo](https://docs-assets.developer.apple.com/published/ff51df9843bef2a67a612e62a804220c/media-2960179%402x.png)

Create the grainy image by compositing the whitened noise as input over the sepia-toned source image using the [`sourceOverCompositingFilter`](cifilter-swift.class/sourceovercompositingfilter.md) filter.

```swift
CIFilter<CICompositeOperation> *speckCompositor = CIFilter.sourceOverCompositingFilter;
speckCompositor.inputImage = whiteSpecks;
speckCompositor.backgroundImage = sepiaCIImage;
CIImage *speckledImage = speckCompositor.outputImage;
```

##### Simulate Scratch By Scaling Randomly Varying Noise

The process for applying random-looking scratches is the same as the technique used in the white grain: color the output of the [`randomGeneratorFilter`](cifilter-swift.class/randomgeneratorfilter.md) filter.

To make the speckle resemble scratches, scale the random noise output vertically by applying a scaling [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform).

```swift
CGAffineTransform verticalScale = CGAffineTransformMakeScale(1.5, 25);
CIImage* transformedNoise = [noiseImage imageByApplyingTransform:verticalScale];
```

Previously, you whitened the speckle image by applying the `CIColorMatrix` filter evenly across all color components.  For the dark scratches, instead focus on only the red component, setting the other vector inputs to zero.  This time, instead of multiplying the green, blue, and alpha channels, add bias `(0, 1, 1, 1)`.

```swift
CIFilter<CIColorMatrix>* darkeningFilter = CIFilter.colorMatrixFilter;
CIVector* darkenVector = [CIVector vectorWithX:4 Y:0 Z:0 W:0];
CIVector* darkenBias = [CIVector vectorWithX:0 Y:1 Z:1 W:1];
darkeningFilter.inputImage = noiseImage;
darkeningFilter.RVector = darkenVector;
darkeningFilter.GVector = zeroVector;
darkeningFilter.BVector = zeroVector;
darkeningFilter.AVector = zeroVector;
darkeningFilter.biasVector = darkenBias;
CIImage* randomScratches = darkeningFilter.outputImage;
```

The resulting scratches are cyan, so grayscale them using the [`minimumComponentFilter`](cifilter-swift.class/minimumcomponentfilter.md) filter, which takes the minimum of the RGB values to produce a grayscale image.

```swift
CIFilter<CIMinimumComponent> *grayscaleFilter = CIFilter.minimumComponentFilter;
grayscaleFilter.inputImage = randomScratches;
CIImage *darkScratches = grayscaleFilter.outputImage;
```

The grayscale filter produces random lines that resemble dark scratches.

![Image of black lines on a white background, used to simulate scratches on an old photo](https://docs-assets.developer.apple.com/published/2871bb09f511273da58c7ccd382417c8/media-2960180%402x.png)

##### Composite the Specks and Scratches to the Sepia Image

Now that the components are set, you can add the scratches to the grainy sepia image produced earlier.  However, unlike the grainy texture, the scratches impact the image multiplicatively.  Instead of the [`sourceOverCompositingFilter`](cifilter-swift.class/sourceovercompositingfilter.md) filter, which composites source over background, use the [`multiplyCompositingFilter`](cifilter-swift.class/multiplycompositingfilter.md) filter to compose the scratches multiplicatively.  Set the scratched image as the filter’s input image, and tab the speckle-composited sepia image as the input background image.

```swift
CIFilter<CICompositeOperation> *oldFilmCompositor = CIFilter.multiplyCompositingFilter;
oldFilmCompositor.inputImage = darkScratches;
oldFilmCompositor.backgroundImage = speckledImage;
CIImage *oldFilmImage = oldFilmCompositor.outputImage;
```

Since the noise images had different dimensions than the source image, crop the composited result to the original image size to remove excess beyond the original extent.

```swift
CIImage* finalImage = [oldFilmImage imageByCroppingToRect:inputImage.extent];
```

The cropped image represents the final result: a sepia-toned image with simulated grain and scratches composited to give it an analog film appearance.

![Sepia-toned image of fruit augmented with speckle grain and dark scratches.](https://docs-assets.developer.apple.com/published/2870c1b20386d99816f59eae94ee9bfb/media-2959656%402x.png)

## See Also

- [Applying a Chroma Key Effect](applying-a-chroma-key-effect.md)
  Replace a color in one image with the background from another.
- [Selectively Focusing on an Image](selectively-focusing-on-an-image.md)
  Focus on a part of an image by applying Gaussian blur and gradient masks.
- [Customizing Image Transitions](customizing-image-transitions.md)
  Transition between images in creative ways using Core Image filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/simulating-scratchy-analog-film)*