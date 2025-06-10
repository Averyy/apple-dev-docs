# Detecting Human Body Poses in Images

**Framework**: Vision

Add the capability to detect human body poses to your app using the Vision framework.

#### Overview

A primary goal of Vision is to provide you with tools to help you better identify and understand people in your visual data. Starting in iOS 14 and macOS 11, Vision adds the powerful new ability to identify human body poses. It does so by detecting up to 19 unique body points, as shown in the figure below.

![An illustration depicting a model of the human body. The body points that Vision detects are the right and left wrists, elbows, shoulders, ears, eyes, hips, knees, and ankles; and the nose, neck, and root, or center point.](https://docs-assets.developer.apple.com/published/fba5d5b4ffa9b8d7d659dbe698f427df/media-3625688%402x.png)

You can use Vision’s capability for detecting human body poses on its own or with Core ML. Combining Vision with the power of machine learning enables a wide variety of feature possibilities. For example, a safety-training app could help employees use correct ergonomics, a fitness app could automatically track the exercise a user performs, and a media-editing app could find photos or videos based on pose similarity.

##### Perform a Body Pose Request

Vision provides its body pose-detection capabilities through [`VNDetectHumanBodyPoseRequest`](vndetecthumanbodyposerequest.md), an image-based request type that detects key body points. The following example shows how to use [`VNImageRequestHandler`](vnimagerequesthandler.md) to perform a [`VNDetectHumanBodyPoseRequest`](vndetecthumanbodyposerequest.md) for detecting body points in the specified [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage).

```swift
// Get the CGImage on which to perform requests.
guard let cgImage = UIImage(named: "bodypose")?.cgImage else { return }

// Create a new image-request handler.
let requestHandler = VNImageRequestHandler(cgImage: cgImage)

// Create a new request to recognize a human body pose.
let request = VNDetectHumanBodyPoseRequest(completionHandler: bodyPoseHandler)

do {
    // Perform the body pose-detection request.
    try requestHandler.perform([request])
} catch {
    print("Unable to perform the request: \(error).")
}
```

> **Note**:  If you have a known region of interest (ROI) in an image, you can specify it using the request’s [`regionOfInterest`](vnimagebasedrequest/regionofinterest.md) property. Setting an ROI reduces the region in the image where the request performs its analysis, which generally results in more accurate pose estimation.

##### Process the Results

After the request handler processes the request, it calls the request’s completion closure, passing it the request and any errors that occurred. Retrieve the observations by querying the request object for its [`results`](vnrequest/results.md), which it returns as an array of [`VNHumanBodyPoseObservation`](vnhumanbodyposeobservation.md) objects. The request returns a unique observation for each detected human body pose, with each containing the recognized points and a confidence score indicating the accuracy of the observation.

```swift
func bodyPoseHandler(request: VNRequest, error: Error?) {
    guard let observations =
            request.results as? [VNHumanBodyPoseObservation] else { 
        return 
    }
    
    // Process each observation to find the recognized body pose points.
    observations.forEach { processObservation($0) }
}
```

##### Retrieve the Points

Retrieve the points of interest from the observation by calling its [`recognizedPoints(_:)`](vnhumanbodyposeobservation/recognizedpoints(_:).md) method. The argument you pass to this method is a key that identifies all of the points for a particular body region (see [`VNHumanBodyPoseObservation.JointsGroupName`](vnhumanbodyposeobservation/jointsgroupname.md) for supported values). This method returns the recognized points for the region as a dictionary of [`VNRecognizedPoint`](vnrecognizedpoint.md) objects keyed by joint name. Each instance of [`VNRecognizedPoint`](vnrecognizedpoint.md) provides the `X` and `Y` coordinates, in normalized space, and a confidence score for the point. Ignore any recognized points with a [`confidence`](vndetectedpoint/confidence.md) value of 0, because they’re invalid.

The following code example retrieves all of the recognized points for the torso and maps them to an array of [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint) objects. The example first retrieves the recognized points of the torso by calling [`recognizedPoints(_:)`](vnhumanbodyposeobservation/recognizedpoints(_:).md)with the [`torso`](vnhumanbodyposeobservation/jointsgroupname/torso.md) key. It then iterates over the specific point keys of the torso and retrieves their associated [`VNRecognizedPoint`](vnrecognizedpoint.md) object. Finally, if a point’s [`confidence`](vndetectedpoint/confidence.md) score is greater than 0, it extracts the point’s coordinates as a [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint).

```swift
func processObservation(_ observation: VNHumanBodyPoseObservation) {
    
    // Retrieve all torso points.
    guard let recognizedPoints =
            try? observation.recognizedPoints(.torso) else { return }
    
    // Torso joint names in a clockwise ordering.
    let torsoJointNames: [VNHumanBodyPoseObservation.JointName] = [
        .neck,
        .rightShoulder,
        .rightHip,
        .root,
        .leftHip,
        .leftShoulder
    ]
    
    // Retrieve the CGPoints containing the normalized X and Y coordinates.
    let imagePoints: [CGPoint] = torsoJointNames.compactMap {
        guard let point = recognizedPoints[$0], point.confidence > 0 else { return nil }
        
        // Translate the point from normalized-coordinates to image coordinates.
        return VNImagePointForNormalizedPoint(point.location,
                                              Int(imageSize.width),
                                              Int(imageSize.height))
    }
    
    // Draw the points onscreen.
    draw(points: imagePoints)
}
```

> **Note**:  The points the [`recognizedPoints(_:)`](vnhumanbodyposeobservation/recognizedpoints(_:).md) method returns are in normalized coordinates (0.0 to 1.0), with the origin at the bottom-left. Use the [`VNImagePointForNormalizedPoint(_:_:_:)`](vnimagepointfornormalizedpoint(_:_:_:).md) function to translate the normalized points to the input image coordinates.

For an example of how you can use and visualize recognized body points, see the [`Building a feature-rich app for sports analysis`](building-a-feature-rich-app-for-sports-analysis.md) sample app.

##### Improve Pose Detection Accuracy

To achieve the most accurate results from Vision’s human body pose-detection capabilities, consider the following points:

- The subject’s height should ideally be at least a third of the overall image height.
- A large portion of the subject’s key body regions and points should be present in the image.
- A subject wearing flowing or robe-like clothing reduces the detection accuracy.
- Attempting to detect body poses in dense crowd scenes is likely to produce inaccurate results.

## See Also

- [Detecting Hand Poses with Vision](detecting-hand-poses-with-vision.md)
  Create a virtual drawing app by using Vision’s capability to detect hand poses.
- [class VNDetectHumanBodyPoseRequest](vndetecthumanbodyposerequest.md)
  A request that detects a human body pose.
- [class VNDetectHumanHandPoseRequest](vndetecthumanhandposerequest.md)
  A request that detects a human hand pose.
- [class VNRecognizedPointsObservation](vnrecognizedpointsobservation.md)
  An observation that provides the points the analysis recognized.
- [class VNHumanBodyPoseObservation](vnhumanbodyposeobservation.md)
  An observation that provides the body points the analysis recognized.
- [class VNHumanHandPoseObservation](vnhumanhandposeobservation.md)
  An observation that provides the hand points the analysis recognized.
- [class VNPoint](vnpoint.md)
  An immutable object that represents a single 2D point in an image.
- [class VNDetectedPoint](vndetectedpoint.md)
  An object that represents a normalized point in an image, along with a confidence value.
- [class VNRecognizedPoint](vnrecognizedpoint.md)
  An object that represents a normalized point in an image, along with an identifier label and a confidence value.
- [struct VNRecognizedPointKey](vnrecognizedpointkey.md)
  The data type for all recognized point keys.
- [struct VNRecognizedPointGroupKey](vnrecognizedpointgroupkey.md)
  The data type for all recognized-point group keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecting-human-body-poses-in-images)*