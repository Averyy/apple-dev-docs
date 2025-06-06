# Digital video file formats

**Framework**: QuickTime File Format

#### Overview

| OpenDML and other AVI files | Description |
| --- | --- |
|  |  |
| Supported by | Movie import component |
| Macintosh file type | `'VfW '` |
| File name extensions | .avi |
| metadata handling | All Microsoft-defined “tombstone” data is transferred to the imported movie’s user data. Metadata fields that have QuickTime equivalents are mapped as follows: `'ICOP'` maps to `kUserDataTextCopyright`, `'ISBJ'` maps to `kUserDataTextInformation`, `'INAM'` maps to `kUserDataTextFullName`, `'ICRD'` maps to `'©day'`, `'IMED'` maps to `'©fmt'`, `'ISRC'` maps to `'©src'`. Where no QuickTime equivalent exists, the metadata item’s four-character code is modified by replacing the initial `I` with the symbol `©`. All other characters remain unchanged. |
| Software required | QuickTime 3 |

## See Also

- [Digital audio file formats](digital_audio_file_formats.md)
- [Still image file formats](still_image_file_formats.md)
- [Animation and 3D file formats](animation_and_3d_file_formats.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/digital_video_file_formats)*