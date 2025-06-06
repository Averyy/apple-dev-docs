# Extended language tag atom ('elng')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that represents media language information.

## Mentions

- [Language code values](language_code_values.md)
- [QuickTime File Format change log](revision_history.md)

#### Overview

The extended language tag atom represents media language information based on the RFC 4646 (Best Common Practices (BCP) #47) industry standard. It is an optional peer of the media header atom and follows the definition of the media header atom in a QuickTime movie. There is at most one extended language tag atom per media atom and, in turn, per track. The extended language tag atom has an atom type of `'elng'`.

Until the introduction of this atom type, QuickTime had support for languages via codes based on either ISO 639 or the classic Macintosh language codes. These language codes are associated to a media (per track) in a QuickTime movie and are referred to as the . For more information, see [`Language code values`](language_code_values.md).

To distinguish the extended language support from the old system, it is referred to as the  as opposed to . The major advantage of the extended language tag is that it includes additional information such as region, script, variation, and so on, as parts (or subtags). For instance, this additional information allows distinguishing content in French as spoken in Canada from content in French as spoken in France.

The layout of an extended language tag atom is as follows.

| Extended language tag atom | Bytes |
| --- | --- |
| [`Size`](extended_language_tag_atom/size.md) | 4 |
| [`Type`](extended_language_tag_atom/type.md) | 4 |
| [`Version`](extended_language_tag_atom/version.md) | 1 |
| [`Flags`](extended_language_tag_atom/flags.md) | 3 |
| [`Language tag string`](extended_language_tag_atom/language_tag_string.md) | Variable |

Additional notes:

- The extended language tag overrides the media language if they are not consistent.
- The extended language tag atom is optional; if it is absent, use the media language.
- No validation of the language tag string is performed. Applications parsing QuickTime movies need to be prepared for an invalid language tag, and are expected to behave as if no information is found.
- For best compatibility with earlier players, if an extended language tag is specified, specify the most compatible language code in the language field of the `'mdhd'` atom (for example, “eng” if the extended language tag is “en-AU”). If there is no reasonably compatible tag, the packed form of `'und'` can be specified in the language code of the `'mdhd'` atom.

## Topics

### Data fields
- [Size](extended_language_tag_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this media header atom.
- [Type](extended_language_tag_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](extended_language_tag_atom/version.md)
  One byte that specifies the version of this header atom.
- [Flags](extended_language_tag_atom/flags.md)
  Three bytes of space for media header flags.
- [Language tag string](extended_language_tag_atom/language_tag_string.md)
  A string containing a language tag.

## See Also

- [Media atom ('mdia')](media_atom.md)
  An atom that describes and defines a track’s media type and sample data.
- [Media header atom ('mdhd')](media_header_atom.md)
  An atom that specifies the characteristics of a media, including time scale and duration.
- [Handler reference atom ('hdlr')](handler_reference_atom.md)
  An atom that specifies the media handler component that is to be used to interpret the media’s data.
- [Media information atoms](media_information_atoms.md)
  An atom that contains a number of other atoms that define specific characteristics of the video media data.
- [Video media information atom ('minf')](video_media_information_atom.md)
  An atom that contains a number of other atoms that define specific characteristics of the video media data.
- [Video media information header atom ('vmhd')](video_media_information_header_atom.md)
  An atom that defines specific color and graphics mode information.
- [Sound media information atom ('minf')](sound_media_information_atom.md)
  An atom that contains a number of other atoms that define specific characteristics of the sound media data.
- [Sound media information header atom ('smhd')](sound_media_information_header_atom.md)
  An atom that stores the sound media’s control information, such as balance.
- [Base media information atom ('minf')](base_media_information_atom.md)
  An atom that stores the media information for media types such as timed metadata, text, MPEG, time code, and music.
- [Base media information header atom ('gmhd')](base_media_information_header_atom.md)
  An atom that indicates that this media information atom pertains to a base media.
- [Base media info atom ('gmin')](base_media_info_atom.md)
  An atom that defines the media’s control information, including graphics mode and balance information.
- [Data information atom ('dinf')](data_information_atom.md)
  An atom that specifies the data handler component that provides access to the media data.
- [Media data reference atom ('dref')](media_data_reference_atom.md)
  An atom that contains tabular data that instructs the data handler component how to access the media’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/extended_language_tag_atom)*