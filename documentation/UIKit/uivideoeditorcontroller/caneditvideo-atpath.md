# canEditVideo(atPath:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value indicating whether a video file can be edited.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func canEditVideo(atPath videoPath: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the specified video file can be edited on the current device or [`false`](https://developer.apple.com/documentation/Swift/false) if it cannot.

#### Discussion

Video editing requires the presence of specific hardware and is available only for specific file formats. Use this method to check whether video editing is available for a given video file, before you create a video editor.

## Parameters

- `videoPath`: The filesystem path to the video file you want to edit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivideoeditorcontroller/caneditvideo(atpath:))*