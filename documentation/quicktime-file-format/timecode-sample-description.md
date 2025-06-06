# Timecode sample description

**Framework**: QuickTime File Format  
**Kind**: class

An atom that defines how to interpret time code media data.

#### Overview

The timecode sample description contains information that defines how to interpret time code media data. This sample description is based on the standard sample description header, as described in [`Sample description atom ('stsd')`](sample_description_atom.md).

The data format field in the sample description is always set to `'tmcd'`.

The timecode media handler also adds some of its own fields to the sample description.

## Topics

### Data fields
- [Reserved](timecode_sample_description/reserved.md)
  A 32-bit integer that is reserved for future use.
- [Flags](timecode_sample_description/flags.md)
  A 32-bit integer containing flags that identify some timecode characteristics.
- [Time scale](timecode_sample_description/time_scale.md)
  A 32-bit integer that specifies the time scale for interpreting the frame duration field.
- [Frame duration](timecode_sample_description/frame_duration.md)
  A 32-bit integer that indicates how long each frame lasts in real time.
- [Number of frames](timecode_sample_description/number_of_frames.md)
  An 8-bit integer that contains the number of frames per second for the timecode format.
- [Reserved](timecode_sample_description/reserved2.md)
  An 8-bit quantity.
- [Source reference](timecode_sample_description/source_reference.md)
  A user data atom containing information about the source tape.

## See Also

- [Timecode media information atom ('tcmi')](timecode_media_information_atom.md)
  An atom that governs how the timecode text is displayed.
- [Timecode sample data](timecode_sample_data.md)
  An atom that represents timecode sample data.
- [Creating a timecode track for 29.97 FPS video](creating_a_timecode_track_for_2997_fps_video.md)
  Configure a timecode track to specify timecode information for other tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/timecode_sample_description)*