# Applying a Chroma Key Effect

**Framework**: Coreimage

Replace a color in one image with the background from another.

#### Overview

Use the chroma key effect, also known as bluescreening or greenscreening, to replace the background of an image by setting a color or range of colors to transparent.

![The chroma key effect replaces the greenscreen background behind a paper airplane foreground with the image of a beach landscape to show paper airplane flying on a beach.](https://docs-assets.developer.apple.com/published/cd3b98a234/d799ef80-cf8e-4db2-aec8-7f398dbc4a2b.png)

You apply this technique in three steps:

1. Create a cube map for the [`colorCube()`](cifilter/3228287-colorcube.md) filter to determine which colors to set transparent.
2. Apply the [`colorCube()`](cifilter/3228287-colorcube.md) filter to the image to make pixels transparent.
3. Use the [`sourceOverCompositing()`](cifilter/3228412-sourceovercompositing.md) filter to place the image over the background image.

##### 2951341

A color cube is a 3D color-lookup table that uses the R, G, and B values from the image to lookup a color. To filter out green from the image, create a color map with the green portion set to transparent pixels.

A simple way to construct a color map with these characteristics is to model colors using an HSV (hue-saturation-value) representation. HSV represents hue as an angle around the central axis, as in a color wheel. In order to make a chroma key color from the source image transparent, set its lookup table value to `0` when its hue is in the correct color range.

![A hue color wheel highlighting hues between 108° and 144° to show the slice of green to filter out of the source image](https://docs-assets.developer.apple.com/published/cf1c45c984/6aac5329-8f16-46a7-ae6a-135098ed1f4a.png)

The value for green in the source image falls within the slice beginning at 108° (`108/360` = `0.3`) and ending at 144° (`144/360` = `0.4`). You’ll set transparency to `0` for this range in the color cube.

To create the color cube, iterate across all values of red, green, and blue, entering a value of 0 for combinations that the filter wiill set to transparent. Refer to the numbered list for details on each step to the routine.

```swift
func chromaKeyFilter(fromHue: CGFloat, toHue: CGFloat) -> CIColorCube {
    // 1
    let size = 64
    var cubeRGB = [Float]()
        
    // 2
    for z in 0 ..< size {
        let blue = CGFloat(z) / CGFloat(size-1)
        for y in 0 ..< size {
            let green = CGFloat(y) / CGFloat(size-1)
            for x in 0 ..< size {
                let red = CGFloat(x) / CGFloat(size-1)
                    
                // 3
                let hue = getHue(red: red, green: green, blue: blue)
                let alpha: CGFloat = (hue >= fromHue && hue <= toHue) ? 0: 1
                    
                // 4
                cubeRGB.append(Float(red * alpha))
                cubeRGB.append(Float(green * alpha))
                cubeRGB.append(Float(blue * alpha))
                cubeRGB.append(Float(alpha))
            }
        }
    }

    // 5
    let colorCubeFilter = CIFilter.colorCube()
    colorCubeFilter.cubeDimension = Float(size)
    colorCubeFilter.cubeData = Data(bytes: cubeRGB, count: cubeRGB.count * 4)
    return colorCubeFilter
}
```

1. Allocate memory. The color cube has three dimensions, each with four elements of data (RGBA). 
2. Use a for-loop to iterate through each color combination of red, green, and blue, simulating a color gradient.
3. Convert RGB to HSV, as in [`Listing 2`](applying_a_chroma_key_effect#2951414.md). Even though the color cube exists in RGB color space, it’s easier to isolate and remove color based on hue. Input `0` for green hues to indicate complete removal; use `1` for other hues to leave those colors intact. To specify green as a hue value, convert its angle in the hue pie chart to a range of `0` to `1`. The green in the sample image has hue between `0.3` (`108` out of `360` degrees`)` and `0.4` (`144` out of `360` degrees). Your shade of green may differ, so adjust the range accordingly.
4. The [`colorCube()`](cifilter/3228287-colorcube.md) filter requires premultiplied alpha values, meaning that the values in the lookup table have their transparency baked into their stored entries rather than applied when accessed.
5. Create a [`colorCube()`](cifilter/3228287-colorcube.md) filter with the cube data.

> **Note**: The framework doesn’t have built-in direct conversion between color spaces, but you can access the hue of a [`UIColor`](https://developer.apple.com/documentation/uikit/uicolor) created with RGB values. Create a [`UIColor`](https://developer.apple.com/documentation/uikit/uicolor) from the raw RGB values and then read the hue from it.

```swift
func getHue(red: CGFloat, green: CGFloat, blue: CGFloat) -> CGFloat {
    let color = UIColor(red: red, green: green, blue: blue, alpha: 1)
    var hue: CGFloat = 0
    color.getHue(&hue, saturation: nil, brightness: nil, alpha: nil)
    return hue
}
```

##### 2951338

Apply the color cube filter to a foreground image by setting its `inputImage` parameter and then accessing the `outputImage`.

```swift
let chromaCIFilter = chromaKeyFilter(fromHue: 0.3, toHue: 0.4)
chromaCIFilter.inputImage = foregroundCIImage
let sourceCIImageWithoutBackground = chromaCIFilter.outputImage
```

The output image contains the foreground with all green pixels made transparent.

The filter passes through each pixel in the input image, looks up its color in the color cube, and replaces the source color with the color in the color cube at the nearest position.

##### 2951340

Chain a [`sourceOverCompositing()`](cifilter/3228412-sourceovercompositing.md) filter to the color cube filter to composite a background image to the greenscreened output. The transparency in the colorcube-filtered image allows the composited background image to show through.

```swift
let compositor = CIFilter.sourceOverCompositing()
compositor.inputImage = sourceCIImageWithoutBackground
compositor.backgroundImage = backgroundCIImage
let compositedCIImage = compositor.outputImage
```

The foreground of the source image now appears in front of the background landscape without any trace of the green screen.

## See Also

- [Selectively Focusing on an Image](selectively_focusing_on_an_image.md)
  Focus on a part of an image by applying Gaussian blur and gradient masks.
- [Customizing Image Transitions](customizing_image_transitions.md)
  Transition between images in creative ways using Core Image filters.
- [Simulating Scratchy Analog Film](simulating_scratchy_analog_film.md)
  Degrade the quality of an image to make it look like dated, analog film.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/applying_a_chroma_key_effect)*