# Sample description atom ('stsd')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that stores information that allows you to decode samples in the media.

## Mentions

- [Sprite media](sprite_media.md)
- [QuickTime File Format change log](revision_history.md)
- [Music media](music_media.md)
- [MPEG-1 media](mpeg-1_media.md)

#### Overview

The data stored in the sample description varies, depending on the media type. For example, in the case of video media, the sample descriptions are image description structures. The sample description information for each media type is explained in [`Media data atom types`](media_data_atom_types.md).

The layout of the sample description atom is as follows.

| Sample description atom data field | Bytes |
| --- | --- |
| [`Size`](sample_description_atom/size.md) | 4 |
| [`Type`](sample_description_atom/type.md) = `'stsd'` | 4 |
| [`Version`](sample_description_atom/version.md) | 1 |
| [`Flags`](sample_description_atom/flags.md) | 3 |
| [`Number of entries`](sample_description_atom/number_of_entries.md) | 4 |
| [`Sample description table`](sample_description_atom/sample_description_table.md) | Variable |

The sample description atom has an atom type of `'stsd'`. The sample description atom contains a table of sample descriptions. A media may have one or more sample descriptions, depending upon the number of different encoding schemes used in the media and on the number of files used to store the data. The sample-to-chunk atom identifies the sample description for each sample in the media by specifying the index into this table for the appropriate description (see [`Sample-to-chunk atom ('stsc')`](sample-to-chunk_atom.md)).

#### General Structure of a Sample Description

While the exact format of the sample description varies by media type, the first four fields of every sample description are the same.

> ❗ **Important**: When parsing sample descriptions in the `‘stsd’` atom, be aware of the sample description size value in order to read each table entry correctly. Some sample descriptions terminate with four zero bytes that are not otherwise indicated.

These four fields may be followed by additional data specific to the media type and data format. See [`Media data atom types`](media_data_atom_types.md) for additional details regarding specific media types and media formats.

## Topics

### Data fields
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
- [Sample description table](sample_description_atom/sample_description_table.md)
  An array of sample descriptions.

## See Also

- [Sample table atom ('stbl')](sample_table_atom.md)
  An atom that contains information for converting from media time to sample number to sample location.
- [Seeking with a QuickTime file](seeking_with_a_quicktime_file.md)
  Seek with a QuickTime file using child atoms.
- [Time-to-sample atom ('stts')](time-to-sample_atom.md)
  An atom that stores duration information for a media’s samples, providing a mapping from a time in a media to the corresponding data sample.
- [Creating video tracks at 30 frames per second](creating_video_tracks_at_30_frames_per_second.md)
  Configure your time-to-sample atom for 30 frames per second.
- [Creating video tracks at 29.97 frames per second](creating_video_tracks_at_2997_frames_per_second.md)
  Configure your time-to-sample atom for 29.97 frames per second.
- [Creating sound tracks at 44.1 kHz](creating_sound_tracks_at_441_khz.md)
  Configure your time-to-sample atom for sound at 44.1 kHz.
- [Composition offset atom ('ctts')](composition_offset_atom.md)
  An atom you use to specify out-of-order video samples.
- [Composition shift least greatest atom ('cslg')](composition_shift_least_greatest_atom.md)
  An atom that summarizes the calculated minimum and maximum offsets between decode and composition time, as well as the start and end times, for all samples.
- [Using composition offset and composition shift least greatest atoms](using_composition_offset_and_composition_shift_least_greatest_atoms.md)
  Calculate the offset shift when you store an out of order video stream’s sample table.
- [Sync sample atom ('stss')](sync_sample_atom.md)
  An atom that identifies the key frames in the media.
- [Partial sync sample atom ('stps')](partial_sync_sample_atom.md)
  An atom that lists the partial sync samples.
- [Sample-to-chunk atom ('stsc')](sample-to-chunk_atom.md)
  An atom that stores chunk information for the samples in a media.
- [Referencing two data files with a single track](referencing_two_data_files_with_a_single_track.md)
  Use multiple sample descriptions reference data in multiple files for a track.
- [Sample size atom ('stsz')](sample_size_atom.md)
  An atom you use to specify the size of each sample in the media.
- [Chunk offset atom ('stco')](chunk_offset_atom.md)
  An atom that identifies the location of each chunk of data in the media’s data stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sample_description_atom)*