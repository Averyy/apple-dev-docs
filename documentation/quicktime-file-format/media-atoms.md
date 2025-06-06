# Media atoms

**Framework**: QuickTime File Format

Atoms that describe and define a track’s media type and sample data.

#### Overview

The media atom contains information that specifies:

- The media type, such as sound, video or timed metadata
- The media handler component used to interpret the sample data
- The media timescale and track duration
- Media-and-track-specific information, such as sound volume or graphics mode
- The media data references, which typically specify the file where the sample data is stored
- The sample table atoms, which, for each media sample, specify the sample description, duration, and byte offset from the data reference

## Topics

### Describing media
- [Media atom ('mdia')](media_atom.md)
  An atom that describes and defines a track’s media type and sample data.
- [Media header atom ('mdhd')](media_header_atom.md)
  An atom that specifies the characteristics of a media, including time scale and duration.
- [Extended language tag atom ('elng')](extended_language_tag_atom.md)
  An atom that represents media language information.
- [Handler reference atom ('hdlr')](handler_reference_atom.md)
  An atom that specifies the media handler component that is to be used to interpret the media’s data.
- [Media information atoms](media_information_atoms.md)
  An atom that contains a number of other atoms that define specific characteristics of the video media data.
- [Video media information atom ('minf')](video_media_information_atom.md)
  An atom that contains a number of other atoms that define specific characteristics of the video media data.
- [Video media information header atom ('vmhd')](video_media_information_header_atom.md)
  An atom that defines specific color and graphics mode information.
- [Sound media information atom ('minf')](sound_media_information_atom.md)
  An atom that contains a number of other atoms that define specific characteristics of the sound media data.
- [Sound media information header atom ('smhd')](sound_media_information_header_atom.md)
  An atom that stores the sound media’s control information, such as balance.
- [Base media information atom ('minf')](base_media_information_atom.md)
  An atom that stores the media information for media types such as timed metadata, text, MPEG, time code, and music.
- [Base media information header atom ('gmhd')](base_media_information_header_atom.md)
  An atom that indicates that this media information atom pertains to a base media.
- [Base media info atom ('gmin')](base_media_info_atom.md)
  An atom that defines the media’s control information, including graphics mode and balance information.
- [Data information atom ('dinf')](data_information_atom.md)
  An atom that specifies the data handler component that provides access to the media data.
- [Media data reference atom ('dref')](media_data_reference_atom.md)
  An atom that contains tabular data that instructs the data handler component how to access the media’s data.

## See Also

- [Movie atoms](movie_atoms.md)
  Atoms that act as a container for the information that describes a movie’s data.
- [Track atoms](track_atoms.md)
  Atoms that define a single track of a movie.
- [Sample atoms](sample_atoms.md)
  Atoms that describe samples, which are single elements in a sequence of time-ordered data.
- [Structuring movie data and features](structuring_movie_data_and_features.md)
  Build movies with compressed or reference data, and add features like effect descriptions and alternate subtitle tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/media_atoms)*