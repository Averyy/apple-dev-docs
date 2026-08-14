# Movie atoms

**Framework**: QuickTime File Format

Atoms that act as a container for the information that describes a movie’s data.

#### Overview

QuickTime movie atoms have an atom type of `'moov'`. These atoms act as a container for the information that describes a movie’s data. This information, or metadata, is stored in a number of different types of atoms. Generally speaking, only metadata is stored in a movie atom. Sample data for the movie, such as audio or video samples, are referenced in the movie atom, but are not contained in it.

The movie atom is essentially a container of other atoms. These atoms, taken together, describe the contents of a movie. At the highest level, movie atoms typically contain track atoms, which in turn contain media atoms. At the lowest level are the leaf atoms, which contain non-atom data, usually in the form of a table or a set of data elements. For example, a track atom contains an edit atom, which in turn contains an edit list atom, a leaf atom which contains data in the form of an edit list table. All of these atoms are discussed later in this documentation.

The following figures provide a conceptual view of the organization of a simple, one-track QuickTime movie. Each nested box in the illustration represents an atom that belongs to its parent atom. The figure does not show the data regions of any of the atoms. These areas are described in the sections that follow.

![A diagram that shows the structure of a movie atom.](/images/com.apple.qtff/movie-atom@2x.png)

The movie atom contains a track atom, which contains other atoms as detailed in the following figure:

![A diagram that shows the structure of a track atom.](/images/com.apple.qtff/track-atom@2x.png)

The track atom in turn contains a media atom as shown in the following figure:

![A diagram that shows the structure of a media atom.](/images/com.apple.qtff/media-atom@2x.png)

The media atom contains a video media information atom as shown in the following figure:

![A diagram that shows the structure of a video media information atom.](/images/com.apple.qtff/video-media-information-atom@2x.png)

The video media information atom contains a sample table atom as follows:

![A diagram that shows the structure of a sample table atom.](/images/com.apple.qtff/sample-table-atom@2x.png)

Note that the figures show the organization of a standard movie atom. It is possible to compress the movie metadata using a lossless compression algorithm. In such cases, the movie atom contains only a single child atom—the compressed movie atom (`'cmov'`). When this child atom is uncompressed, its contents conform to the structure shown in the following illustration. For details, see [`Compressed movie resources`](compressed_movie_resources.md).

It is also possible to create a reference movie, a movie that refers to other movies; in this case the movie atom may contain only a reference movie atom (`'rmra'`). For details, see [`Reference movies`](reference_movies.md). Ultimately, the chain must end in either a standard movie atom, such as the one in following figure, or a compressed movie atom, which can be uncompressed to obtain the same structure.

## Topics

### Describing movies
- [Movie atom ('moov')](movie_atom.md)
  An atom that specifies the information that defines a movie.
- [Movie header atom ('mvhd')](movie_header_atom.md)
  An atom that specifies the characteristics of an entire QuickTime movie.
- [Color table atom ('ctab')](color_table_atom.md)
  An atom that defines a list of preferred colors for displaying the movie on devices that support only 256 colors.
- [User data atoms](user_data_atoms.md)
  Atoms you use to define and store data associated with a QuickTime object.
- [Interleaving movie data](interleaving_movie_data.md)
  Interleave data in your movie for optimal playback.

## See Also

- [Track atoms](track_atoms.md)
  Atoms that define a single track of a movie.
- [Media atoms](media_atoms.md)
  Atoms that describe and define a track’s media type and sample data.
- [Sample atoms](sample_atoms.md)
  Atoms that describe samples, which are single elements in a sequence of time-ordered data.
- [Structuring movie data and features](structuring_movie_data_and_features.md)
  Build movies with compressed or reference data, and add features like effect descriptions and alternate subtitle tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/movie_atoms)*