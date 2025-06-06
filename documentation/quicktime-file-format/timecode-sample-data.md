# Timecode sample data

**Framework**: QuickTime File Format  
**Kind**: class

An atom that represents timecode sample data.

#### Overview

A timecode media sample is recorded as a 32-bit integer, interpreted based on the value of the Counter flag in the timecode sample description.

If the Counter flag is set to `1` in the timecode sample description, the sample data is an unsigned 32-bit integer. The timecode counter value is determined by dividing this unsigned 32-bit integer by the number of frames field in the timecode sample description.

If the Counter flag is set to `0` in the timecode sample description, the sample data format is a signed 32-bit integer and is used to calculate a timecode record.

## Topics

### Data fields
- [Hours](timecode_sample_data/hours.md)
  An 8-bit unsigned integer that indicates the starting number of hours.
- [Negative](timecode_sample_data/negative.md)
  A 1-bit value indicating the time’s sign.
- [Minutes](timecode_sample_data/minutes.md)
  A 7-bit integer that contains the starting number of minutes.
- [Seconds](timecode_sample_data/seconds.md)
  An 8-bit unsigned integer indicating the starting number of seconds.
- [Frames](timecode_sample_data/frames.md)
  An 8-bit unsigned integer that specifies the starting number of frames.

## See Also

- [Timecode sample description](timecode_sample_description.md)
  An atom that defines how to interpret time code media data.
- [Timecode media information atom ('tcmi')](timecode_media_information_atom.md)
  An atom that governs how the timecode text is displayed.
- [Creating a timecode track for 29.97 FPS video](creating_a_timecode_track_for_2997_fps_video.md)
  Configure a timecode track to specify timecode information for other tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/timecode_sample_data)*