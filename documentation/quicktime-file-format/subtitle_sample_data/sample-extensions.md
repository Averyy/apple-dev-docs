# Sample extensions

**Framework**: QuickTime File Format  
**Kind**: property

One or more atoms containing additional information for selecting and drawing the subtitle.

#### Overview

The following table lists the currently defined subtitle sample extensions.

| Subtitle sample extension | Description |
| --- | --- |
| `'frcd'` | The presence of this atom indicates that the sample contains a forced subtitle. This extension has no data. Forced subtitles are shown automatically when appropriate without any interaction from the user. If any sample contains a forced subtitle, the Some Samples Are Forced (`0x40000000`) flag must also be set in the display flags. Consider an example where the primary language of the content is English, but the user has chosen to listen to a French dub of the audio. If a scene in the video displays something in English that is important to the plot or the content (such as a newspaper headline), a forced subtitle displays the content translated into French. In this case, the subtitle is linked (“forced”) to the French language sound track. If this atom is not present, the subtitle is typically simply a translation of the audio content, which a user can choose to display or hide. |
| `'styl'` | Style information for the subtitle. This atom allows you to override the default style in the sample description or to define more than one style within a sample. See [`Subtitle style atom ('styl')`](subtitle_style_atom.md). |
| `'tbox'` | Override of the default text box for this sample. Used only if the `0x20000000` display flag is set in the sample description and, in that case, only the top is considered. Even so, all fields should be set as though they are considered. See [`Text box atom ('tbox')`](text_box_atom.md). |
| `'twrp'` | Text wrap. Set the one-byte payload to `0x00` for no wrapping or `0x01` for automatic soft wrapping. |

## See Also

- [Text size](subtitle_sample_data/text_size.md)
  A 16-bit word that specifies the length (number of bytes) of the subtitle text.
- [Text](subtitle_sample_data/text.md)
  The subtitle text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/subtitle_sample_data/sample_extensions)*