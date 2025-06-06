# Composition shift least greatest atom ('cslg')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that summarizes the calculated minimum and maximum offsets between decode and composition time, as well as the start and end times, for all samples.

#### Overview

The optional composition shift least greatest atom summarizes the calculated minimum and maximum offsets between decode and composition time, as well as the start and end times, for all samples. This allows a reader to determine the minimum required time for decode to obtain proper presentation order without needing to scan the sample table for the range of offsets. The type of the composition shift least greatest atom is `‘cslg’`.

The layout of a composition shift least greatest atom is as follows.

| Composition shift least greatest atom data field | Bytes |
| --- | --- |
| [`Size`](composition_shift_least_greatest_atom/size.md) | 4 |
| [`Type`](composition_shift_least_greatest_atom/type.md) = `'cslg'` | 4 |
| [`Version`](composition_shift_least_greatest_atom/version.md) | 1 |
| [`Flags`](composition_shift_least_greatest_atom/flags.md) | 3 |
| [`compositionOffsetToDisplayOffsetShift`](composition_shift_least_greatest_atom/compositionoffsettodisplayoffsetshift.md) | 4 |
| [`leastDisplayOffset`](composition_shift_least_greatest_atom/leastdisplayoffset.md) | 4 |
| [`greatestDisplayOffset`](composition_shift_least_greatest_atom/greatestdisplayoffset.md) | 4 |
| [`displayStartTime`](composition_shift_least_greatest_atom/displaystarttime.md) | 4 |
| [`displayEndTime`](composition_shift_least_greatest_atom/displayendtime.md) | 4 |

## Topics

### Data fields
- [Size](composition_shift_least_greatest_atom/size.md)
  A 32-bit integer that specifies the number of bytes in the composition shift least greatest atom atom.
- [Type](composition_shift_least_greatest_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](composition_shift_least_greatest_atom/version.md)
  A 1-byte specification of the version of this atom.
- [Flags](composition_shift_least_greatest_atom/flags.md)
  A 3-byte space reserved for flags.
- [compositionOffsetToDisplayOffsetShift](composition_shift_least_greatest_atom/compositionoffsettodisplayoffsetshift.md)
  A 32-bit unsigned integer that specifies the calculated value.
- [leastDisplayOffset](composition_shift_least_greatest_atom/leastdisplayoffset.md)
  A 32-bit unsigned integer that specifies the calculated value.
- [greatestDisplayOffset](composition_shift_least_greatest_atom/greatestdisplayoffset.md)
  A 32-bit unsigned integer that specifies the calculated value.
- [displayStartTime](composition_shift_least_greatest_atom/displaystarttime.md)
  A 32-bit signed integer that specifies the calculated value.
- [displayEndTime](composition_shift_least_greatest_atom/displayendtime.md)
  A 32-bit signed integer that specifies the calculated value.

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/composition_shift_least_greatest_atom)*