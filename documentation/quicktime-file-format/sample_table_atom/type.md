# Type

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 32-bit integer that identifies the atom type.

#### Overview

This field must be set to `'stbl'`.

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer that specifies the number of bytes in this sample table atom.
- [Sample description atom](./sample_description_atom.md)
  An atom that stores information that allows you to decode samples in the media.
- [Time-to-sample atom](./time-to-sample_atom.md)
  An atom that stores duration information for a media’s samples, providing a mapping from a time in a media to the corresponding data sample.
- [Composition offset atom](./composition_offset_atom.md)
  An atom you use to specify out-of-order video samples.
- [Composition shift least greatest atom](./composition_shift_least_greatest_atom.md)
  An atom that summarizes the calculated minimum and maximum offsets between decode and composition time, as well as the start and end times, for all samples.
- [Sync sample atom](./sync_sample_atom.md)
  An atom that identifies the key frames in the media.
- [Partial sync sample atom](./partial_sync_sample_atom.md)
  An atom that lists the partial sync samples.
- [Sample-to-chunk atom](./sample-to-chunk_atom.md)
  An atom that stores chunk information for the samples in a media.
- [Sample size atom](./sample_size_atom.md)
  An atom you use to specify the size of each sample in the media.
- [Chunk offset atom](./chunk_offset_atom.md)
  An atom that identifies the location of each chunk of data in the media’s data stream.
- [Sample dependency flags atom](./sample_dependency_flags_atom.md)
  An atom that uses one byte per sample as a bit field that describes dependency information.
- [Shadow sync atom](./shadow_sync_atom.md)
  An atom reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sample_table_atom/type)*