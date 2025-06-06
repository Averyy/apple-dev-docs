# User data atoms

**Framework**: Quicktime File Format

Atoms you use to define and store data associated with a QuickTime object.

#### Overview

User data atoms allow you to define and store data associated with a QuickTime object, such as a movie `'moov'`, track `'trak'`, or media `'mdia'`. This includes both information that QuickTime looks for, such as copyright information or whether a movie should loop, and arbitrary information — provided by and for your application — that QuickTime simply ignores.

A user data atom whose immediate parent is a movie atom contains data relevant to the movie as a whole. A user data atom whose parent is a track atom contains information relevant to that specific track. A QuickTime movie file may contain many user data atoms, but only one user data atom is allowed as the immediate child of any given movie atom or track atom.

The user data atom has an atom type of `'udta'`. Inside the user data atom is a list of atoms describing each piece of user data. User data provides a simple way to extend the information stored in a QuickTime movie. For example, user data atoms can store a movie’s window position, playback characteristics, or creation information.

This section describes the data atoms that QuickTime recognizes. You may create new data atom types that your own application recognizes. Applications should ignore any data atom types that they do not recognize.

#### User Data List Entry Types

The user data list entry types are as follows.

| List entry type | Description | For sorting |
| --- | --- | --- |
| `'©arg'` | Name of arranger |  |
| `'©ark'` | Keywords for arranger | X |
| `'©cok'` | Keywords for composer | X |
| `'©com'` | Name of composer |  |
| `'©cpy'` | Copyright statement |  |
| `'©day'` | Date the movie content was created |  |
| `'©dir'` | Name of movie’s director |  |
| `'©ed1'` to `'©ed9'` | Edit dates and descriptions |  |
| `'©fmt'` | Indication of movie format (computer-generated, digitized, and so on) |  |
| `'©inf'` | Information about the movie |  |
| `'©isr'` | ISRC code |  |
| `'©lab'` | Name of record label |  |
| `'©lal'` | URL of record label |  |
| `'©mak'` | Name of file creator or maker |  |
| `'©mal'` | URL of file creator or maker |  |
| `'©nak'` | Title keywords of the content | X |
| `'©nam'` | Title of the content |  |
| `'©pdk'` | Keywords for producer | X |
| `'©phg'` | Recording copyright statement, normally preceded by the symbol ℗ |  |
| `'©prd'` | Name of producer |  |
| `'©prf'` | Names of performers |  |
| `'©prk'` | Keywords of main artist and performer | X |
| `'©prl'` | URL of main artist and performer |  |
| `'©req'` | Special hardware and software requirements |  |
| `'©snk'` | Subtitle keywords of the content | X |
| `'©snm'` | Subtitle of content |  |
| `'©src'` | Credits for those who provided movie source content |  |
| `'©swf'` | Name of songwriter |  |
| `'©swk'` | Keywords for songwriter | X |
| `'©swr'` | Name and version number of the software (or hardware) that generated this movie |  |
| `'©wrt'` | Name of movie’s writer |  |
| `'AllF'` | Play all frames—byte indicating that all frames of video should be played, regardless of timing |  |
| `'hinf'` | Hint track information—statistical data for real-time streaming of a particular track. For more information, see Hint Track User Data Atom in [`Hint media`](hint_media.md). |  |
| `'hnti'` | Hint info atom—data used for real-time streaming of a movie or a track. For more information, see Movie Hint Info Atom and Hint Track User Data Atom in [`Hint media`](hint_media.md). |  |
| `'name'` | Name of object |  |
| `'tnam'` | Localized track name optionally present in Track user data. The payload is described in [`Track name atom ('tnam')`](track_name_atom.md). |  |
| `'tagc'` | Media characteristic optionally present in Track user data—specialized text that describes something of interest about the track. For more information, see Media Characteristic Tags below. |  |
| `'LOOP'` | Long integer indicating looping style. This atom is not present unless the movie is set to loop. Values are 0 for normal looping, 1 for palindromic looping. |  |
| `'ptv '` | Print to video — display movie in full screen mode. This atom contains a 16-byte structure, described in [`Print to video atom ('ptv ')`](print_to_video_atom.md). |  |
| `'SelO'` | Play selection only—byte indicating that only the selected area of the movie should be played |  |
| `'WLOC'` | Default window location for movie—two 16-bit values, `{x,y}` |  |

The user-data items labelled “keywords” and marked as “For Sorting” are for use when the display text does not have a pre-determined sorting order (for example, in oriental languages when the sorting depends on the contextual meaning). These keywords can be sorted algorithmically to place the corresponding items in correct order.

The window location, looping, play selection only, play all frames, and print to video atoms control the way QuickTime displays a movie. These atoms are interpreted only if the user data atom’s immediate parent is a movie atom (`'moov'`). If they are included as part of a track atom’s user data, they are ignored.

