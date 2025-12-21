# Generating high-quality thumbnails from videos

**Framework**: Vision

Identify the most visually pleasing frames in a video by using the image-aesthetics scores request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 2.0+
- Xcode 16.0+

#### Overview

Using the [`Vision`](Vision.md) framework, you can process images and videos frame by frame, enabling image-analysis requests through [`VisionRequest`](VisionRequest.md). The sample demonstrates how to process video input to identify the three frames with the highest aesthetic scores. By leveraging this capability, you can automatically select the best frames for creating promotional materials or for highlighting short films. The following image shows a preview of the sample:

![A screen recording of a macOS app that demonstrates selecting a video file to generate the best thumbnails.](https://docs-assets.developer.apple.com/published/864613acf2af54ee865a04b0174615ea/sample-thumbnail-generator-1-main-view.png)

The sample uses a [`VideoProcessor`](VideoProcessor.md) to convert the video into a stream of frames, which [`CalculateImageAestheticsScoresRequest`](CalculateImageAestheticsScoresRequest.md) analyzes to rate each frame with an overall aesthetic score. To avoid selecting similar thumbnails, the [`GenerateImageFeaturePrintRequest`](GenerateImageFeaturePrintRequest.md) compares the image similarity. Finally, [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation) extracts the images from the selected frames and presents them as thumbnails.

##### Set Up the Representation of Frames and Thumbnails

The `Frame` structure contains the information about a specific frame in the video that the sample uses to determine the best frame to use as a thumbnail. It accepts a `CMTime` to represent the timestamp of the frame, a `Float` value for the overall score of the frame, and a [`FeaturePrintObservation`](FeaturePrintObservation.md) to enable comparison to other frames:

```swift
struct Frame {
    /// The timestamp of the frame.
    let time: CMTime

    /// The score of the frame.
    let score: Float

    /// The feature-print observation of the frame.
    let observation: FeaturePrintObservation
}
```

To present the results of each frame, the sample creates a `Thumbnail` class that conforms to the [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable) protocal. This ensures that the class has a unique identity for [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach) to display the results. This class accepts a `CGImage` to store the image of the frame, and a `Frame` to establish a connection between the frame and the thumbnail:

```swift
class Thumbnail: Identifiable {
    /// The image that captures from the video frame.
    let image: CGImage

    /// The frame that the thumbnail represents.
    let frame: Frame

    // ...
}
```

##### Process the Video

The sample processes videos frame by frame using the [`VideoProcessor`](VideoProcessor.md). The sample first initializes the video processor with the video URL, then create the instances of the requests the sample uses to process the video:

```swift
func processVideo(for videoURL: URL, progression: Binding<Float>) async -> [Thumbnail] {
    /// The instance of the `VideoProcessor` with the local path to the video file.
    let videoProcessor = VideoProcessor(videoURL)

    /// The request to calculate the aesthetics score for each frame.
    let aestheticsScoresRequest = CalculateImageAestheticsScoresRequest()

    /// The request to generate feature prints from an image.
    let imageFeaturePrintRequest = GenerateImageFeaturePrintRequest()

    /// The array to store information for the frames with the highest scores.
    var topFrames: [Frame] = []

    // ...
}
```

The [`CalculateImageAestheticsScoresRequest`](CalculateImageAestheticsScoresRequest.md) calculates the aesthetic scores for each frame. To ensure that the thumbnail results represent different scenes rather than variations of the same frame, [`GenerateImageFeaturePrintRequest`](GenerateImageFeaturePrintRequest.md) computes the similarity between the frames.

The sample calculates a time interval for the video processor to process approximately 100 frames, adds the `aestheticsScoresRequest` and `imageFeaturePrintRequest` to the video processor, then starts the video-analysis process. To store the timestamp and the results from the video-processor stream, the sample creates two dictionaries: `aestheticsResults` and `featurePrintResults`:

```swift
do {
    /// The time interval for the video-processing cadence.
    let interval = CMTime(
        seconds: totalDuration / framesToEval,
        preferredTimescale: timeScale
    )

    /// The video-processing cadence to process only 100 frames.
    let cadence = VideoProcessor.Cadence.timeInterval(interval)

    /// The stream that adds the aesthetics scores request to the video processor.
    let aestheticsScoreStream = try await videoProcessor.addRequest(aestheticsScoresRequest, cadence: cadence)

    /// The stream that adds the image feature-print request to the video processor.
    let featurePrintStream = try await videoProcessor.addRequest(imageFeaturePrintRequest, cadence: cadence)
    
    // Start to analyze the video.
    videoProcessor.startAnalysis()

    /// The dictionary to store the timestamp and the aesthetics score.
    var aestheticsResults: [CMTime: Float] = [:]

    /// The dictionary to store the timestamp and the feature-print observation.
    var featurePrintResults: [CMTime: FeaturePrintObservation] = [:]

    // ...

    // Solve for the top-rated frames.
    topFrames = await calculateTopFrames(aestheticsResults: aestheticsResults, featurePrintResults: featurePrintResults)
} 
```

When the sample receives the results for both requests, call `calculateTopFrames(aestheticsResults:featurePrintResults:)` to solve for the top-rated frames.

##### Solve for the Top Rated Frames

The function uses `aestheticsResults` and `featurePrintResults` to identify three frames that have the highest aesthetic scores and are different from each other:

```swift
for (time, score) in aestheticsResults {
    /// The `FeaturePrintObservation` for the timestamp.
    guard let featurePrint = featurePrintResults[time] else { continue }

    /// The new frame at that timestamp.
    let newFrame = Frame(time: time, score: score, observation: featurePrint)

    /// The variable that tracks whether to add the image based on image similarity.
    var isSimilar = false

    // Iterate through the current top-rated frames to check whether any of them
    // are similar to the new frame and find the insertion index.
    for (index, frame) in topFrames.enumerated() {
        if let distance = try? featurePrint.distance(to: frame.observation), distance < similarityThreshold {
            // Replace the frame if the new frame has a higher score.
            if newFrame.score > frame.score {
                topFrames[index] = newFrame
            }
            isSimilar = true
            break
        }

        // ...
    }
}
```

For each result, the sample creates a new frame based on the timestamp and attaches the score and `FeaturePrintObservation`. It checks for similar frames in `topFrames` with the `distance(to:)` function to compare the observations. If there is a match, the sample keeps the frame with the higher score and exits the loop.

## See Also

- [struct CalculateImageAestheticsScoresRequest](calculateimageaestheticsscoresrequest.md)
  A request that analyzes an image for aesthetically pleasing attributes.
- [struct DetectLensSmudgeRequest](detectlenssmudgerequest.md)
  A request that detects a smudge on a lens from an image or video frame capture.
- [struct GenerateAttentionBasedSaliencyImageRequest](generateattentionbasedsaliencyimagerequest.md)
  An object that produces a heat map that identifies the parts of an image most likely to draw attention.
- [struct GenerateObjectnessBasedSaliencyImageRequest](generateobjectnessbasedsaliencyimagerequest.md)
  A request that generates a heat map that identifies the parts of an image most likely to represent objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generating-thumbnails-from-videos)*