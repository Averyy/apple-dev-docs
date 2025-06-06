# Partial sync sample atom ('stps')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that lists the partial sync samples.

#### Overview

Since such samples are not full sync samples, don’t list them in the sync sample atom.

The type of the partial sync sample atom is `‘stps’`.

The layout of the partial sync sample atom is as follows.

| Partial sync sample atom data field | Bytes |
| --- | --- |
| [`Size`](partial_sync_sample_atom/size.md) | 4 |
| [`Type`](partial_sync_sample_atom/type.md) = `'stps'` | 4 |
| [`Version`](partial_sync_sample_atom/version.md) | 1 |
| [`Flags`](partial_sync_sample_atom/flags.md) | 3 |
| [`Entry count`](partial_sync_sample_atom/entry_count.md) | 4 |
| [`Partial sync sample table`](partial_sync_sample_atom/partial_sync_sample_table.md) | Variable |

## Topics

### Data fields
- [Size](partial_sync_sample_atom/size.md)
  A 32-bit integer that specifies the number of bytes in the partial sync sample atom.
- [Type](partial_sync_sample_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](partial_sync_sample_atom/version.md)
  A 1-byte specification of the version of this atom.
- [Flags](partial_sync_sample_atom/flags.md)
  A 3-byte space reserved for flags.
- [Entry count](partial_sync_sample_atom/entry_count.md)
  A 32-bit unsigned integer that specifies the number of sample numbers in the array that follows.
- [Partial sync sample table](partial_sync_sample_atom/partial_sync_sample_table.md)
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
- [Sync sample atom ('stss')](sync_sample_atom.md)
  An atom that identifies the key frames in the media.
- [Sample-to-chunk atom ('stsc')](sample-to-chunk_atom.md)
  An atom that stores chunk information for the samples in a media.
- [Referencing two data files with a single track](referencing_two_data_files_with_a_single_track.md)
  Use multiple sample descriptions reference data in multiple files for a track.
- [Sample size atom ('stsz')](sample_size_atom.md)
  An atom you use to specify the size of each sample in the media.
- [Chunk offset atom ('stco')](chunk_offset_atom.md)
  An atom that identifies the location of each chunk of data in the media’s data stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/partial_sync_sample_atom)*