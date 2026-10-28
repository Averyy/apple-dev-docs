# splitPoints(forFrameStart:duration:serviceCount:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Determines the source media segments based on the number of available encoder services.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func splitPoints(forFrameStart start: Int64, duration numFrames: Int64, serviceCount: Int32) -> [Any]!
```

```objc
- (NSArray *) splitPointsForFrameStart:(int64_t) start duration:(int64_t) numFrames serviceCount:(int32_t) serviceCount;
```

## Return Value

An array of frame numbers indicating the start of each segment.

## Discussion

In a distributed process environment, the Compressor app assigns source media segments to the available encoder instances to process them concurrently. If your extension supports segmenting, the Compressor app calls this method to determine segments of the source media. Segmenting the source media is beneficial for distributed encoding, and for local encoding if you enable additional Compressor app instances.

> **Note**:  When determining source media segments, specify multiple segments for video data and a single segment for complete audio data.

## Parameters

- `start`: The frame at which to start segmenting.
- `numFrames`: The number of frames in the source media.
- `serviceCount`: The number of encoder services available to process the source media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionencoder/splitpoints(forframestart:duration:servicecount:))*