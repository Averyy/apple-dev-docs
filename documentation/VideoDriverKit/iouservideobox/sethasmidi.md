# SetHasMIDI

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetHasMIDI(bool in_has_midi);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the value indicating the box’s midi support

A notification will be sent to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## See Also

- [SetHasAudio](iouservideobox/sethasaudio.md)
- [HasAudio](iouservideobox/hasaudio.md)
- [SetHasVideo](iouservideobox/sethasvideo.md)
- [HasVideo](iouservideobox/hasvideo.md)
- [HasMIDI](iouservideobox/hasmidi.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/sethasmidi)*