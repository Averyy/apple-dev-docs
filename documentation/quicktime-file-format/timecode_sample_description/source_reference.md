# Source reference

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A user data atom containing information about the source tape.

#### Overview

The only currently used user data list entry is the `'name'` type. This entry contains a text item specifying the name of the source tape.

## See Also

### Data fields
- [Reserved](./reserved.md)
  A 32-bit integer that is reserved for future use.
- [Flags](./flags.md)
  A 32-bit integer containing flags that identify some timecode characteristics.
- [Time scale](./time_scale.md)
  A 32-bit integer that specifies the time scale for interpreting the frame duration field.
- [Frame duration](./frame_duration.md)
  A 32-bit integer that indicates how long each frame lasts in real time.
- [Number of frames](./number_of_frames.md)
  An 8-bit integer that contains the number of frames per second for the timecode format.
- [Reserved](./reserved2.md)
  An 8-bit quantity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/timecode_sample_description/source_reference)*