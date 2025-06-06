# Referencing two data files with a single track

**Framework**: QuickTime File Format

Use multiple sample descriptions reference data in multiple files for a track.

#### Overview

The data reference index to be used for a given media sample is stored within that sample’s sample description. Therefore, a track must contain multiple sample descriptions in order for that track to reference multiple data files. A different sample description must be used whenever the data file changes or whenever the format of the data changes. The sample-to-chunk atom determines which sample description to use for a sample.

The sample description atom would contain the following data values:

```None
Sample description atom
├── Atom size: ...
├── Atom type: 'stsd'
├── Version/Flags: 0
└── Number of entries | 2
    ├── Sample description size[1]: ...
    ├── Data format: 'tmcd'
    ├── Reserved: 0
    ├── Data reference index: 1
    ├── (sample data): ...
    ├── Sample description size[1]: ...
    ├── Data format: 'tmcd'
    ├── Reserved: 0
    ├── Data reference index: 2
    └── (sample data): ...
```

If there is only 1 sample per chunk and the first 10 samples are extracted from sample description 2 and the next 30 samples are extracted from sample description 1, the sample-to-chunk atom would contain the following data values:

```None
Sample-to-chunk atom
├── Atom size: 40
├── Atom type: 'stsc'
├── Version/Flags: 0
└── Number of entries: 2
    ├── First chunk[1]: 1
    ├── Samples per chunk[1]: 1
    ├── Samples description ID[1]: 2
    ├── First chunk[2]: 11
    ├── Samples per chunk[2]: 1
    └── Samples description ID[2]: 1
```

The data reference atom would contain the following data values:

```None
Data information atom
├── Atom size: ...
├── Atom type: 'dinf'
└── Data reference atom
    ├── Atom size: ...
    ├── Atom type: 'dref'
    ├── Version/Flags: 0
    └── Number of entries: 2
        ├── Size[1]: ...
        ├── Type[1]: 'alis'
        ├── Version[1]: 0
        ├── Flags[1]: 0 (not self referenced)
        ├── Data reference[1]: [alias pointing to file #1]
        ├── Size[2]: ...
        ├── Type[2]: 'rsrc'
        ├── Version[2]: 0
        ├── Flags[2] | 0 (not self referenced)
        └── Data reference[2]: [alias pointing to file #2]
```

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
- [Sample-to-chunk atom ('stsc')](sample-to-chunk_atom.md)
  An atom that stores chunk information for the samples in a media.
- [Sample size atom ('stsz')](sample_size_atom.md)
  An atom you use to specify the size of each sample in the media.
- [Chunk offset atom ('stco')](chunk_offset_atom.md)
  An atom that identifies the location of each chunk of data in the media’s data stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/referencing_two_data_files_with_a_single_track)*