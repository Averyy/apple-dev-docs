# Original Objective-C and Swift API

**Framework**: Vision

## Topics

### Essentials
- [Building a feature-rich app for sports analysis](building-a-feature-rich-app-for-sports-analysis.md)
  Detect and classify human activity in real time using computer vision and machine learning.
### Still-image analysis
- [Detecting Objects in Still Images](detecting-objects-in-still-images.md)
  Locate and demarcate rectangles, faces, barcodes, and text in images using the Vision framework.
- [Classifying images for categorization and search](classifying-images-for-categorization-and-search.md)
  Analyze and label images using a Vision classification request.
- [Analyzing Image Similarity with Feature Print](analyzing-image-similarity-with-feature-print.md)
  Generate a feature print to compute distance between images.
- [class VNRequest](vnrequest.md)
  The abstract superclass for analysis requests.
- [class VNImageBasedRequest](vnimagebasedrequest.md)
  The abstract superclass for image-analysis requests that focus on a specific part of an image.
- [class VNClassifyImageRequest](vnclassifyimagerequest.md)
  A request to classify an image.
- [class VNGenerateImageFeaturePrintRequest](vngenerateimagefeatureprintrequest.md)
  An image-based request to generate feature prints from an image.
- [class VNFeaturePrintObservation](vnfeatureprintobservation.md)
  An observation that provides the recognized feature print.
- [class VNImageRequestHandler](vnimagerequesthandler.md)
  An object that processes one or more image-analysis request pertaining to a single image.
- [class VNObservation](vnobservation.md)
  The abstract superclass for analysis results.
### Image sequence analysis
- [Applying Matte Effects to People in Images and Video](applying-matte-effects-to-people-in-images-and-video.md)
  Generate image masks for people automatically by using semantic person-segmentation.
- [Detecting Human Actions in a Live Video Feed](../createml/detecting_human_actions_in_a_live_video_feed.md)
  Identify body movements by sending a person’s pose data from a series of video frames to an action-classification model.
- [Segmenting and colorizing individuals from a surrounding scene](segmenting-and-colorizing-individuals-from-a-surrounding-scene.md)
  Use the Vision framework to isolate and apply colors to people in an image.
- [class VNStatefulRequest](vnstatefulrequest.md)
  An abstract request type that builds evidence of a condition over time.
- [class VNGeneratePersonSegmentationRequest](vngeneratepersonsegmentationrequest.md)
  An object that produces a matte image for a person it finds in the input image.
- [class VNGeneratePersonInstanceMaskRequest](vngeneratepersoninstancemaskrequest.md)
  An object that produces a mask of individual people it finds in the input image.
- [class VNDetectDocumentSegmentationRequest](vndetectdocumentsegmentationrequest.md)
  An object that detects rectangular regions that contain text in the input image.
- [class VNSequenceRequestHandler](vnsequencerequesthandler.md)
  An object that processes image-analysis requests for each frame in a sequence.
### Image aesthetics analysis
- [class VNCalculateImageAestheticsScoresRequest](vncalculateimageaestheticsscoresrequest.md)
  An object that analyzes an image for aesthetically pleasing attributes.
### Saliency analysis
- [Cropping Images Using Saliency](cropping-images-using-saliency.md)
  Isolate regions in an image that are most likely to draw people’s attention.
- [Highlighting Areas of Interest in an Image Using Saliency](highlighting-areas-of-interest-in-an-image-using-saliency.md)
  Quantify and visualize where people are likely to look in an image.
- [class VNGenerateAttentionBasedSaliencyImageRequest](vngenerateattentionbasedsaliencyimagerequest.md)
  An object that produces a heat map that identifies the parts of an image most likely to draw attention.
- [class VNGenerateObjectnessBasedSaliencyImageRequest](vngenerateobjectnessbasedsaliencyimagerequest.md)
  A request that generates a heat map that identifies the parts of an image most likely to represent objects.
- [class VNSaliencyImageObservation](vnsaliencyimageobservation.md)
  An observation that contains a grayscale heat map of important areas across an image.
### Object tracking
- [Tracking the User’s Face in Real Time](tracking-the-user-s-face-in-real-time.md)
  Detect and track faces from the selfie cam feed in real time.
- [Tracking Multiple Objects or Rectangles in Video](tracking-multiple-objects-or-rectangles-in-video.md)
  Apply Vision algorithms to track objects or rectangles throughout a video.
- [class VNTrackingRequest](vntrackingrequest.md)
  The abstract superclass for image-analysis requests that track unique features across multiple images or video frames.
