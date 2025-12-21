# UIVideoAtPathIsCompatibleWithSavedPhotosAlbum(_:)

**Framework**: UIKit  
**Kind**: func

Returns a Boolean value that indicates whether the specified video is compatible to save to the user’s Camera Roll album.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func UIVideoAtPathIsCompatibleWithSavedPhotosAlbum(_ videoPath: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the video can be saved to the Camera Roll album or [`false`](https://developer.apple.com/documentation/Swift/false) if it cannot.

#### Discussion

Not all devices are able to play video files placed in the user’s Camera Roll album. Before attempting to save a video, call this function and check its return value to ensure that saving the video is supported for the current device. For a code example, refer to [`Camera Programming Topics for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/CameraAndPhotoLib_TopicsForIOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010400).

When used on an iOS device without a camera, this method indicates whether the specified movie can be saved to the Saved Photos album rather than to the Camera Roll album.

## Parameters

- `videoPath`: The filesystem path to the movie file you want to save.

## See Also

- [func UIImageWriteToSavedPhotosAlbum(UIImage, Any?, Selector?, UnsafeMutableRawPointer?)](uiimagewritetosavedphotosalbum(_:_:_:_:).md)
  Adds the specified image to the user’s Camera Roll album.
- [func UISaveVideoAtPathToSavedPhotosAlbum(String, Any?, Selector?, UnsafeMutableRawPointer?)](uisavevideoatpathtosavedphotosalbum(_:_:_:_:).md)
  Adds the movie from the specified path to the user’s Camera Roll album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivideoatpathiscompatiblewithsavedphotosalbum(_:))*