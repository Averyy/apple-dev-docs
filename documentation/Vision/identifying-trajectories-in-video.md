# Identifying Trajectories in Video

**Framework**: Vision

Gain new insights into your video data by using Vision to detect trajectories.

#### Overview

Starting in iOS 14, tvOS 14, and macOS 11, Vision provides the ability to detect the trajectories of objects in a video sequence. It detects multiple, simultaneous trajectories in a scene, following the path of objects, including those that are only a few pixels in size. This feature has wide-ranging uses, but can be of particular use in sports and fitness apps, where you commonly want to follow the trajectories of balls, pucks, and so on.

![An image showing the trajectory of a soccer ball being kicked by a player.](https://docs-assets.developer.apple.com/published/ae9522150ec7075ac9d05b9cb60f10bd/media-3618313%402x.png)

Vision’s trajectory-detection algorithm requires a stable scene, meaning the camera is mounted on a tripod, and the camera and background remain stationary. The algorithm looks at the frame differentials in the video to detect any objects traveling along a parabolic path. Any camera movement introduces noise and motion blur, which reduces the accuracy of the detection.

A single object may produce multiple trajectories. For example, a bouncing ball forms a new trajectory with each bounce. Similarly, if a trajectory goes offscreen and comes back at a later time, Vision creates a new trajectory for the object.

##### Perform a Request to Detect Trajectories

To detect trajectories in video, use an instance of [`VNDetectTrajectoriesRequest`](vndetecttrajectoriesrequest.md). This is a new  request type that you use to build evidence over time. Most Vision requests are stateless, and because they require limited resources to create, you typically make new instances as needed. Because a request to detect trajectories maintains state, you instead create a single instance of it and perform the request multiple times.

When you create a [`VNDetectTrajectoriesRequest`](vndetecttrajectoriesrequest.md), you pass it the following arguments:

- A frame analysis spacing, which lets you control the rate at which the request performs its analysis. You provide a [`CMTime`](https://developer.apple.com/documentation/CoreMedia/CMTime) value that defines a millisecond interval value to wait between analysis runs. Setting this argument to [`zero`](https://developer.apple.com/documentation/CoreMedia/CMTime/zero) processes all frames (if the device can keep up). Increasing the value reduces processor consumption, but may produce less accurate results.
- A trajectory length, which indicates the number of points you require to recognize a parabola. The minimum number is 5, but you can increase it to fit your needs. The value you set changes the number of points given in each observation. If you know you’re looking for a long throw, you could increase the length to filter out small, spurious movements.
- A completion handler to process the results.

The following example shows how to create and perform a request in an app thatʼs capturing live video from the camera. Note that [`VNDetectTrajectoriesRequest`](vndetecttrajectoriesrequest.md) requires using [`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer) objects that contain timestamps so it can correctly calculate the trajectory observationʼs time range.

```swift
// Lazily create a single instance of VNDetectTrajectoriesRequest.
private lazy var request: VNDetectTrajectoriesRequest = {
    return VNDetectTrajectoriesRequest(frameAnalysisSpacing: .zero,
                                       trajectoryLength: 15,
                                       completionHandler: completionHandler)
}()

// AVCaptureVideoDataOutputSampleBufferDelegate callback.
func captureOutput(_ output: AVCaptureOutput,
                   didOutput sampleBuffer: CMSampleBuffer,
                   from connection: AVCaptureConnection) {
    do {
        let requestHandler = VNImageRequestHandler(cmSampleBuffer: sampleBuffer)
        try requestHandler.perform([request])
    } catch {
        // Handle the error.
    }
}

func completionHandler(request: VNRequest, error: Error?) {
    // Process the results.
}

```

You can improve the performance and accuracy of the request by applying filtering criteria to it. If you know the approximate size of the objects you want to follow, you can set a minimum and maximum object size. You specify an object’s size as its normalized pixel diameters. Set the minimum size to filter out small, spurious movements like a bird flying through the scene. Likewise, set the maximum size to filter out larger objects. Like with all Vision requests, you can also set a region of interest (ROI) if you want to detect only those trajectories occurring in a particular region of the frame.

```swift
// Set the normalized (0.0 to 1.0) minimum and maximum object sizes.
request.minimumObjectSize = smallDiameter / videoWidth
request.maximumObjectSize = largeDiameter / videoWidth

// Set the ROI to the left half of the image.
request.regionOfInterest = CGRect(x: 0, y: 0, width: 0.5, height: 1.0)
```

> 💡 **Tip**:  The minimum and maximum object sizes aren’t pixel accurate, but instead provide general guidelines to the algorithm. Setting a size that’s slightly smaller than your target [`minimumObjectSize`](vndetecttrajectoriesrequest/minimumobjectsize.md), and slightly larger than your [`maximumObjectSize`](vndetecttrajectoriesrequest/maximumobjectsize.md) may produce better results.

##### Process the Results

After the handler performs the request, it calls the request’s completion closure, passing it the request and any errors that occurred. Retrieve the observations by querying the request object for its results, which it returns as an array of [`VNTrajectoryObservation`](vntrajectoryobservation.md) objects.

```swift
func requestHandler(request: VNRequest, error: Error?) {
    guard let observations =
            request.results as? [VNTrajectoryObservation] else { return }
    
    // Process the observations.
    
}
```

Because the request builds evidence over time before it produces trajectory observations, the handler is called, but with no observations until the result has at least one trajectory with a high confidence score and a trajectory length matching the requested length.

![An illustration showing that a request must build evidence over time before it produces trajectory observations.](https://docs-assets.developer.apple.com/published/6e36239fa3aa111b86502cf27d63be08/media-3625760%402x.png)

The key pieces of data that a [`VNTrajectoryObservation`](vntrajectoryobservation.md) provides are the  and  points the object travels on the parabolic path. The detected points follow the centroids of the object in motion, which may not follow the parabolic path exactly, whereas the projected points represent the path precisely. You can retrieve the equation coefficients for the quadratic equation, f(x) = ax2 + bx + c, from the observation, which it provides as a [`simd_float3`](https://developer.apple.com/documentation/simd/simd_float3) value.

Each trajectory provides a [`uuid`](https://developer.apple.com/documentation/Foundation/UUID/uuid) value that you can use to track it over time, which is useful when performing ongoing calculations on the data or drawing visualizations of it. For an example of how you can visualize trajectory data, see the [`Building a feature-rich app for sports analysis`](building-a-feature-rich-app-for-sports-analysis.md) sample app.

##### Apply Your Business Logic

Vision gives you the tools to detect trajectories and retrieve the relevant data about them. How you use the data is unique to your app, and requires you to apply your own business logic. Some key things to keep in mind as you develop that logic:

- Filter out trajectories whose confidence scores don’t meet your criteria.
- Filter out irrelevant directional movement. If you only care about objects traveling in a certain direction, evaluate the direction of the path and eliminate irrelevant trajectories.
- Know where to look. If you know the specific region of the image you want to analyze, set the request’s region of interest. Doing so also reduces noise and enhances performance.
- Know the size of what you’re looking for. Whenever possible, set a minimum and maximum object size. Doing so also reduces noise and enhances performance.
- Pick a camera resolution that’s appropriate for the size of object you want to track. For small objects, like a tennis or cricket ball, you may need 1080p resolution to achieve the results you want. Tracking larger objects, like a soccer ball, may require only VGA resolution for optimal results. Vision downscales the movie as needed, based on the minimum object size, to improve performance.

## See Also

- [Detecting moving objects in a video](detecting-moving-objects-in-a-video.md)
  Identify the trajectory of a thrown object by using Vision.
- [class VNDetectTrajectoriesRequest](vndetecttrajectoriesrequest.md)
  A request that detects the trajectories of shapes moving along a parabolic path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/identifying-trajectories-in-video)*