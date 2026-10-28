# SetHasMIDI

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the value indicating the box’s MIDI support

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetHasMIDI(bool in_has_midi);
```

## Discussion

The object sends a notification to the host to update the object state on success. The object’s work queue synchronizes access to the value.

## Parameters

- `in_has_midi`: The box’s MIDI support.

## See Also

### Determining media support
- [SetHasAudio](./sethasaudio.md)
  Sets the value indicating the box’s audio support.
- [HasAudio](./hasaudio.md)
  A Boolean value indicating if box has audio capabilities.
- [SetHasVideo](./sethasvideo.md)
  Sets the value indicating the box’s video support.
- [HasVideo](./hasvideo.md)
  A Boolean value indicating if box has video capabilities.
- [HasMIDI](./hasmidi.md)
  A Boolean value indicating if box has MIDI capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox/sethasmidi)*