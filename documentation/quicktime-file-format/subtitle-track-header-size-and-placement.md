# Subtitle track header size and placement

**Framework**: QuickTime File Format

Specify the size and placement of subtitles.

#### Overview

Individual subtitles can be placed only within the subtitle track’s dimensions, adjusted by the subtitle track’s matrix. This is expressed relative to the main video track, allowing subtitles to overlay the video. Typically, all subtitles are placed at the bottom of the video. Alternatively, subtitles can be placed at a different vertical location, which allows individual subtitles at the bottom or the top of the associated video. This section describes how this is controlled and how track and subtitle geometry is established.

The value of the track dimensions and track matrix differ depending upon the absence or presence of the Vertical Placement (`0x20000000`) flag in the subtitle sample description’s display flags. When Vertical Placement is not set, subtitles are always placed at the bottom of the video. When Vertical Placement is set, the vertical position of subtitles can vary based upon the Text Box atom (`'tbox'`) in each sample.

In both cases, the subtitle track width must be the same as that of its associated main video (`'vide'`) track.

If the Vertical Placement flag (`0x20000000`) display flag of the sample description is not set, the following should be true:

- The subtitle track’s height should be 0.15 * the `'vide'` track header height. This allows room for two lines of subtitle text. For example, if the `'vide'` track header height is 720 pixels, then the `'sbtl'` track header height should be 108 (pixels).
- The subtitle track’s vertical placement is determined by the track matrix, which should be a simple vertical translation matrix that shifts the subtitle down by 0.85 * the `'vide'` track header height. For a subtitle media handler that obeys the tx3g rules, this positions the subtitles atop the bottom 15 percent of the video. Media handlers may choose to shift the subtitles further down in some modes; for example, in a playback mode that displays black bars above and below content, the video could be shifted up and the subtitles moved down into the bottom bar area.
- Subtitle samples must not contain a text box sample data extension (`'tbox'`) because no control over vertical placement is allowed.

Alternatively, if the Vertical Placement flag (`0x20000000`) display flag of the sample description is set, the following should be true:

- The height of the subtitle track should be the height of the video track header instead of 0.15 * the video track height. Because the subtitle track dimensions match the video track dimensions, subtitle text can be positioned at the bottom or top of the video, unlike when the Vertical Placement flag is not set.
- The track matrix should be the identity matrix.
- A subtitle’s placement is determined by the top coordinate of one of two rectangles. If the override text box sample data extension (`'tbox'`) is present, it is used. Otherwise, the default text box in the sample description is used. Some players will use the top coordinate to determine whether the subtitle is in the top half of the track dimensions and place the subtitle at the top of the video, otherwise placing it at the bottom of the video. Other players might use the top coordinate precisely, placing the subtitle at the specified vertical coordinate. As both playback environments are possible for a piece of content, it is recommend that a top coordinate of 0 be used for placing at the top and a top coordinate equal to the track height minus the subtitle height be used. In this way, if the content is played in either kind of player, its placement is predictable.

## See Also

- [Subtitle sample description](subtitle_sample_description.md)
  An atom that defines how to interpret subtitle media data.
- [Font table atom ('ftab')](font_table_atom.md)
  An atom that specifies the font used to display the subtitle.
- [Subtitle sample data](subtitle_sample_data.md)
  An atom that contains subtitle sample data.
- [Subtitle style atom ('styl')](subtitle_style_atom.md)
  An atom that specifies changes to the appearance of a subtitle.
- [Text box atom ('tbox')](text_box_atom.md)
  An atom that defines a text box for a subtitle sample.
- [Referencing a related forced subtitle track](referencing_a_related_forced_subtitle_track.md)
  Prevent overlapping a timed subtitle track with a forced subtitle track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/subtitle_track_header_size_and_placement)*