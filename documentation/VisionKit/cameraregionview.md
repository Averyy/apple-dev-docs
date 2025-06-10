# CameraRegionView

**Framework**: VisionKit  
**Kind**: struct

CameraRegionView displays a view of a stabilized region of interest within a user’s view, and then provide Passthrough camera feed for the selected region. It also allows additional post-processing of the passthrough camera frames. Example of such region of interest could be documents, a user manual, gauges or displays.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency struct CameraRegionView
```

#### Overview

CameraRegionView is a standalone view used in a WindowGroup that a user can freely move and place, just as they can with any other window to select the region. Stabilized camera frames of the selected region will be rendered directly into this view.

These frames are provided to Enterprise developers before being rendered on screen, so they can apply any enhancements or modifications prior to them being rendered within the view.

Note that based on potential computation time required for both the base functionality as well as post-processing, the frame rate within the View is not expected to match the rest of the user’s Passthrough view, and will be running more slowly, in exchange for providing the additional functionality of stabilization and enhancement.

e.g:

```swift
struct AppScene: Scene {
    var body: some Scene {
        // Enterprise use case which requires enterprise license and entitlement
        WindowGroup(id: "WithEnterpriseLicense") {
            CameraRegionView() { result in
                switch result {
                    case .success(let context):
                        let pixelBuffer = context.pixelBuffer

                        // make desired changes to pixel buffer ...
                        return pixelBuffer
                    case .failure(let error):
                        // handle error ...
                        return nil
                }
            }
        }
        .windowResizability(.contentSize)
    }
}
```

## Topics

### Structures
- [CameraRegionView.PixelBufferProcessingContext](cameraregionview/pixelbufferprocessingcontext.md)
  Pixel buffer processing context currently provides the pixel buffer for a passthrough frame.
### Initializers
- [init(isContrastAndVibrancyEnhancementEnabled: Bool, pixelBufferProcessor: ((Result<CameraRegionView.PixelBufferProcessingContext, any Error>) async -> CVReadOnlyPixelBuffer?)?)](cameraregionview/init(iscontrastandvibrancyenhancementenabled:pixelbufferprocessor:).md)
  Creates a view that renders a spatial camera region, and optionally applies contrast enhancement.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/cameraregionview)*