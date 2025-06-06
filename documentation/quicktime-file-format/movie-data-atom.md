# Movie data atom ('mdat')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains movie data.

#### Overview

As with the free and skip atoms, the movie data atom is structured quite simply. It consists of an atom header (atom size and type fields), followed by the movie’s media data. Your application can understand the data in this atom only by using the metadata stored in the movie atom. This atom can be quite large, and may exceed 2^32 bytes, in which case the size field will be set to `1`, and the header will contain a 64-bit extended size field.

## Topics

### Data fields
- [Size](movie_data_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this media data atom.
- [Type](movie_data_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Extended size](movie_data_atom/extended_size.md)
  A 64-bit integer that specifies the number of bytes in this media data atom.
- [Movie media data](movie_data_atom/movie_media_data.md)
  The movie’s media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/movie_data_atom)*