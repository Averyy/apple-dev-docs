# Flags

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit integer containing flags that identify some timecode characteristics.

#### Overview

The following flags are defined:

- **Drop frame**: Indicates whether the timecode is drop frame. Set it to `1` if the timecode is drop frame. This flag’s value is `0x0001`.
- **24 hour max**: Indicates whether the timecode wraps after 24 hours. Set it to `1` if the timecode wraps. This flag’s value is `0x0002`.
- **Negative times OK**: Indicates whether negative time values are allowed. Set it to `1` if the timecode supports negative values. This flag’s value is `0x0004`.
- **Counter**: Indicates whether the time value corresponds to a tape counter value. Set it to `1` if the timecode values are tape counter values. This flag’s value is `0x0008`.

## See Also

- [Reserved](timecode_sample_description/reserved.md)
  A 32-bit integer that is reserved for future use.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/timecode_sample_description/flags)*