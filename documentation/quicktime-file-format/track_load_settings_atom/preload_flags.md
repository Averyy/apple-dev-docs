# Preload flags

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 32-bit integer containing flags governing the preload operation.

#### Overview

Only two flags are defined, and they are mutually exclusive. If this flag is set to `1`, the track is to be preloaded regardless of whether it is enabled. If this flag is set to `2`, the track is to be preloaded only if it is enabled.

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer that specifies the number of bytes in this track load settings atom.
- [Type](./type.md)
  A 32-bit integer that identifies the atom type.
- [Preload start time](./preload_start_time.md)
  A 32-bit integer specifying the starting time, in the movie’s time coordinate system, of a segment of the track that is to be preloaded.
- [Preload duration](./preload_duration.md)
  A 32-bit integer specifying the duration, in the movie’s time coordinate system, of a segment of the track that is to be preloaded.
- [Default hints](./default_hints.md)
  A 32-bit integer containing playback hints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_load_settings_atom/preload_flags)*