# Preload duration

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit integer specifying the duration, in the movie’s time coordinate system, of a segment of the track that is to be preloaded.

#### Overview

If the duration is set to –1, it means that the preload segment extends from the preload start time to the end of the track. All media data in the segment of the track defined by the preload start time and preload duration values should be loaded into memory when the movie is to be played.

## See Also

- [Size](track_load_settings_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this track load settings atom.
- [Type](track_load_settings_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Preload start time](track_load_settings_atom/preload_start_time.md)
  A 32-bit integer specifying the starting time, in the movie’s time coordinate system, of a segment of the track that is to be preloaded.
- [Preload flags](track_load_settings_atom/preload_flags.md)
  A 32-bit integer containing flags governing the preload operation.
- [Default hints](track_load_settings_atom/default_hints.md)
  A 32-bit integer containing playback hints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_load_settings_atom/preload_duration)*