# Creating video tracks at 29.97 frames per second

**Framework**: QuickTime File Format

Configure your time-to-sample atom for 29.97 frames per second.

#### Overview

NTSC color video is not `30` frames per second (fps), but actually `29.97` fps. The previous example showed how the media time scale and the duration of the frames specify the video’s frame rate. By setting the media’s time scale to `2997` units per second and setting the frame durations to `100` units each, the effective rate is `29.97` fps exactly.

In this situation, it is also a good idea to set the movie time scale to `2997` in order to avoid movie edits that don’t land on frame boundaries. The movie’s time scale is stored in the movie header atom.

With a time scale of `2997` in the media header atom, the time-to-sample atom would contain the data values listed in following table.

| Field | Value |
| --- | --- |
| Atom size | `24` |
| Atom type | `'stts'` |
| Version/Flags | `0` |
| Number of entries | `1` |
| Sample count | `n` |
| Sample duration | `100` |

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/creating_video_tracks_at_2997_frames_per_second)*