# Sample atoms

**Framework**: QuickTime File Format

Atoms that describe samples, which are single elements in a sequence of time-ordered data.

#### Overview

QuickTime stores media data in samples. A sample is a single element in a sequence of time-ordered data. Samples are stored in the media, and they may have varying durations.

Samples are stored in a series of chunks in a media. Chunks are a collection of data samples in a media that allow optimized data access. A chunk may contain one or more samples. Chunks in a media may have different sizes, and the individual samples within a chunk may have different sizes from one another, as shown in the following figure.

![A diagram that represents a data stream as a vertical stack of boxes, with each box representing a sequentially numbered sample. The sample boxes have labels adjacent to them, that group samples into chunks. The first three boxes, samples one, two, and three, are grouped into chunk one. The next three boxes, samples four, five, and six, are grouped into chunk two. Sample seven is chunk three, sample eight is chunk four, and sample nine is chunk five.](https://docs-assets.developer.apple.com/published/a6e9402c4d566f89c2956cf135912297/data-stream%402x.png)

One way to describe a sample is to use a sample table atom. The sample table atom acts as a storehouse of information about the samples and contains a number of different types of atoms. The various atoms contain information that allows the media handler to parse the samples in the proper order. This approach enforces an ordering of the samples without requiring that the sample data be stored sequentially with respect to movie time in the actual data stream.

## Topics

### Describing samples
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
- [Referencing two data files with a single track](referencing_two_data_files_with_a_single_track.md)
  Use multiple sample descriptions reference data in multiple files for a track.
- [Sample size atom ('stsz')](sample_size_atom.md)
  An atom you use to specify the size of each sample in the media.
- [Chunk offset atom ('stco')](chunk_offset_atom.md)
  An atom that identifies the location of each chunk of data in the media’s data stream.
- [Sample dependency flags atom ('sdtp')](sample_dependency_flags_atom.md)
  An atom that uses one byte per sample as a bit field that describes dependency information.
- [Using sample atoms](using_sample_atoms.md)
  Find samples or key frames in sample atoms.

## See Also

- [Movie atoms](movie_atoms.md)
  Atoms that act as a container for the information that describes a movie’s data.
- [Track atoms](track_atoms.md)
  Atoms that define a single track of a movie.
- [Media atoms](media_atoms.md)
  Atoms that describe and define a track’s media type and sample data.
- [Structuring movie data and features](structuring_movie_data_and_features.md)
  Build movies with compressed or reference data, and add features like effect descriptions and alternate subtitle tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sample_atoms)*