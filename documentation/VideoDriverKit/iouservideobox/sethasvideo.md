# SetHasVideo

**Framework**: VideoDriverKit  
**Kind**: method

Sets the value indicating the box’s video support.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t SetHasVideo(bool in_has_video);
```

#### Discussion

The object sends a notification to the host to update the object state on success. The object’s work queue synchronizes access to the value.

## See Also

- [SetHasAudio](iouservideobox/sethasaudio.md)
  Sets the value indicating the box’s audio support.
- [HasAudio](iouservideobox/hasaudio.md)
  A Boolean value indicating if box has audio capabilities.
- [HasVideo](iouservideobox/hasvideo.md)
  A Boolean value indicating if box has video capabilities.
- [SetHasMIDI](iouservideobox/sethasmidi.md)
  Sets the value indicating the box’s MIDI support
- [HasMIDI](iouservideobox/hasmidi.md)
  A Boolean value indicating if box has MIDI capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/sethasvideo)*