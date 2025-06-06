# Processing an Image Using Built-in Filters

**Framework**: Coreimage

Apply effects such as sepia tint, highlight strengthening, and scaling to images.

#### Overview

You can add effects to images by applying Core Image filters to [`CIImage`](ciimage.md) objects. Figure 1 shows three filters chained together to achieve a cumulative effect:

1. Apply the sepia filter to tint an image with a reddish-brown hue. 
2. Add the bloom filter to accentuate highlights. 
3. Use the Lanczos scale filter to scale an image down.

![Photo of a waterwheel filtered using sepia tone, bloom, and Lanczos scale filters](https://docs-assets.developer.apple.com/published/3ba6c93555/d7305d70-2fba-452b-a643-49041c714ee1.png)

##### 2948368

[`CIImage`](ciimage.md) processing occurs in a [`CIContext`](cicontext.md) object. Creating a [`CIContext`](cicontext.md) is expensive, so create one during your initial setup and reuse it throughout your app.

```swift
let context = CIContext()
```

##### 2948369

The next step is to load an image to process. This example loads an image from the project bundle.

```swift
let imageURL = URL(fileURLWithPath: "\(Bundle.main.bundlePath)/YourImageName.png")
let originalCIImage = CIImage(contentsOf: imageURL)!
self.imageView.image = UIImage(ciImage:originalCIImage)
```

The [`CIImage`](ciimage.md) object isn’t itself a displayable image, but rather image data. To display it, you must convert it to another type, such as [`UIImage`](https://developer.apple.com/documentation/uikit/uiimage).

##### 2951305

A [`CIFilter`](cifilter.md) represents a single operation or recipe for a particular effect. To process a [`CIImage`](ciimage.md) object, pass it through [`CIFilter`](cifilter.md) objects. You can subclass [`CIFilter`](cifilter.md) or draw from the existing library of built-in filters.

###### 2948365

Although you can chain filters without separating them into functions, the following example shows how to configure a single [`CIFilter`](cifilter.md), the [`sepiaTone()`](cifilter/3228402-sepiatone.md) filter.

```swift
func sepiaFilter(_ input: CIImage, intensity: Float) -> CIImage? {
    let sepiaFilter = CIFilter.sepiaTone()
    sepiaFilter.inputImage = input
    sepiaFilter.intensity = intensity
    return sepiaFilter.outputImage
}
```

To pass the image through the filter, call the sepia filter function.

```swift
let sepiaCIImage = sepiaFilter(originalCIImage, intensity:0.9)
```

You can check the intermediate result at any point in the filter chain by converting from [`CIImage`](ciimage.md) to a [`UIImage`](https://developer.apple.com/documentation/uikit/uiimage). You can then assign this [`UIImage`](https://developer.apple.com/documentation/uikit/uiimage) to a [`UIImageView`](https://developer.apple.com/documentation/uikit/uiimageview) for display.

```swift
self.imageView.image = UIImage(ciImage:sepiaCIImage!)
```

###### 2948366

The bloom filter accentuates the highlights of an image. You can apply it as part of a chain without factoring it into a separate function, but this example encapsulates its functionality into a function.

```swift
func bloomFilter(_ input:CIImage, intensity: Float, radius: Float) -> CIImage? {
    let bloomFilter = CIFilter.bloom()
    bloomFilter.inputImage = input
    bloomFilter.intensity = intensity
    bloomFilter.radius
    return bloomFilter.outputImage
}
```

Like the sepia filter, the intensity of the bloom filter’s effect ranges between 0 and 1, with 1 being the most intense effect. The bloom filter has an additional r`adius` parameter to determine how much the glowing regions expand. Experiment with a range to values to fine tune the effect, or assign the input parameter to a control like a [`UISlider`](https://developer.apple.com/documentation/uikit/uislider) to allow your users to tweak its values.

> **Note**: The [`gloom()`](cifilter/3228334-gloom.md) filter performs the opposite effect.

To display the output, convert the [`CIImage`](ciimage.md) to a [`UIImage`](https://developer.apple.com/documentation/uikit/uiimage).

```swift
let bloomCIImage = bloomFilter(sepiaCIImage, intensity:1, radius:10)
_imageView.image = UIImage(ciImage:bloomCIImage)
```

###### 2948367

Apply the [`lanczosScaleTransform()`](cifilter/3228344-lanczosscaletransform.md) to obtain a high-quality downsampling of the image, preserving the original image’s aspect ratio through the [`lanczosScaleTransform()`](cifilter/3228344-lanczosscaletransform.md) filter’s parameter `aspectRatio`. For built-in Core Image filters, calculate the aspect ratio as the image’s width over height, as in Listing 8.

```swift
CGFloat imageWidth = originalUIImage.size.width
CGFloat imageHeight = originalUIImage.size.height
let aspectRatio = Double(originalImage.size.width) / Double(originalImage.size.height)
let scaledCIImage = scaleFilter(bloomCIImage, aspectRatio:aspectRatio, scale:0.5)
```

Like other built-in filters, the [`lanczosScaleTransform()`](cifilter/3228344-lanczosscaletransform.md) filter also outputs its result as a [`CIImage`](ciimage.md).

```swift
func scaleFilter(_ input:CIImage, aspectRatio : Float, scale : Float) -> CIImage {
    let scaleFilter = CIFilter.lanczosScaleTransform()
    scaleFilter.inputImage = input
    scaleFilter.scale = scale
    scaleFilter.aspectRatio = aspectRatio
    return scaleFilter.outputImage!
}
```

> ❗ **Important**: To optimize computation, Core Image doesn’t actually render any intermediate [`CIImage`](ciimage.md) result until you force the [`CIImage`](ciimage.md) to display its content onscreen, as you might do using [`UIImageView`](https://developer.apple.com/documentation/uikit/uiimageview).

```swift
self.imageView.image = UIImage(ciImage:scaledCIImage)
```

> **Note**: Core Image optimizes filtering by reordering the three chained filters and concatenating them into a single image processing kernel, saving computation and rendering cycles.

In addition to trying out the built-in filters for a fixed effect, you can combine filters in certain [`Filter Recipes`](https://developer.apple.com/documentation/coreimage#2951339) to accomplish tasks such as [`Applying a Chroma Key Effect`](applying_a_chroma_key_effect.md), [`Selectively Focusing on an Image`](selectively_focusing_on_an_image.md), [`Customizing Image Transitions`](customizing_image_transitions.md), and [`Simulating Scratchy Analog Film`](simulating_scratchy_analog_film.md).

## See Also

- [class CIContext](cicontext.md)
  An evaluation context for rendering image processing results and performing image analysis.
- [class CIImage](ciimage.md)
  A representation of an image to be processed or produced by Core Image filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/processing_an_image_using_built-in_filters)*