#### User Data Text Strings and Language Codes

All user data list entries whose type begins with the © character (ASCII `169`) are defined to be international text. These list entries must contain a list of text strings with associated language codes. By storing multiple versions of the same text, a single user data text item can contain translations for different languages.

The list of text strings uses a small integer atom format, which is identical to the QuickTime atom format except that it uses 16-bit values for size and type instead of 32-bit values. The first value is the size of the string, including the size and type, and the second value is the language code for the string.

User data text strings may use either Macintosh text encoding or Unicode text encoding. The format of the language code determines the text encoding format. Macintosh language codes are followed by Macintosh-encoded text. If the language code is specified using the ISO language codes listed in specification ISO 639-2/T, the text uses Unicode text encoding. When Unicode is used, the text is in UTF-8 unless it starts with a byte-order-mark (BOM, `0xFEFF`), in which case the text is in UTF-16. Both the BOM and the UTF-16 text should be big-endian. Multiple versions of the same text may use different encoding schemes.

> ❗ **Important**: Language code values less than `0x400` are Macintosh language codes. Language code values greater than or equal to `0x400` are ISO language codes. The exception to this rule is language code `0x7FF`F, which indicates an unspecified Macintosh language.

ISO language codes are three-character codes. In order to fit inside a 16-bit field, the characters must be packed into three 5-bit subfields. This packing is described in [`Language code values`](language_code_values.md).

#### Media Characteristic Tags

A track (`'trak'`) atom’s user data atom may contain zero or more media characteristic tag atoms (`'tagc'`).

The media characteristic tag atom’s payload data is a tag that indicates something of interest about the track. This is a specialized string consisting of a subset of US-ASCII (7 bits plus a clear high bit) characters and conforming to the structure described in the following paragraphs. This is not a C string; there is no terminating null, so the number of characters is determined from the atom’s size. Legal characters are alphabetic (`A-Z`, `a-z`), digits (`0-9`), dash (`-`), period (`.`), underscore (`_`), and tilde (`~`).

Any track of a QuickTime file can be associated with one or more tags that indicate the media’s characteristics. Tags indicate something of interest about a track. For example, a tag could indicate the purpose of the track (it is commentary), an abstract characteristic of the track (it requires hardware decoding), or an indication that the track includes legible text (a chapter track and subtitle track both can be read by the user).

Comparison of tags is case sensitive; two tags match if the bytes of the strings match exactly. To avoid possible confusion for developers or content creators, don’t use two tag strings differing only by case.

Duplicate tags in a single track are allowed but are discouraged. Duplication has no special meaning.

Tag strings are not localized and are meant to be machine interpreted; however, mnemonic strings are encouraged.

A tag is either public or private:

- Public tags allow shared semantics to be deployed widely. Apple defines public tags.
- Private tags can be defined for private use.

Tag strings have the following structure:

- A public tag starts with the prefix “`public.`”, which is followed by one or more segments separated by periods. Examples (not defined) might be `public.subtitle` or `public.commentary.director`.

> **Note**: Public tags are public because they are documented in this specification or are available in Apple APIs. Other definitions of tags with the “`public.`” prefix are prohibited; use private tags instead.

- A private tag starts with the private entity’s domain using a reverse DNS naming convention. For example, `apple.com` becomes `com.apple`. This is followed by one or more segments separated by periods. Examples (not defined) might be `com.apple.this-is-a-tag`, `com.apple.video.includes-sign-language`, and `org.w3c.html5.referenced-video`.
- The only allowed prefixes are “`public.`” and reversed domains. All other prefixes are reserved for future use.

> **Note**: Generic top-level domains other than “`public`” (if it were to be assigned) are supported. The string “`public`” is reserved to signal public media characteristic tags.

This specification defines the following public media characteristic tags. Other public and private tags could be defined outside the specification; unrecognized tags should be ignored.

## Topics

### Atoms for user data
- [User data atom ('udta')](user_data_atom.md)
  An atom where you define and store data associated with a QuickTime object.
- [Track name atom ('tnam')](track_name_atom.md)
  An atom that provides a name for a track.
- [Print to video atom ('ptv ')](print_to_video_atom.md)
  An atom you use to play the movie in full-screen mode, with no window and no visible controller.

## See Also

- [Movie atom ('moov')](movie_atom.md)
  An atom that specifies the information that defines a movie.
- [Movie header atom ('mvhd')](movie_header_atom.md)
  An atom that specifies the characteristics of an entire QuickTime movie.
- [Color table atom ('ctab')](color_table_atom.md)
  An atom that defines a list of preferred colors for displaying the movie on devices that support only 256 colors.
- [Interleaving movie data](interleaving_movie_data.md)
  Interleave data in your movie for optimal playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/user_data_atoms)*