# Still image file formats

**Framework**: QuickTime File Format

#### Overview

| FlashPix | Description |
| --- | --- |
| Supported by | Graphics import component |
| Macintosh file type | `'FPix'` |
| File name extensions | `.fpx` |
| Metadata handling | Information about copyright, authorship, caption text, content description notes, camera manufacturer name, camera model name are transferred to `kUserDataTextCopyright`, `kUserDataTextArtistField`, `kUserDataTextFullName`, `kParameterInfoWindowTitle`, `kParameterInfoManufacturer`, `kUserDataTextMakeField` user data items, respectively. |
| Formats supported | 1.0 |
| Software required | QuickTime 4 |

| GIF | Description |
| --- | --- |
| Supported by | Graphics import component |
| Macintosh file type | `'GIFf'`, or `'GIF '` |
| File name extensions | `.gif` |
| Metadata handling | The GIF comment field is transferred to the `kUserDataDateTextInformation` user data item. |
| Software required | QuickTime 2.5 or later |

| JFIF/JPEG | Description |
| --- | --- |
| Supported by | Graphics import component |
| Macintosh file type | `'JPEG’` |
| File name extensions | `.jpg` |
| Metadata handling | The JFIF comment field is transferred to the imported Movie’s user data in the `kUserDataTextInformation` field. |
| Software required | QuickTime 2.5 or later |

| Photoshop | Description |
| --- | --- |
| Supported by | Graphics import component |
| Macintosh file type | `'8BPS'` |
| File name extensions | `.psd` |
| Metadata handling | Photoshop files store their metadata based on the IPTC-NAA Information Interchange Model and Digital Newsphoto Parameter Record. This information is transferred into the importer Movie’s user data. The entire ITPC-NAA record is placed into a user data item of type `'iptc'`. In addition, those metadata items which are defined by QuickTime are mapped directly to QuickTime types as follows: 116 to `kUserDataTextCopyright`, 120 to `kUserDataTextInformation`, 105 to `kUserDataTextFullName`, 55 to `'©day'`, 115 to `'©src'`. |
| Software required | QuickTime 2.5 or later. QuickTime 3 is required for metadata handling. |

| QuickTime Image File | Description |
| --- | --- |
| Supported by | Graphics import component |
| Macintosh file type | `'qtif'` |
| File name extensions | `.qtif`, `.qif`, `.qti` |
| Metadata handling | Metadata that is stored in `quickTimeImageFileMetaDataAtom` atom is copied directly to the Movie’s user data. |
| Formats supported | All |
| Software required | QuickTime 2.5 or later |

| TIFF | Description |
| --- | --- |
| Supported by | Graphics Import Component |
| Macintosh file type | `'TIFF'` |
| File name extensions | `.tif`, `.tiff` |
| Metadata handling | Extracted from standard tags and from IPTC block |
| Software required | QuickTime 3 or later |

## See Also

- [Digital video file formats](digital_video_file_formats.md)
- [Digital audio file formats](digital_audio_file_formats.md)
- [Animation and 3D file formats](animation_and_3d_file_formats.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/still_image_file_formats)*