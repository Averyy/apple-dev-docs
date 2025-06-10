# Sample table atom ('stbl')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains information for converting from media time to sample number to sample location.

## Mentions

- [Streaming media](streaming_media.md)
- [Tween sample description](tween_sample_description.md)
- [3D media](3d_media.md)

#### Overview

This atom also indicates how to interpret the sample (for example, whether to decompress the video data and, if so, how). This section describes the format and content of the sample table atom.

The sample table atom has an atom type of `'stbl'`. It can contain the sample description atom, the time-to-sample atom, the sync sample atom, the sample-to-chunk atom, the sample size atom, the chunk offset atom, and the shadow sync atom. Recent additions to the list of atom types that a sample table atom can contain are the optional sample group description and sample-to-group atoms included in [`Audio priming-handling encoder delay in AAC`](appendix_g_audio_priming_handling_encoder_delay_in_aac.md).

The sample table atom contains all the time and data indexing of the media samples in a track. Using tables, it is possible to locate samples in time, determine their type, and determine their size, container, and offset into that container.

If the track that contains the sample table atom references no data, then the sample table atom does not need to contain any child atoms (not a very useful media track).

If the track that the sample table atom is contained in does reference data, then the following child atoms are required: sample description, sample size, sample to chunk, and chunk offset. All of the subtables of the sample table use the same total sample count.

The sample description atom must contain at least one entry. A sample description atom is required because it contains the data reference index field that indicates which data reference atom to use to retrieve the media samples. Without the sample description, it is not possible to determine where the media samples are stored. The sync sample atom is optional. If the sync sample atom is not present, all samples are implicitly sync samples.

The layout of the sample table atom is as follows.

| Data | Type |
| --- | --- |
| [`Size`](sample_table_atom/size.md) | 4 bytes |
| [`Type`](sample_table_atom/type.md) = `'stbl'` | 4 bytes |
| [`Sample description atom`](sample_table_atom/sample_description_atom.md) | `'stsd'` |
| [`Time-to-sample atom`](sample_table_atom/time-to-sample_atom.md) | `'stts'` |
| [`Composition offset atom`](sample_table_atom/composition_offset_atom.md) | `'ctts'` |
| [`Composition shift least greatest atom`](sample_table_atom/composition_shift_least_greatest_atom.md) | `'cslg'` |
| [`Sync sample atom`](sample_table_atom/sync_sample_atom.md) | `'stss'` |
| [`Partial sync sample atom`](sample_table_atom/partial_sync_sample_atom.md) | `'stps'` |
| [`Sample-to-chunk atom`](sample_table_atom/sample-to-chunk_atom.md) | `'stsc'` |
| [`Sample size atom`](sample_table_atom/sample_size_atom.md) | `'stsz'` |
| [`Chunk offset atom`](sample_table_atom/chunk_offset_atom.md) | `'stco'` |
| [`Sample dependency flags atom`](sample_table_atom/sample_dependency_flags_atom.md) | `'sdtp'` |
| [`Shadow sync atom`](sample_table_atom/shadow_sync_atom.md) | `'stsh'` |

## Topics

### Data fields
- [Size](sample_table_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this sample table atom.
- [Type](sample_table_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Sample description atom](sample_table_atom/sample_description_atom.md)
  An atom that stores information that allows you to decode samples in the media.
- [Time-to-sample atom](sample_table_atom/time-to-sample_atom.md)
  An atom that stores duration information for a media’s samples, providing a mapping from a time in a media to the corresponding data sample.
- [Composition offset atom](sample_table_atom/composition_offset_atom.md)
  An atom you use to specify out-of-order video samples.
- [Composition shift least greatest atom](sample_table_atom/composition_shift_least_greatest_atom.md)
  An atom that summarizes the calculated minimum and maximum offsets between decode and composition time, as well as the start and end times, for all samples.
- [Sync sample atom](sample_table_atom/sync_sample_atom.md)
  An atom that identifies the key frames in the media.
- [Partial sync sample atom](sample_table_atom/partial_sync_sample_atom.md)
  An atom that lists the partial sync samples.
- [Sample-to-chunk atom](sample_table_atom/sample-to-chunk_atom.md)
  An atom that stores chunk information for the samples in a media.
- [Sample size atom](sample_table_atom/sample_size_atom.md)
  An atom you use to specify the size of each sample in the media.
- [Chunk offset atom](sample_table_atom/chunk_offset_atom.md)
  An atom that identifies the location of each chunk of data in the media’s data stream.
- [Sample dependency flags atom](sample_table_atom/sample_dependency_flags_atom.md)
  An atom that uses one byte per sample as a bit field that describes dependency information.
- [Shadow sync atom](sample_table_atom/shadow_sync_atom.md)
  An atom reserved for future use.

## See Also

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
- [Sample-to-chunk atom ('stsc')](sample-to-chunk_atom.md)
  An atom that stores chunk information for the samples in a media.
- [Referencing two data files with a single track](referencing_two_data_files_with_a_single_track.md)
  Use multiple sample descriptions reference data in multiple files for a track.
- [Sample size atom ('stsz')](sample_size_atom.md)
  An atom you use to specify the size of each sample in the media.
- [Chunk offset atom ('stco')](chunk_offset_atom.md)
  An atom that identifies the location of each chunk of data in the media’s data stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sample_table_atom)*