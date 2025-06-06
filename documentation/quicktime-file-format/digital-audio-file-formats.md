# Digital audio file formats

**Framework**: QuickTime File Format

#### Overview

| MPEG 1 layer 3 | Description |
| --- | --- |
| Supported by | Movie import component |
| Macintosh file type | `'Mp3 '`, `'SwaT'`, `'MPEG'`, `'PLAY'`, `'MPG3'`, `'MP3 '` |
| File name extensions | `.mp3`, `.swa` |
| Metadata handling | Metadata from ID3v1-style MP3 files is imported into the QuickTime movie.Title maps to `kUserDataTextFullName`, artist maps to `'©ART'`, album maps to `'©alb'`, year maps to `'©day'`, comment maps to `'©cmt'`, and track number maps to `'©des'`. |
| Software required | QuickTime 4 |

| WAV | Description |
| --- | --- |
| Supported by | Movie import component |
| Macintosh file type | `'WAVE'`, `'.WAV'` |
| File name extensions | `.wav` |
| Metadata handling | All Microsoft-defined “tombstone” data is transferred to the imported movie’s user data. Metadata fields that have QuickTime equivalents are mapped as follows: `'ICOP'` maps to `kUserDataTextCopyright`, `'ISBJ'` maps to `kUserDataTextInformation`, `'INAM'` maps to `kUserDataTextFullName`, `'ICRD'` maps to `'©day'`, `'IMED'` maps to `'©fmt'`, `'ISRC'` maps to `'©src'`. Where no QuickTime equivalent exists, the metadata item’s four-character code is modified by replacing the initial `I` with the symbol `©`. All other characters remain unchanged. |
| Software required | QuickTime 2.5 or later |

## See Also

- [Digital video file formats](digital_video_file_formats.md)
- [Still image file formats](still_image_file_formats.md)
- [Animation and 3D file formats](animation_and_3d_file_formats.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/digital_audio_file_formats)*