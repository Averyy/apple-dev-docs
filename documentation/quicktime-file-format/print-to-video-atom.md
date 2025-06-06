# Print to video atom ('ptv ')

**Framework**: QuickTime File Format  
**Kind**: class

An atom you use to play the movie in full-screen mode, with no window and no visible controller.

#### Overview

A movie atom’s user data atom may contain a print to video atom (`'ptv '`). Note that the fourth character is an ASCII blank (`0x20`). If a print to video atom is present, QuickTime plays the movie in full-screen mode, with no window and no visible controller. Any portion of the screen not occupied by the movie is cleared to black. The user must press the Esc (Escape) key to exit full-screen mode.

This atom is often added and removed transiently to control the display mode of a movie for a single presentation, but it can also be stored as part of the permanent movie file.

## Topics

### Data fields
- [Display size](print_to_video_atom/display_size.md)
  A 16-bit little-endian integer indicating the display size for the movie.
- [Reserved](print_to_video_atom/reserved1.md)
  A 16-bit integer.
- [Reserved](print_to_video_atom/reserved2.md)
  A 16-bit integer.
- [Play on open](print_to_video_atom/play_on_open.md)
  An 8-bit Boolean value that indicates whether the movie plays when opened.

## See Also

- [User data atom ('udta')](user_data_atom.md)
  An atom where you define and store data associated with a QuickTime object.
- [Track name atom ('tnam')](track_name_atom.md)
  An atom that provides a name for a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/print_to_video_atom)*