- [class VNTrackRectangleRequest](vntrackrectanglerequest.md)
  An image-analysis request that tracks movement of a previously identified rectangular object across multiple images or video frames.
- [class VNTrackObjectRequest](vntrackobjectrequest.md)
  An image-analysis request that tracks the movement of a previously identified object across multiple images or video frames.
- [class VNDetectedObjectObservation](vndetectedobjectobservation.md)
  An observation that provides the position and extent of an image feature that an image- analysis request detects.
### Rectangle detection
- [class VNDetectRectanglesRequest](vndetectrectanglesrequest.md)
  An image-analysis request that finds projected rectangular regions in an image.
### Face and body detection
- [Selecting a selfie based on capture quality](selecting-a-selfie-based-on-capture-quality.md)
  Compare face-capture quality in a set of images by using Vision.
- [class VNDetectFaceCaptureQualityRequest](vndetectfacecapturequalityrequest.md)
  A request that produces a floating-point number that represents the capture quality of a face in a photo.
- [class VNDetectFaceLandmarksRequest](vndetectfacelandmarksrequest.md)
  An image-analysis request that finds facial features like eyes and mouth in an image.
- [class VNDetectFaceRectanglesRequest](vndetectfacerectanglesrequest.md)
  A request that finds faces within an image.
- [class VNDetectHumanRectanglesRequest](vndetecthumanrectanglesrequest.md)
  A request that finds rectangular regions that contain people in an image.
- [class VNHumanObservation](vnhumanobservation.md)
  An object that represents a person that the request detects.
### Body and hand pose detection
- [Detecting Human Body Poses in Images](detecting-human-body-poses-in-images.md)
  Add the capability to detect human body poses to your app using the Vision framework.
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
### 3D body pose detection
- [Identifying 3D human body poses in images](identifying-3d-human-body-poses-in-images.md)
  Detect three-dimensional human body poses using the Vision framework.
- [Detecting human body poses in 3D with Vision](detecting-human-body-poses-in-3d-with-vision.md)
  Render skeletons of 3D body pose points in a scene overlaying the input image.
- [class VNDetectHumanBodyPose3DRequest](vndetecthumanbodypose3drequest.md)
  A request that detects points on human bodies in 3D space, relative to the camera.
- [class VNHumanBodyPose3DObservation](vnhumanbodypose3dobservation.md)
  An observation that provides the 3D body points the request recognizes.
- [class VNRecognizedPoints3DObservation](vnrecognizedpoints3dobservation.md)
  An observation that provides the 3D points for a request.
- [class VNHumanBodyRecognizedPoint3D](vnhumanbodyrecognizedpoint3d.md)
  A recognized 3D point that includes a parent joint.
- [class VNPoint3D](vnpoint3d.md)
  An object that represents a 3D point in an image.
- [class VNRecognizedPoint3D](vnrecognizedpoint3d.md)
  A 3D point that includes an identifier to the point.
- [VNHumanBodyPose3DObservation.JointName](vnhumanbodypose3dobservation/jointname.md)
  The joint names for a 3D body pose.
- [VNHumanBodyPose3DObservation.JointsGroupName](vnhumanbodypose3dobservation/jointsgroupname.md)
  The joint group names for a 3D body pose.
### Animal detection
- [class VNRecognizeAnimalsRequest](vnrecognizeanimalsrequest.md)
  A request that recognizes animals in an image.
### Animal body pose detection
- [Detecting animal body poses with Vision](detecting-animal-body-poses-with-vision.md)
  Draw the skeleton of an animal by using Vision’s capability to detect animal body poses.
- [class VNDetectAnimalBodyPoseRequest](vndetectanimalbodyposerequest.md)
  A request that detects an animal body pose.
- [class VNAnimalBodyPoseObservation](vnanimalbodyposeobservation.md)
  An observation that provides the animal body points the analysis recognizes.
### Trajectory detection
- [Identifying Trajectories in Video](identifying-trajectories-in-video.md)
  Gain new insights into your video data by using Vision to detect trajectories.
- [Detecting moving objects in a video](detecting-moving-objects-in-a-video.md)
  Identify the trajectory of a thrown object by using Vision.
- [class VNDetectTrajectoriesRequest](vndetecttrajectoriesrequest.md)
  A request that detects the trajectories of shapes moving along a parabolic path.
### Contour detection
- [class VNDetectContoursRequest](vndetectcontoursrequest.md)
  A request that detects the contours of the edges of an image.
