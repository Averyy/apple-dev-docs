# Movie atom ('moov')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies the information that defines a movie.

#### Overview

You use movie atoms to specify the information that defines a movie — that is, the information that allows your application to interpret the sample data that is stored elsewhere. The movie atom usually contains a movie header atom, which defines the time scale and duration information for the entire movie, as well as its display characteristics. Existing movies may contain a movie profile atom, which summarizes the main features of the movie, such as the necessary codecs and maximum bit rate. In addition, the movie atom contains a track atom for each track in the movie.

The movie atom has an atom type of `'moov'`. It contains other types of atoms, including at least one of three possible atoms—the movie header atom (`'mvhd'`), the compressed movie atom (`'cmov'`), or a reference movie atom (`'rmra'`). An uncompressed movie atom can contain both a movie header atom and a reference movie atom, but it must contain at least one of the two. It can also contain several other atoms, such as a clipping atom (`'clip'`), one or more track atoms (`'trak'`), a color table atom (`'ctab'`), and a user data atom (`'udta'`).

Compressed movie atoms and reference movie atoms are discussed separately. This section describes normal uncompressed movie atoms.

The layout of movie atom is as follows.

| Data | Type |
| --- | --- |
| [`Size`](movie_atom/size.md) | 4 bytes |
| [`Type`](movie_atom/type.md) = `'moov'` | 4 bytes |
| [`Profile atom`](movie_atom/profile_atom.md) | `'prfl'` |
| [`Movie header atom`](movie_atom/movie_header_atom.md) | `'mvhd'`‡ |
| [`Movie clipping atom`](movie_atom/movie_clipping_atom.md) | `'clip'` |
| One or more [`Track atoms`](movie_atom/track_atoms.md) | `'trak'` |
| [`User data atom`](movie_atom/user_data_atom.md) | `'udta'` |
| [`Color table atom`](movie_atom/color_table_atom.md) | `'ctab'` |
| [`Compressed movie atom`](movie_atom/compressed_movie_atom.md) | `'cmov'` |
| [`Reference movie atom`](movie_atom/reference_movie_atom.md) | `'rmra'` |

‡ denotes required atom.

## Topics

### Data fields
- [Size](movie_atom/size.md)
  The number of bytes in this movie atom.
- [Type](movie_atom/type.md)
  The type of this movie atom.
- [Profile atom](movie_atom/profile_atom.md)
  An atom that summarizes the features and complexity of a movie.
- [Movie header atom](movie_atom/movie_header_atom.md)
  An atom that specifies the characteristics of an entire QuickTime movie.
- [Movie clipping atom](movie_atom/movie_clipping_atom.md)
  An atom that specifies the clipping regions for movies and for tracks.
- [Track atoms](movie_atom/track_atoms.md)
  One or more atoms that define a single track of a movie.
- [User data atom](movie_atom/user_data_atom.md)
  An atom where you define and store data associated with a QuickTime object.
- [Color table atom](movie_atom/color_table_atom.md)
  An atom that defines a list of preferred colors for displaying the movie on devices that support only 256 colors.
- [Compressed movie atom](movie_atom/compressed_movie_atom.md)
  An atom you use to reduce file size and startup latency by compressing movie resources.
- [Reference movie atom](movie_atom/reference_movie_atom.md)
  A reference movie atom contains references to one or more movies.

## See Also

- [Movie header atom ('mvhd')](movie_header_atom.md)
  An atom that specifies the characteristics of an entire QuickTime movie.
- [Color table atom ('ctab')](color_table_atom.md)
  An atom that defines a list of preferred colors for displaying the movie on devices that support only 256 colors.
- [User data atoms](user_data_atoms.md)
  Atoms you use to define and store data associated with a QuickTime object.
- [Interleaving movie data](interleaving_movie_data.md)
  Interleave data in your movie for optimal playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/movie_atom)*