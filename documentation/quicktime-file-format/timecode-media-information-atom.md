# Timecode media information atom ('tcmi')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that governs how the timecode text is displayed.

## Mentions

- [QuickTime File Format change log](revision_history.md)

#### Overview

The timecode media also requires a media information atom. This atom contains information governing how the timecode text is displayed. This media information atom is stored in a base media information atom (see [`Base media information atom ('minf')`](base_media_information_atom.md) for more information). The type of the timecode media information atom is `'tcmi'`.

## Topics

### Data fields
- [Size](timecode_media_information_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this time code media information atom.
- [Type](timecode_media_information_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](timecode_media_information_atom/version.md)
  A 1-byte specification of the version of this timecode media information atom.
- [Flags](timecode_media_information_atom/flags.md)
  A 3-byte space for timecode media information flags.
- [Text font](timecode_media_information_atom/text_font.md)
  A 16-bit integer that indicates the font to use.
- [Text face](timecode_media_information_atom/text_face.md)
  A 16-bit integer that indicates the font’s style.
- [Text size](timecode_media_information_atom/text_size.md)
  A 16-bit integer that specifies the point size of the time code text.
- [Reserved](timecode_media_information_atom/reserved.md)
  A 16-bit integer that is reserved for use by Apple.
- [Text color](timecode_media_information_atom/text_color.md)
  A 48-bit RGB color value for the timecode text.
- [Background color](timecode_media_information_atom/background_color.md)
  A 48-bit RGB background color for the timecode text.
- [Font name](timecode_media_information_atom/font_name.md)
  A Pascal string specifying the name of the timecode text’s font.

## See Also

- [Timecode sample description](timecode_sample_description.md)
  An atom that defines how to interpret time code media data.
- [Timecode sample data](timecode_sample_data.md)
  An atom that represents timecode sample data.
- [Creating a timecode track for 29.97 FPS video](creating_a_timecode_track_for_2997_fps_video.md)
  Configure a timecode track to specify timecode information for other tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/timecode_media_information_atom)*