### Optical flow
- [class VNGenerateOpticalFlowRequest](vngenerateopticalflowrequest.md)
  An object that generates directional change vectors for each pixel in the targeted image.
- [class VNTrackOpticalFlowRequest](vntrackopticalflowrequest.md)
  An object that determines the direction change of vectors for each pixel from a previous to current image.
### Barcode detection
- [class VNDetectBarcodesRequest](vndetectbarcodesrequest.md)
  A request that detects barcodes in an image.
- [enum VNBarcodeCompositeType](vnbarcodecompositetype.md)
  Composite types for barcode requests.
### Text detection
- [class VNDetectTextRectanglesRequest](vndetecttextrectanglesrequest.md)
  An image-analysis request that finds regions of visible text in an image.
- [class VNTextObservation](vntextobservation.md)
  Information about regions of text that an image-analysis request detects.
### Text recognition
- [Recognizing Text in Images](recognizing-text-in-images.md)
  Add text-recognition features to your app using the Vision framework.
- [Structuring Recognized Text on a Document](../visionkit/structuring_recognized_text_on_a_document.md)
  Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- [Extracting phone numbers from text in images](extracting-phone-numbers-from-text-in-images.md)
  Analyze and filter phone numbers from text in live capture by using Vision.
- [Locating and displaying recognized text](locating-and-displaying-recognized-text.md)
  Perform text recognition on a photo using the Vision framework’s text-recognition request.
- [class VNRecognizeTextRequest](vnrecognizetextrequest.md)
  An image-analysis request that finds and recognizes text in an image.
- [class VNRecognizedTextObservation](vnrecognizedtextobservation.md)
  A request that detects and recognizes regions of text in an image.
### Object recognition
- [Recognizing Objects in Live Capture](recognizing-objects-in-live-capture.md)
  Apply Vision algorithms to identify objects in real-time video.
- [Understanding a Dice Roll with Vision and Object Detection](../coreml/model_integration_samples/understanding_a_dice_roll_with_vision_and_object_detection.md)
  Detect dice position and values shown in a camera frame, and determine the end of a roll by leveraging a dice detection model.
- [class VNRecognizedObjectObservation](vnrecognizedobjectobservation.md)
  A detected object observation with an array of classification labels that classify the recognized object.
### Request progress tracking
- [protocol VNRequestProgressProviding](vnrequestprogressproviding.md)
  A protocol for providing progress information on long-running tasks in Vision.
- [typealias VNRequestProgressHandler](vnrequestprogresshandler.md)
  A block executed at intervals during the processing of a Vision request.
### Horizon detection
- [class VNDetectHorizonRequest](vndetecthorizonrequest.md)
  An image-analysis request that determines the horizon angle in an image.
- [class VNHorizonObservation](vnhorizonobservation.md)
  The horizon angle information that an image-analysis request detects.
### Image alignment
- [Aligning Similar Images](aligning-similar-images.md)
  Construct a composite image from images that capture the same scene.
- [class VNTargetedImageRequest](vntargetedimagerequest.md)
  The abstract superclass for image analysis requests that operate on both the processed image and a secondary image.
- [class VNImageRegistrationRequest](vnimageregistrationrequest.md)
  The abstract superclass for image-analysis requests that align images according to their content.
- [class VNTranslationalImageRegistrationRequest](vntranslationalimageregistrationrequest.md)
  An image-analysis request that determines the affine transform necessary to align the content of two images.
- [class VNTrackTranslationalImageRegistrationRequest](vntracktranslationalimageregistrationrequest.md)
  An image-analysis request, as a stateful request you track over time, that determines the affine transform necessary to align the content of two images.
- [class VNHomographicImageRegistrationRequest](vnhomographicimageregistrationrequest.md)
  An image-analysis request that determines the perspective warp matrix necessary to align the content of two images.
- [class VNTrackHomographicImageRegistrationRequest](vntrackhomographicimageregistrationrequest.md)
  An image-analysis request, as a stateful request you track over time, that determines the perspective warp matrix necessary to align the content of two images.
- [class VNImageAlignmentObservation](vnimagealignmentobservation.md)
  The abstract superclass for image-analysis results that describe the relative alignment of two images.
- [class VNImageTranslationAlignmentObservation](vnimagetranslationalignmentobservation.md)
  Affine transform information that an image-alignment request produces.
- [class VNImageHomographicAlignmentObservation](vnimagehomographicalignmentobservation.md)
  An object that represents a perspective warp transformation.
