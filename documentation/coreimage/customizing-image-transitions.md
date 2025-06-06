# Customizing Image Transitions

**Framework**: Coreimage

Transition between images in creative ways using Core Image filters.

#### Overview

You can add visual effects to an image transition by chaining together Core Image [`CIFilter`](cifilter.md) objects in the category [`CICategoryTransition`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP30000136-SW239). Each filter from this category represents a single transition effect.

For example, you can combine an effect that dissolves an image and one that pixelates it as a transition to a second image. This particular transition chain comprises three steps:

1. Create a [`dissolveTransition()`](cifilter/3228314-dissolvetransition.md) transition filter with time as an input parameter.
2. Create a [`pixellate()`](cifilter/3228393-pixellate.md) transition filter with time as an input parameter.
3. Initiate the transition by adding a time step to your run loop.

![Pixelated transition from a beach at daytime with rainbow in the sky to a beach at sunset](https://docs-assets.developer.apple.com/published/78a5ca63c0/171233e0-66d7-46fc-ad90-a14e683396e3.png)

##### 2953418

Filters in the transition category require your program to load both source and target images in order to transform the source into the destination.

```swift
let sourceURL = URL(fileURLWithPath: "\(Bundle.main.bundlePath)/YourSourceImage.JPG")
let sourceCIImage = CIImage(contentsOf: sourceURL)
        
let destinationURL = URL(fileURLWithPath: "\(Bundle.main.bundlePath)/YourTargetImage.JPG")
let destinationCIImage = CIImage(contentsOf: destinationURL)
```

##### 2953417

The key difference of transition filters from their normal filter chain counterparts is the dependence on time.  After creating a [`CIFilter`](cifilter.md) from the [`Transition Filters`](transition_filters.md) category, you set the value of the `time` parameter to a float between `0.0` and `1.0` to indicate how far along the transition has progressed.  

Write each transition filter to accept time as an input parameter, and reapply the filter at a regular interval to transform the image from its source state to the target state.

```swift
import simd

func dissolveFilter(_ inputImage: CIImage,
                    to targetImage: CIImage,
                    time: TimeInterval) -> CIImage? {
    let time = simd_smoothstep(0, 1, time)        
    let filter = CIFilter.dissolveTransition()
    filter.inputImage = inputImage
    filter.targetImage = targetImage
    filter.time = Float(time)
    return filter.outputImage
}
```

You don’t need to pass time linearly from `0.0` to `1.0`. In fact, you can advance the transition at a variable rate by modulating the time variable with a function, such as `simd_smoothstep`, which is a smooth ramp function clamped between two values, imbuing the dissolve effect with an ease-in ease-out feel.

![A graphic of simd_smoothstep, showing a smooth ramp between 0 and 1](https://docs-assets.developer.apple.com/published/0aa81a34f5/2960171@2x.png)

##### 2953422

Like the dissolve transition, you can write the pixelate transition filter as a time-dependent function as well.

```swift
import simd

func pixelateFilter(_ inputImage: CIImage, time: TimeInterval) -> CIImage? {
    let scale = simd_smoothstep(1, 0, fabs(time))
    let filter = CIFilter.pixellate()
    filter.inputImage = inputImage
    filter.scale = 100 * Float(scale)
    return filter.outputImage
}
```

As with the dissolve filter, you can modify the speed and acceleration of the transition by changing the way time varies between `0.0` and `1.0`.  In this case, unlike the [`dissolveTransition()`](cifilter/3228314-dissolvetransition.md) filter, the [`pixellate()`](cifilter/3228393-pixellate.md) filter accepts a s`cale`, which you can vary over a smoothened triangle function: `simd_smoothstep(1, 0, abs(time))`.  

![A graphic depicting simd_smoothstep(1, 0, abs(time)), a smoothened triangle ramp between 0 and 1](https://docs-assets.developer.apple.com/published/bf0f2a0bba/2960172@2x.png)

This function puts the peak of the pixelation at the middle of the transition: the pixels start and end small, closely approximating the source image, but as the transition reaches its halfway point, the pixels scale to their largest size, effectively blocking out the moment farthest from source and target.

##### 2953419

In writing the filter functions to accept a time parameter, you parametrized the transition effect moving from source to target. Now, you must move time forward when you want to perform the transition.

Adding a [`CADisplayLink`](https://developer.apple.com/documentation/quartzcore/cadisplaylink) to your run loop gives you a way to refresh an image every time a screen redraw occurs, so you can execute on a reliably regular time interval. In the case of a transition, you need only perform the following steps:

1. Create the display link to call an update function.
2. Add to your app’s main run loop to begin the transition. Start time at `0.0` and track time through the update function.
3. In the update function, update the transition filters’ `inputTime` value and refresh the filtered image. Since this example chains two filters for a simultaneous effect, update both filters.
4. In the update function, remove the link once time has expired.

> **Note**: Adding a [`Timer`](https://developer.apple.com/documentation/foundation/timer) may seem like a logical strategy for stepping time, but the display link fires with greater precision in sync with screen redraws.

###### 2953691

```swift
displayLink = CADisplayLink(target: self, 
                            selector: #selector(stepTime))
```

Keeping the display link around beyond function scope allows you to remove it when the transition completes.

###### 2953687

To begin the transition effect, add the [`CADisplayLink`](https://developer.apple.com/documentation/quartzcore/cadisplaylink) to your program’s main run loop, so it can execute each time step and redraw the transitioning [`CIImage`](ciimage.md).

```swift
func beginTransition() {
        
    time = 0
    dt = 0.005
        
    displayLink = CADisplayLink(target: self,
                                selector: #selector(stepTime))
    displayLink.add(to: RunLoop.current,
                    forMode: RunLoopMode.defaultRunLoopMode)
}
```

###### 2953689

The [`CADisplayLink`](https://developer.apple.com/documentation/quartzcore/cadisplaylink) should call a time-stepping function on each pass through the run loop.  Inside this function, recompute the filtered image with that frame's `time` variable.

```swift
@objc
func stepTime() {
    
   time += dt
        
   // End transition after 1 second
   if time > 1 {
       displayLink.remove(from:RunLoop.main, forMode:RunLoopMode.defaultRunLoopMode)
   } else {
       guard let dissolvedCIImage = dissolveFilter(sourceCIImage,
                                                   to:finalCIImage,
                                                   time:time) else {
                                                      return
       }
       guard let pixelatedCIImage = pixelateFilter(dissolvedCIImage,
                                                   time:time) else {
                                                      return
       }
       // imageView and ciContext are properties of the class.
       showCIImage(pixelatedCIImage, in:imageView, context:ciContext)
   }
}
```

As a convenience, the following helper function shows a CIImage in a UIImageView.

```swift
func showCIImage(_ ciImage: CIImage,
                 in imageView: UIImageView,
                 context: CIContext) {
    
    guard let cgImage = context.createCGImage(ciImage,
                                              from: ciImage.extent) else {
                                                 return
    }
    let uiImage = UIImage(CGImage:cgImage)
        
    imageView.image = uiImage
}
```

##### 2953420

The Core Image framework provides many distinct visual effects through its built-in catalog of filters. You can substitute a different transition effect for the dissolve and pixelation effects. 

See filters under the [`Transition Filters`](transition_filters.md) collection for other effects to try.

For example, the [`copyMachineTransition()`](cifilter/3228304-copymachinetransition.md) filter passes a scanning light over the source image as it transforms into the target image.

![Copy machine transition from a beach at sunset to a beach at daytime with rainbow in the sky](https://docs-assets.developer.apple.com/published/90629758f9/18b2120f-ba94-46c2-bb53-8c8e8c7c92e8.png)

The [`pageCurlWithShadowTransition()`](cifilter/3228376-pagecurlwithshadowtransition.md) filter simulates the turn of a page, peeling the source image toward the right to reveal the target image underneath. You can include a separate image on the back of the flipped page.

![Page curl transition from a photo of a beach at daytime with rainbow in the sky to a photo of a beach at sunset, with a flower image on the back of the page](https://docs-assets.developer.apple.com/published/ecdd6f2d0b/adb2afa0-1ee1-4d56-b572-84f89f858a20.png)

The [`barsSwipeTransition()`](cifilter/3228270-barsswipetransition.md) slices the source image into vertical bars that sequentially slide off the page, revealing the target image underneath.

![Bar swipe transition from a beach at sunset to a beach at daytime with rainbow in the sky](https://docs-assets.developer.apple.com/published/8a5434313e/0abd4390-94e0-46dd-849c-01db7f3a513e.png)

You can apply transitions such as accordion folding, flash photography, disintegration, and watery rippling. Substitute the dissolve and pixellate filters with others from the same category, and tweak the t`ime` or s`cale` parameter to customize the effect to fit your app.

## See Also

- [Applying a Chroma Key Effect](applying_a_chroma_key_effect.md)
  Replace a color in one image with the background from another.
- [Selectively Focusing on an Image](selectively_focusing_on_an_image.md)
  Focus on a part of an image by applying Gaussian blur and gradient masks.
- [Simulating Scratchy Analog Film](simulating_scratchy_analog_film.md)
  Degrade the quality of an image to make it look like dated, analog film.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/customizing_image_transitions)*