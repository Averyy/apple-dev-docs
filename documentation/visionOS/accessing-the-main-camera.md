# Accessing the main camera

**Framework**: visionOS

Add camera-based features to enterprise apps.

**Availability**:
- visionOS 2.0+
- Xcode 16.0+

#### Overview

This sample code project demonstrates how to use ARKit to access and display the left main camera frame in your visionOS app. You can use this functionality to implement computer vision-powered experiences or live streaming in your enterprise app. For instance, support technicians can live stream their surroundings to remote experts for improved guidance.

##### Configure the Sample Code Project

Replace `Enterprise.license` with your license file. The sample app requires a valid license file to display the main camera.

##### Request the Entitlement

Main camera access is a part of enterprise APIs for visionOS, a collection of APIs that unlock capabilities for enterprise customers. To use main camera access, you need to apply for the [`Main camera access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.arkit.main-camera-access.allow) entitlement. For more information, including how to apply for this entitlement, see [`Building spatial experiences for business apps with enterprise APIs for visionOS`](building-spatial-experiences-for-business-apps-with-enterprise-apis.md).

##### Add Usage Descriptions for Arkit Data Access

To help protect people’s privacy, visionOS limits app access to cameras and other sensors in Apple Vision Pro. You need to add an `NSEnterpriseMCAMUsageDescription` to your app’s information property list to provide a usage description that explains how your app uses the data these sensors provide. People see this description when your app prompts for access to camera data.

> **Note**: In visionOS, ARKit is only available in an immersive space. See [`Setting up access to ARKit data`](setting-up-access-to-arkit-data.md) to learn more about opening an immersive space and requesting authorization for ARKit data access. To learn more about best practices for privacy, see [`Adopting best practices for privacy and user preferences`](adopting-best-practices-for-privacy.md).

##### Access and Display Main Camera Frames

The following code example accesses and displays the left main camera at the highest available resolution. To access the camera, start an [`ARKitSession`](https://developer.apple.com/documentation/ARKit/ARKitSession) with a [`CameraFrameProvider`](https://developer.apple.com/documentation/ARKit/CameraFrameProvider), and then request [`CameraFrameProvider.CameraFrameUpdates`](https://developer.apple.com/documentation/ARKit/CameraFrameProvider/CameraFrameUpdates) in a given format. ARKit delivers a stream of [`CameraFrame`](https://developer.apple.com/documentation/ARKit/CameraFrame) instances; each frame includes a [`CameraFrame.Sample`](https://developer.apple.com/documentation/ARKit/CameraFrame/Sample) containing a [`pixelBuffer`](https://developer.apple.com/documentation/ARKit/CameraFrame/Sample/pixelBuffer) and [`CameraFrame.Sample.Parameters`](https://developer.apple.com/documentation/ARKit/CameraFrame/Sample/Parameters-swift.struct) describing the frame’s characteristics.

```swift
import ARKit
import RealityKit
import SwiftUI

struct MainCameraView: View {
    @State private var arkitSession = ARKitSession()
    @State private var pixelBuffer: CVPixelBuffer?
    
    let emptyImage = Image(systemName: "camera")

    var body: some View {
        let image = pixelBuffer?.image ?? emptyImage
        
        image
        .resizable()
        .scaledToFit()
        .task {
            
            // Check wether there's support for camera access; otherwise, handle this case.
            guard CameraFrameProvider.isSupported else {
                return
            }
            
            let cameraFrameProvider = CameraFrameProvider()

            try? await arkitSession.run([cameraFrameProvider])
            
            // Read the video formats that the left main camera supports.
            let formats = CameraVideoFormat.supportedVideoFormats(for: .main, cameraPositions: [.left])
        
            // Find the highest resolution format.
            let highResolutionFormat = formats.max { $0.frameSize.height < $1.frameSize.height }

            // Request an asynchronous sequence of camera frames.
            guard let highResolutionFormat,
                  let cameraFrameUpdates = cameraFrameProvider.cameraFrameUpdates(for: highResolutionFormat) else {
                return
            }
            
            for await cameraFrame in cameraFrameUpdates {

                if let sample = cameraFrame.sample(for: .left) {
                    
                    // Update the `pixelBuffer` to render the frame's image.
                    pixelBuffer = sample.pixelBuffer
                    
                    let parameters = sample.parameters
                    
                    // If needed, take action with the frame's parameters.
                    print(
                         """

                         Intrinsics: \(parameters.intrinsics)
                         Extrinsics: \(parameters.extrinsics)
                         """)
                }

            }
        }
    }
}
```

To display the frame’s content, convert its [`pixelBuffer`](https://developer.apple.com/documentation/AVFoundation/AVCapturePhoto/pixelBuffer) to an [`Image`](https://developer.apple.com/documentation/SwiftUI/Image) using the following extension:

```swift
extension CVPixelBuffer {
    var image: Image? {
        let ciImage = CIImage(cvPixelBuffer: self)
        let context = CIContext(options: nil)
        
        guard let cgImage = context.createCGImage(ciImage, from: ciImage.extent) else {
            return nil
        }

        let uiImage = UIImage(cgImage: cgImage)

        return Image(uiImage: uiImage)
    }
}
```

## See Also

- [Building spatial experiences for business apps with enterprise APIs for visionOS](building-spatial-experiences-for-business-apps-with-enterprise-apis.md)
  Grant enhanced sensor access and increased platform control to your visionOS app by using entitlements.
- [Displaying video from connected devices](displaying-video-from-connected-devices.md)
  Show video from devices connected with the Developer Strap in your visionOS app.
- [Locating and decoding barcodes in 3D space](locating-and-decoding-barcodes-in-3d-space.md)
  Create engaging, hands-free experiences based on barcodes in a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/accessing-the-main-camera)*