### Image background removal
- [Applying visual effects to foreground subjects](applying-visual-effects-to-foreground-subjects.md)
  Segment the foreground subjects of an image and composite them to a new background with visual effects.
- [class VNInstanceMaskObservation](vninstancemaskobservation.md)
  An observation that contains an instance mask that labels instances in the mask.
- [class VNGenerateForegroundInstanceMaskRequest](vngenerateforegroundinstancemaskrequest.md)
  A request that generates an instance mask of noticable objects to separate from the background.
- [let VNGenerateForegroundInstanceMaskRequestRevision1: Int](vngenerateforegroundinstancemaskrequestrevision1.md)
  A constant for specifying the first revision of the foreground instance mask request.
### Machine learning image analysis
- [Classifying Images with Vision and Core ML](../coreml/model_integration_samples/classifying_images_with_vision_and_core_ml.md)
  Crop and scale photos using the Vision framework and classify them with a Core ML model.
- [Training a Create ML Model to Classify Flowers](training-a-create-ml-model-to-classify-flowers.md)
  Train a flower classifier using Create ML in Swift Playgrounds, and apply the resulting model to real-time image classification using Vision.
- [class VNCoreMLRequest](vncoremlrequest.md)
  An image-analysis request that uses a Core ML model to process images.
- [class VNClassificationObservation](vnclassificationobservation.md)
  An object that represents classification information that an image-analysis request produces.
