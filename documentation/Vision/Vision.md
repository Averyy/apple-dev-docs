# Vision

**Framework**: Vision  
**Kind**: module

Apply computer vision algorithms to perform a variety of tasks on input images and videos.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

#### Overview

The Vision framework combines machine learning technologies and Swift’s concurrency features to perform computer vision tasks in your app. Use the Vision framework to analyze images for a variety of purposes:

- Tracking human and animal body poses or the trajectory of an object
- Recognizing text in 18 different languages
- Detecting faces and face landmarks, such as eyes, nose, and mouth
- Performing hand tracking to enable new device interactions
- Calculating an aesthetics score to determine how memorable a photo is

![An illustration showing a dog, and a magnifying glass depicting the dog being analyzed.](https://docs-assets.developer.apple.com/published/c745ff2988bec9749a8ba2313d77598e/vision-framework%402x.png)

To begin using the framework, you create a request for the type of analysis you want to do. Each request conforms to the [`VisionRequest`](visionrequest.md) protocol. You then perform the request to get an observation object — or an array of observations — with the analysis details for the request. There are more than 25 requests available to choose from. Vision also allows the use of custom Core ML models for tasks like classification or object detection.

> **Note**:  Starting in iOS 18.0, the Vision framework provides a new Swift-only API. See [`Original Objective-C and Swift API`](original-objective-c-and-swift-api.md) to view the original API.

 Starting in iOS 18.0, the Vision framework provides a new Swift-only API. See [`Original Objective-C and Swift API`](original-objective-c-and-swift-api.md) to view the original API.

## Topics

### Still-image analysis
- [Classifying images for categorization and search](classifying-images-for-categorization-and-search.md)
  Analyze and label images using a Vision classification request.
- [struct ClassifyImageRequest](classifyimagerequest.md)
  A request to classify an image.
- [protocol ImageProcessingRequest](imageprocessingrequest.md)
  A type for image-analysis requests that focus on a specific part of an image.
- [class ImageRequestHandler](imagerequesthandler.md)
  An object that processes one or more image-analysis requests pertaining to a single image.
- [protocol VisionRequest](visionrequest.md)
  A type for image-analysis requests.
- [protocol VisionObservation](visionobservation.md)
  A type for objects produced by image-analysis requests.
### Image sequence analysis
- [class GeneratePersonSegmentationRequest](generatepersonsegmentationrequest.md)
  A request that produces a matte image for a person it finds in the input image.
- [struct GeneratePersonInstanceMaskRequest](generatepersoninstancemaskrequest.md)
  A request that produces a mask of individual people it finds in the input image.
- [struct DetectDocumentSegmentationRequest](detectdocumentsegmentationrequest.md)
  A request that detects rectangular regions that contain text in the input image.
- [protocol StatefulRequest](statefulrequest.md)
  The protocol for a type that builds evidence of a condition over time.
### Image aesthetics analysis
- [Generating high-quality thumbnails from videos](generating-thumbnails-from-videos.md)
  Identify the most visually pleasing frames in a video by using the image-aesthetics scores request.
- [struct CalculateImageAestheticsScoresRequest](calculateimageaestheticsscoresrequest.md)
  A request that analyzes an image for aesthetically pleasing attributes.
### Saliency analysis
- [struct GenerateAttentionBasedSaliencyImageRequest](generateattentionbasedsaliencyimagerequest.md)
  An object that produces a heat map that identifies the parts of an image most likely to draw attention.
- [struct GenerateObjectnessBasedSaliencyImageRequest](generateobjectnessbasedsaliencyimagerequest.md)
  A request that generates a heat map that identifies the parts of an image most likely to represent objects.
### Object tracking
- [class TrackObjectRequest](trackobjectrequest.md)
  An image-analysis request that tracks the movement of a previously identified object across multiple images or video frames.
- [class TrackRectangleRequest](trackrectanglerequest.md)
  An image-analysis request that tracks movement of a previously identified rectangular object across multiple images or video frames.
### Face and body detection
- [Analyzing a selfie and visualizing its content](analyzing-a-selfie-and-visualizing-its-content.md)
  Calculate face-capture quality and visualize facial features for a collection of images using the Vision framework.
- [struct DetectFaceRectanglesRequest](detectfacerectanglesrequest.md)
  A request that finds faces within an image.
- [struct DetectFaceLandmarksRequest](detectfacelandmarksrequest.md)
  An image-analysis request that finds facial features like eyes and mouth in an image.
- [struct DetectFaceCaptureQualityRequest](detectfacecapturequalityrequest.md)
  A request that produces a floating-point number that represents the capture quality of a face in a photo.
- [struct DetectHumanRectanglesRequest](detecthumanrectanglesrequest.md)
  A request that finds rectangular regions that contain people in an image.
### Body and hand pose detection
- [struct DetectHumanBodyPoseRequest](detecthumanbodyposerequest.md)
  A request that detects a human body pose.
- [struct DetectHumanHandPoseRequest](detecthumanhandposerequest.md)
  A request that detects a human hand pose.
- [protocol PoseProviding](poseproviding.md)
  An observation that provides a collection of joints that make up a pose.
- [enum Chirality](chirality.md)
  The hand sidedness of a pose.
- [struct Joint](joint.md)
  A pose joint represented as a normalized point in an image, along with a label and a confidence value.
### 3D body pose detection
- [class DetectHumanBodyPose3DRequest](detecthumanbodypose3drequest.md)
  A request that detects points on human bodies in 3D space, relative to the camera.
- [struct Joint3D](joint3d.md)
  An object that represents a body pose joint in 3D space.
### Text detection
- [Locating and displaying recognized text](locating-and-displaying-recognized-text.md)
  Perform text recognition on a photo using the Vision framework’s text-recognition request.
- [struct DetectTextRectanglesRequest](detecttextrectanglesrequest.md)
  An image-analysis request that finds regions of visible text in an image.
- [struct RecognizeTextRequest](recognizetextrequest.md)
  An image-analysis request that recognizes text in an image.
### Barcode detection
- [struct DetectBarcodesRequest](detectbarcodesrequest.md)
  A request that detects barcodes in an image.
### Trajectory, contour, and horizon detection
- [class DetectTrajectoriesRequest](detecttrajectoriesrequest.md)
  A request that detects the trajectories of shapes moving along a parabolic path.
- [struct DetectContoursRequest](detectcontoursrequest.md)
  A request that detects the contours of the edges of an image.
- [struct DetectHorizonRequest](detecthorizonrequest.md)
  An image-analysis request that determines the horizon angle in an image.
### Animal detection
- [struct DetectAnimalBodyPoseRequest](detectanimalbodyposerequest.md)
  A request that detects an animal body pose.
- [struct RecognizeAnimalsRequest](recognizeanimalsrequest.md)
  A request that recognizes animals in an image.
### Optical flow and rectangle detection
- [class TrackOpticalFlowRequest](trackopticalflowrequest.md)
  A request that determines the direction change of vectors for each pixel from a previous to current image.
- [struct DetectRectanglesRequest](detectrectanglesrequest.md)
  An image-analysis request that finds projected rectangular regions in an image.
### Image alignment
- [class TrackTranslationalImageRegistrationRequest](tracktranslationalimageregistrationrequest.md)
  An image-analysis request that you track over time to determine the affine transform necessary to align the content of two images.
- [class TrackHomographicImageRegistrationRequest](trackhomographicimageregistrationrequest.md)
  An image-analysis request that you track over time to determine the perspective warp matrix necessary to align the content of two images.
- [protocol TargetedRequest](targetedrequest.md)
  A type for analyzing two images together.
### Image feature print and background removal
- [struct GenerateImageFeaturePrintRequest](generateimagefeatureprintrequest.md)
  An image-based request to generate feature prints from an image.
- [struct GenerateForegroundInstanceMaskRequest](generateforegroundinstancemaskrequest.md)
  A request that generates an instance mask of noticeable objects to separate from the background.
### Machine learning image analysis
- [struct CoreMLRequest](coremlrequest.md)
  An image-analysis request that uses a Core ML model to process images.
- [struct CoreMLFeatureValueObservation](coremlfeaturevalueobservation.md)
  An object that represents a collection of key-value information that a Core ML image-analysis request produces.
- [struct ClassificationObservation](classificationobservation.md)
  An object that represents classification information that an image-analysis request produces.
- [struct PixelBufferObservation](pixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.
### Coordinate conversion
- [struct NormalizedPoint](normalizedpoint.md)
  A point in a 2D coordinate system.
- [struct NormalizedRect](normalizedrect.md)
  The location and dimensions of a rectangle.
- [struct NormalizedCircle](normalizedcircle.md)
  The center point and radius of a 2D circle.
- [enum CoordinateOrigin](coordinateorigin.md)
  The origin of a coordinate system relative to an image.
### Request Handlers
- [class ImageRequestHandler](imagerequesthandler.md)
  An object that processes one or more image-analysis requests pertaining to a single image.
- [class TargetedImageRequestHandler](targetedimagerequesthandler.md)
  An object that performs image-analysis requests on two images.
### Utilities
- [enum ComputeStage](computestage.md)
  Types that represent the compute stage.
- [class VideoProcessor](videoprocessor.md)
  An object that performs offline analysis of video content.
### Errors
- [enum VisionError](visionerror.md)
  The errors that the framework produces.
### Legacy API
- [Original Objective-C and Swift API](original-objective-c-and-swift-api.md)
### Structures
- [struct ImageCoordinateConversionHelpers](imagecoordinateconversionhelpers.md)
- [struct ImagePixelDimensions](imagepixeldimensions.md)
- [struct ResourceVersion](resourceversion.md)
- [struct VNVideoProcessingOption](vnvideoprocessingoption.md)
  Options to pass to the video processor when adding requests.
### Type Aliases
- [typealias DetectorKey](detectorkey.md)
- [typealias NamedMultipleObjectDataAccessBlock](namedmultipleobjectdataaccessblock.md)
- [typealias NamedObjectDataAccessBlock](namedobjectdataaccessblock.md)
- [typealias NamedObjectsDictionary](namedobjectsdictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Vision)*