# Core Image

**Framework**: Core Image

Use built-in or custom filters to process still and video images.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

#### Overview

Core Image is an image processing and analysis technology that provides high-performance processing for still and video images. Use the many built-in image filters to process images and build complex effects by chaining filters. For a list of all the built-in filters see the [`Filter Catalog`](https://developer.apple.com/documentation/coreimage#4390024).

You can also create new effects with custom filters and image processors; see [`Custom Filters`](https://developer.apple.com/documentation/coreimage#2880063).

## Topics

### Essentials
- [Processing an Image Using Built-in Filters](processing_an_image_using_built-in_filters.md)
  Apply effects such as sepia tint, highlight strengthening, and scaling to images.
- [class CIContext](cicontext.md)
  An evaluation context for rendering image processing results and performing image analysis.
- [class CIImage](ciimage.md)
  A representation of an image to be processed or produced by Core Image filters.
### Filters
- [class CIFilter](cifilter.md)
  An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [class CIRAWFilter](cirawfilter.md)
  A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- [class CIColor](cicolor.md)
  The component values defining a color in a specific color space.
- [class CIVector](civector.md)
  A container for coordinate values, direction vectors, matrices, and other non-scalar values, typically used in Core Image for filter parameters.
### Filter Catalog
- [Blur Filters](blur_filters.md)
  Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](color_adjustment_filters.md)
  Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](color_effect_filters.md)
  Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](composite_operations.md)
  Composite images by using a range of blend modes and compositing operators. 
- [Convolution Filters](convolution_filters.md)
  Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](distortion_filters.md)
  Apply distortion to images.
- [Generator Filters](generator_filters.md)
  Generate barcode, geometric, and special-effect images.
- [Geometry Adjustment Filters](geometry_adjustment_filters.md)
  Translate, scale, and rotate images in 2D and 3D.
- [Gradient Filters](gradient_filters.md)
  Generate linear and radial gradients.
- [Halftone Effect Filters](halftone_effect_filters.md)
  Simulate monochrome and CMYK halftone screens.
- [Reduction Filters](reduction_filters.md)
  Create statistical information about an image.
- [Sharpening Filters](sharpening_filters.md)
  Apply sharpening to images.
- [Stylizing Filters](stylizing_filters.md)
  Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](tile_effect_filters.md)
  Produce tiled images from source images.
- [Transition Filters](transition_filters.md)
  Transition between two images by using effects including page curl and swipe.
### Filter Recipes
- [Applying a Chroma Key Effect](applying_a_chroma_key_effect.md)
  Replace a color in one image with the background from another.
- [Selectively Focusing on an Image](selectively_focusing_on_an_image.md)
  Focus on a part of an image by applying Gaussian blur and gradient masks.
- [Customizing Image Transitions](customizing_image_transitions.md)
  Transition between images in creative ways using Core Image filters.
- [Simulating Scratchy Analog Film](simulating_scratchy_analog_film.md)
  Degrade the quality of an image to make it look like dated, analog film.
### Custom Filters
- [Writing Custom Kernels](writing_custom_kernels.md)
  Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [class CIKernel](cikernel.md)
  A GPU-based image-processing routine used to create custom Core Image filters.
- [class CIColorKernel](cicolorkernel.md)
  A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [class CIWarpKernel](ciwarpkernel.md)
  A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [class CIBlendKernel](ciblendkernel.md)
  A GPU-based image-processing routine that is optimized for blending two images.
- [class CISampler](cisampler.md)
  An object that retrieves pixel samples for processing by a filter kernel.
- [class CIFilterShape](cifiltershape.md)
  A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [struct CIFormat](ciformat.md)
  Pixel data formats for image input, output, and processing.
### Custom Image Processors
- [class CIImageProcessorKernel](ciimageprocessorkernel.md)
  The abstract class you extend to create custom image processors that can integrate with Core Image workflows.
- [protocol CIImageProcessorInput](ciimageprocessorinput.md)
  A container of image data and information for use in a custom image processor. 
- [protocol CIImageProcessorOutput](ciimageprocessoroutput.md)
  A container for writing image data and information produced by a custom image processor. 
### Custom Render Destination
- [Generating an animation with a Core Image Render Destination](generating_an_animation_with_a_core_image_render_destination.md)
  Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [class CIRenderDestination](cirenderdestination.md)
  A specification for configuring all attributes of a render task's destination and issuing asynchronous render tasks.
- [class CIRenderInfo](cirenderinfo.md)
  An encapsulation of a render task's timing, passes, and pixels processed.
- [class CIRenderTask](cirendertask.md)
  A single render task issued in conjunction with [`CIRenderDestination`](cirenderdestination.md).
- [enum CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md)
  Different ways of representing alpha.
### Feedback-Based Processing
- [class CIImageAccumulator](ciimageaccumulator.md)
  An object that manages feedback-based image processing for tasks such as painting or fluid simulation.
### Barcode Descriptions
- [class CIBarcodeDescriptor](cibarcodedescriptor.md)
  An abstract base class that represents a machine-readable code's attributes.
- [class CIQRCodeDescriptor](ciqrcodedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a square QR code symbol.
- [class CIAztecCodeDescriptor](ciazteccodedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents an Aztec code symbol.
- [class CIPDF417CodeDescriptor](cipdf417codedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a PDF417 symbol.
- [class CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md)
  A concrete subclass of [`CIBarcodeDescriptor`](cibarcodedescriptor.md) that represents a Data Matrix code symbol.
### Image Feature Detection
- [class CIDetector](cidetector.md)
  An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- [class CIFeature](cifeature.md)
  The abstract superclass for objects representing notable features detected in an image.
- [class CIFaceFeature](cifacefeature.md)
  Information about a face detected in a still or video image.
- [class CIRectangleFeature](cirectanglefeature.md)
  Information about a rectangular region detected in a still or video image.
- [class CITextFeature](citextfeature.md)
  Information about a region likely to contain text detected in a still or video image.
- [class CIQRCodeFeature](ciqrcodefeature.md)
  Information about a Quick Response code detected in a still or video image.
### Image Units
- [class CIPlugIn](ciplugin.md)
  The mechanism for loading image units in macOS. 
- [class CIFilterGenerator](cifiltergenerator.md)
  An object that creates and configures chains of individual image filters. 
- [protocol CIPlugInRegistration](cipluginregistration.md)
  The interface for loading Core Image image units.
- [protocol CIFilterConstructor](cifilterconstructor.md)
  A general interface for objects that produce [`CIFilter`](cifilter.md) instances.
### Constants
- [var COREIMAGE_SUPPORTS_IOSURFACE: Int32](coreimage_supports_iosurface.md)
  Support for IOSurface enabled.
- [var COREIMAGE_SUPPORTS_OPENGLES: Int32](coreimage_supports_opengles.md)
  Support for OpenGL ES enabled.
### Protocols
- [protocol CIAreaBoundsRed](ciareaboundsred.md)
- [protocol CIMaximumScaleTransform](cimaximumscaletransform.md)
- [protocol CIToneMapHeadroom](citonemapheadroom.md)

## See Also

- [Core Image Filter Reference](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346-Reference)
- [Core Image Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage)*