- [class VNPixelBufferObservation](vnpixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.
- [class VNCoreMLFeatureValueObservation](vncoremlfeaturevalueobservation.md)
  An object that represents a collection of key-value information that a Core ML image-analysis request produces.
### Coordinate conversion
- [func VNImagePointForNormalizedPoint(CGPoint, Int, Int) -> CGPoint](vnimagepointfornormalizedpoint(_:_:_:).md)
  Projects a point in normalized coordinates into image coordinates.
- [func VNNormalizedPointForImagePoint(CGPoint, Int, Int) -> CGPoint](vnnormalizedpointforimagepoint(_:_:_:).md)
  Projects a point from image coordinates into normalized coordinates.
- [func VNImagePointForNormalizedPointUsingRegionOfInterest(CGPoint, Int, Int, CGRect) -> CGPoint](vnimagepointfornormalizedpointusingregionofinterest(_:_:_:_:).md)
  Projects a point from a region of interest within the normalized coordinates into image coordinates.
- [func VNNormalizedPointForImagePointUsingRegionOfInterest(CGPoint, Int, Int, CGRect) -> CGPoint](vnnormalizedpointforimagepointusingregionofinterest(_:_:_:_:).md)
  Projects a point from a region of interest within the image coordinates into normalized coordinates.
- [func VNImageRectForNormalizedRect(CGRect, Int, Int) -> CGRect](vnimagerectfornormalizedrect(_:_:_:).md)
  Projects a rectangle from normalized coordinates into image coordinates.
- [func VNNormalizedRectForImageRect(CGRect, Int, Int) -> CGRect](vnnormalizedrectforimagerect(_:_:_:).md)
  Projects a rectangle from image coordinates into normalized coordinates.
- [func VNImageRectForNormalizedRectUsingRegionOfInterest(CGRect, Int, Int, CGRect) -> CGRect](vnimagerectfornormalizedrectusingregionofinterest(_:_:_:_:).md)
  Projects a rectangle from a region of interest within the normalized coordinates into image coordinates.
- [func VNNormalizedRectForImageRectUsingRegionOfInterest(CGRect, Int, Int, CGRect) -> CGRect](vnnormalizedrectforimagerectusingregionofinterest(_:_:_:_:).md)
  Projects a rectangle from a region of interest within the image coordinates space into normalized coordinates.
- [let VNNormalizedIdentityRect: CGRect](vnnormalizedidentityrect.md)
  A normalized identity rectangle with an origin of zero and unit length and width.
- [func VNNormalizedRectIsIdentityRect(CGRect) -> Bool](vnnormalizedrectisidentityrect(_:).md)
  Returns a Boolean value that indicates whether the rectangle has an origin of zero and unit length and width.
- [func VNImagePointForFaceLandmarkPoint(vector_float2, CGRect, Int, Int) -> CGPoint](vnimagepointforfacelandmarkpoint(_:_:_:_:).md)
  Returns the image coordinates of a specified face landmark point.
- [func VNNormalizedFaceBoundingBoxPointForLandmarkPoint(vector_float2, CGRect, Int, Int) -> CGPoint](vnnormalizedfaceboundingboxpointforlandmarkpoint(_:_:_:_:).md)
  Returns the coordinates of a specified face landmark point, in bounding box coordinates.
### Utilities
- [struct VNComputeStage](vncomputestage.md)
  Types that represent the compute stage.
- [class VNGeometryUtils](vngeometryutils.md)
  Utility methods to determine the geometries of various Vision types.
- [class VNVideoProcessor](vnvideoprocessor.md)
  An object that performs offline analysis of video content.
### Common data types
- [class VNCircle](vncircle.md)
  An immutable 2D circle represented by its center point and radius.
- [class VNVector](vnvector.md)
  An immutable 2D vector represented by its x-axis and y-axis projections.
### Errors
- [let VNErrorDomain: String](vnerrordomain.md)
  The domain of errors that the framework generates.
- [enum VNErrorCode](vnerrorcode.md)
  Constants that identify errors from the framework.
### Version and revision numbers
- [var VNVisionVersionNumber: Double](vnvisionversionnumber.md)
  The current version number of the Vision framework.
- [let VNDetectAnimalBodyPoseRequestRevision1: Int](vndetectanimalbodyposerequestrevision1.md)
  A value that indicates the first revision for an animal body-pose request.
- [let VNDetectHumanBodyPose3DRequestRevision1: Int](vndetecthumanbodypose3drequestrevision1.md)
  A value that indicates the first revision for a human 3D body pose request.
- [let VNTrackHomographicImageRegistrationRequestRevision1: Int](vntrackhomographicimageregistrationrequestrevision1.md)
  A value that indicates the first revision for a homographic image-registration request.
- [let VNTrackTranslationalImageRegistrationRequestRevision1: Int](vntracktranslationalimageregistrationrequestrevision1.md)
  A value that indicates the first revision for a translational image-registration request.
- [let VNTrackOpticalFlowRequestRevision1: Int](vntrackopticalflowrequestrevision1.md)
  A value that indicates the first revision for an optial-flow request.
- [let VNClassifyImageRequestRevision1: Int](vnclassifyimagerequestrevision1.md)
  A constant for specifying the first revision of the image-classification request.
- [let VNClassifyImageRequestRevision2: Int](vnclassifyimagerequestrevision2.md)
  A value that indicates the second revision for an image-classification request.
- [let VNGenerateObjectnessBasedSaliencyImageRequestRevision2: Int](vngenerateobjectnessbasedsaliencyimagerequestrevision2.md)
  A value that indicates the second revision for an image-classification request.
- [let VNGenerateAttentionBasedSaliencyImageRequestRevision2: Int](vngenerateattentionbasedsaliencyimagerequestrevision2.md)
  A value that indicates the second revision for an attention-saliency image request.
- [let VNGenerateImageFeaturePrintRequestRevision1: Int](vngenerateimagefeatureprintrequestrevision1.md)
  A constant for specifying the first revision of the feature-print request.
- [let VNGenerateImageFeaturePrintRequestRevision2: Int](vngenerateimagefeatureprintrequestrevision2.md)
  A value that indicates the second revision for a feature-print request.
- [let VNDetectFaceCaptureQualityRequestRevision3: Int](vndetectfacecapturequalityrequestrevision3.md)
  A value that indicates the third revision for a face capture-quality request.
- [let VNDetectBarcodesRequestRevision4: Int](vndetectbarcodesrequestrevision4.md)
  A value that indicates the fourth revision for a barcode request.
- [let VNCalculateImageAestheticsScoresRequestRevision1: Int](vncalculateimageaestheticsscoresrequestrevision1.md)
  A value that indicates the first revision for an aesthetics scores request.
- [let VNRequestRevisionUnspecified: Int](vnrequestrevisionunspecified.md)
  A constant for specifying an unspecified request revision.
### Macros
- [Macros](vision-macros.md)
### Structures
- [struct ImageCoordinateConversionHelpers](imagecoordinateconversionhelpers.md)
- [struct ImagePixelDimensions](imagepixeldimensions.md)
- [struct ResourceVersion](resourceversion.md)
- [struct VNVideoProcessingOption](vnvideoprocessingoption.md)
  Options to pass to the video processor when adding requests.
### Type aliases
- [typealias DetectorKey](detectorkey.md)
- [typealias NamedMultipleObjectDataAccessBlock](namedmultipleobjectdataaccessblock.md)
- [typealias NamedObjectDataAccessBlock](namedobjectdataaccessblock.md)
- [typealias NamedObjectsDictionary](namedobjectsdictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/original-objective-c-and-swift-api)*