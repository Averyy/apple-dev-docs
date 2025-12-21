# CameraRegionView

**Framework**: VisionKit  
**Kind**: struct

This view displays a stabilized region of interest within a person’s view and provides passthrough camera feed for that selected region.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency struct CameraRegionView
```

#### Overview

`CameraRegionView` needs enterprise API access in order to be used. To use this view, you need to apply for the [`Camera Region access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.arkit.camera-region.allow) entitlement. For more information, including how to apply for this entitlement, see [`Building spatial experiences for business apps with enterprise APIs for visionOS`](https://developer.apple.com/documentation/visionOS/building-spatial-experiences-for-business-apps-with-enterprise-apis).

This is a standalone view used in a `WindowGroup` that a person can freely move and place in order to position the desired region of interest. Examples of possible regions of interest are documents, user manuals, gauges, and displays.

The view also allows additional post-processing of passthrough camera frames. These stabilized camera frames of the selected region of interest are directly rendered into the view. The framework provides these frames to enterprise developers before rendering them on screen, so developers can apply any enhancements or modifications prior to the rendering within the view.

```swift
struct AppScene: Scene {
    var body: some Scene {
         // Enterprise use case which requires an enterprise license and
         // entitlement.
         WindowGroup(id: "WithEnterpriseLicense") {
             CameraRegionView() { result in
                 switch result {
                     case .success(let context):
                         let pixelBuffer = context.pixelBuffer

                         // Add desired changes to pixel buffer.
                        return pixelBuffer
                    case .failure(let error):
                       // Handle errors.
                       return nil
                }
             }
         }
         .windowResizability(.contentSize)
     }
 }
```

> **Note**: The frame rate within the `CameraRegionView` isn’t expected to match the frame rate of the passthrough view. The CameraRegionView’s base functionality and any post-processing requires additional computation time, so the frame rate runs slower in this view in exchange for providing additional stabilization and enhancement.

## Topics

### Creating a view
- [init(isContrastAndVibrancyEnhancementEnabled: Bool, pixelBufferProcessor: ((Result<CameraRegionView.PixelBufferProcessingContext, any Error>) async -> CVReadOnlyPixelBuffer?)?)](cameraregionview/init(iscontrastandvibrancyenhancementenabled:pixelbufferprocessor:).md)
  Creates a view that renders a spatial camera region and optionally applies contrast enhancement.
### Setting up frame processing in your view
- [CameraRegionView.PixelBufferProcessingContext](cameraregionview/pixelbufferprocessingcontext.md)
  A context which provides the pixel buffer for a passthrough frame.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)
  Add a Live Text interface that enables users to perform actions with text and QR codes that appear in images.
- [class ImageAnalyzer](imageanalyzer.md)
  An object that finds items in images that people can interact with, such as subjects, text, and QR codes.
- [class ImageAnalysis](imageanalysis.md)
  An object that represents the results of analyzing an image, and provides the input for the Live Text interface object.
- [class ImageAnalysisInteraction](imageanalysisinteraction.md)
  An interface that enables people to interact with recognized text, barcodes, and other objects in an image.
- [protocol ImageAnalysisInteractionDelegate](imageanalysisinteractiondelegate.md)
  A delegate that handles image-analysis and user-interaction callbacks for an interaction object.
- [class ImageAnalysisOverlayView](imageanalysisoverlayview.md)
  A view that enables people to interact with recognized text, barcodes, and other objects in an image.
- [protocol ImageAnalysisOverlayViewDelegate](imageanalysisoverlayviewdelegate.md)
  A delegate that handles image-analysis and user-interaction callbacks for an overlay view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/cameraregionview)*