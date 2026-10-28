# projectAspectRatio(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the aspect ratio of the host’s project.

**Availability**:
- FxPlug 4.2.9+

## Declaration

```swift
func projectAspectRatio(_ aspectRatio: UnsafeMutablePointer<Float>!) throws
```

```objc
- (BOOL) projectAspectRatio:(float *) aspectRatio error:(NSError * *) error;
```

## Discussion

Use this method to get the aspect ratio of the current project. The clip that the user applies your plug-in to may not be the same aspect ratio as the project or sequence it’s a part of.

> **Note**:  This method returns the document space aspect ratio, meaning the aspect ratio the project is displayed at after any non-square pixels or fields are accounted for. For example, a NTSC standard definition DV project that’s `720 x 480` with `10:11` pixel aspect ratio returns `(720 * 10/11) / 480 = ~1.36363636...` as the aspect ratio, not `1.5`.

## Parameters

- `aspectRatio`: A float value representing the project aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxprojectapi_v2/projectaspectratio(_:))*