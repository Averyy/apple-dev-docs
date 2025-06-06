# Alternate group

**Framework**: QuickTime File Format  
**Kind**: property

A 16-bit integer that identifies a collection of movie tracks that contain alternate data for one another.

## Mentions

- [QuickTime File Format change log](revision_history.md)

#### Overview

This same identifier appears in each `'tkhd'` atom of the other tracks in the group. QuickTime chooses one track from the group to be used when the movie is played. The choice may be based on such considerations as playback quality, language, or the capabilities of the computer.

A value of zero indicates that the track is not in an alternate track group.

The most common reason for having alternate tracks is to provide versions of the same track in different languages. The following table shows an example of several tracks. The video track’s Alternate Group ID is `0`, which means that it is not in an alternate group (and its language codes are empty; normally, video tracks have the appropriate language tags). The three sound tracks have the same Group ID, so they form one alternate group, and the subtitle tracks have a different Group ID, so they form another alternate group. The tracks would not be adjacent in an actual QuickTime file; this is just a list of example track field values.

| Track type | Alternate group ID | Extended language tag | Language code |
| --- | --- | --- | --- |
| video (`vide`) | `0` |  |  |
| sound (`soun`) | `1` | `en-US` | `eng` |
| sound | `1` | `fr-FR` | `fra` |
| sound | `1` | `jp-JP` | `jpn` |
| subtitle (`subt`) | `2` | `en-US` | `eng` |
| subtitle | `2` | `fr-FR` | `fra` |

## See Also

- [Size](track_header_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this track header atom.
- [Type](track_header_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](track_header_atom/version.md)
  A 1-byte specification of the version of this track header.
- [Flags](track_header_atom/flags.md)
  Three bytes that are reserved for the track header flags.
- [Creation time](track_header_atom/creation_time.md)
  A 32-bit integer that indicates the creation calendar date and time for the track header.
- [Modification time](track_header_atom/modification_time.md)
  A 32-bit integer that indicates the last change date for the track header.
- [Track ID](track_header_atom/track_id.md)
  A 32-bit integer that uniquely identifies the track.
- [Reserved](track_header_atom/reserved.md)
  A 32-bit integer that is reserved for use by Apple.
- [Duration](track_header_atom/duration.md)
  A time value that indicates the duration of this track, in the movie’s time coordinate system.
- [Reserved](track_header_atom/reserved_2.md)
  An 8-byte value that is reserved for use by Apple.
- [Layer](track_header_atom/layer.md)
  A 16-bit integer that indicates this track’s spatial priority in its movie.
- [Volume](track_header_atom/volume.md)
  A 16-bit fixed-point value that indicates how loudly to play this track’s sound.
- [Reserved](track_header_atom/reserved_3.md)
  A 16-bit integer that is reserved for use by Apple.
- [Matrix structure](track_header_atom/matrix_structure.md)
  The matrix structure associated with this track.
- [Track width](track_header_atom/track_width.md)
  A 32-bit fixed-point number that specifies the width of this track in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_header_atom/alternate_group)*