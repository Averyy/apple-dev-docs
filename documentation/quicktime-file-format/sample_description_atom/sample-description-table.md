# Sample description table

**Framework**: QuickTime File Format  
**Kind**: property

An array of sample descriptions.

#### Overview

While the exact format of the sample description varies by media type, the first four fields of every sample description are the same.

- **Sample description size**: A 32-bit integer indicating the number of bytes in the sample description.

> ❗ **Important**: When parsing sample descriptions in the `‘stsd’` atom, be aware of the sample description size value in order to read each table entry correctly. Some sample descriptions terminate with four zero bytes that are not otherwise indicated.

- **Data format**: A 32-bit integer indicating the format of the stored data. This depends on the media type, but is usually either the compression format or the media type.
- **Reserved**: Six bytes that must be set to `0`.
- **Data reference index**: A 16-bit integer that contains the index of the data reference to use to retrieve data associated with samples that use this sample description. Data references are stored in data reference atoms.

These four fields may be followed by additional data specific to the media type and data format. See [`Media data atom types`](media_data_atom_types.md) for additional details regarding specific media types and media formats.

## See Also

- [Size](sample_description_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this sample description atom.
- [Type](sample_description_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](sample_description_atom/version.md)
  A 1-byte specification of the version of this sample description atom.
- [Flags](sample_description_atom/flags.md)
  A 3-byte space for sample description flags.
- [Number of entries](sample_description_atom/number_of_entries.md)
  A 32-bit integer containing the number of sample descriptions that follow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sample_description_atom/sample_description_table)*