# Sample-to-chunk atom ('stsc')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that stores chunk information for the samples in a media.

#### Overview

As samples are added to a media, they are collected into chunks that allow optimized data access. A chunk contains one or more samples. Chunks in a media may have different sizes, and the samples within a chunk may have different sizes. The sample-to-chunk atom stores chunk information for the samples in a media.

Sample-to-chunk atoms have an atom type of `'stsc'`. The sample-to-chunk atom contains a table that maps samples to chunks in the media data stream. By examining the sample-to-chunk atom, you can determine the chunk that contains a specific sample.

The layout of the sample-to-chunk atom is as follows.

| Sample-to-chunk atom data field | Bytes |
| --- | --- |
| [`Size`](sample-to-chunk_atom/size.md) | 4 |
| [`Type`](sample-to-chunk_atom/type.md) = `'stsc'` | 4 |
| [`Version`](sample-to-chunk_atom/version.md) | 1 |
| [`Flags`](sample-to-chunk_atom/flags.md) | 3 |
| [`Number of entries`](sample-to-chunk_atom/number_of_entries.md) | 4 |
| [`Sample-to-chunk table`](sample-to-chunk_atom/sample-to-chunk_table.md) | Variable |

## Topics

### Data fields
- [Size](sample-to-chunk_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this sample-to-chunk atom.
- [Type](sample-to-chunk_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](sample-to-chunk_atom/version.md)
  A 1-byte specification of the version of this sample-to-chunk atom.
- [Flags](sample-to-chunk_atom/flags.md)
  A 3-byte space for sample-to-chunk flags.
- [Number of entries](sample-to-chunk_atom/number_of_entries.md)
  A 32-bit integer containing the count of entries in the sample-to-chunk table.
- [Sample-to-chunk table](sample-to-chunk_atom/sample-to-chunk_table.md)
  A table that maps samples to chunks.

## See Also

- [Sample table atom ('stbl')](sample_table_atom.md)
  An atom that contains information for converting from media time to sample number to sample location.
- [Seeking with a QuickTime file](seeking_with_a_quicktime_file.md)
  Seek with a QuickTime file using child atoms.
- [Sample description atom ('stsd')](sample_description_atom.md)
  An atom that stores information that allows you to decode samples in the media.
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
- [Referencing two data files with a single track](referencing_two_data_files_with_a_single_track.md)
  Use multiple sample descriptions reference data in multiple files for a track.
- [Sample size atom ('stsz')](sample_size_atom.md)
  An atom you use to specify the size of each sample in the media.
- [Chunk offset atom ('stco')](chunk_offset_atom.md)
  An atom that identifies the location of each chunk of data in the media’s data stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sample-to-chunk_atom)*