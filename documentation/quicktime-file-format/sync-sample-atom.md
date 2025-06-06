# Sync sample atom ('stss')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that identifies the key frames in the media.

#### Overview

In a media that contains compressed data, key frames define starting points for portions of a temporally compressed sequence. The key frame is self-contained — that is, it is independent of preceding frames. Subsequent frames may depend on the key frame.

The sync sample atom provides a compact marking of the random access points within a stream. The table is arranged in strictly increasing order of sample number. If this table is not present, every sample is implicitly a random access point.

Sync sample atoms have an atom type of `'stss'`. The sync sample atom contains a table of sample numbers. Each entry in the table identifies a sample that is a key frame for the media. If no sync sample atom exists, then all the samples are key frames.

The layout of a sync sample atom is as follows.

| Sync sample atom data field | Bytes |
| --- | --- |
| [`Size`](sync_sample_atom/size.md) | 4 |
| [`Type`](sync_sample_atom/type.md) = `'stss'` | 4 |
| [`Version`](sync_sample_atom/version.md) | 1 |
| [`Flags`](sync_sample_atom/flags.md) | 3 |
| [`Number of entries`](sync_sample_atom/number_of_entries.md) | 4 |
| [`Sync sample table`](sync_sample_atom/sync_sample_table.md) | Variable |

## Topics

### Data fields
- [Size](sync_sample_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this sync sample atom.
- [Type](sync_sample_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](sync_sample_atom/version.md)
  A 1-byte specification of the version of this sync sample atom.
- [Flags](sync_sample_atom/flags.md)
  A 3-byte space for sync sample flags.
- [Number of entries](sync_sample_atom/number_of_entries.md)
  A 32-bit integer containing the count of entries in the sync sample table.
- [Sync sample table](sync_sample_atom/sync_sample_table.md)
  A table of sample numbers.

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sync_sample_atom)*