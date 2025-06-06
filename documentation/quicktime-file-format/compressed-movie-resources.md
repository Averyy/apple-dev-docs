# Compressed movie resources

**Framework**: QuickTime File Format

Reduce file size and startup latency by compressing movie resources.

#### Overview

Most QuickTime movies have metadata in addition to their media data. Media data can be compressed using a variety of video and sound compression algorithms. Beginning with QuickTime 3, it also became possible to compress the metadata—more commonly known as the movie resource. However, the movie resource cannot be compressed by means of a lossy compression algorithm because it contains critical information, such as the video and audio compression types used, individual frame offsets, and timing information. To compress the movie resource, therefore, lossless data compression algorithms must be used.

Compressing movie resources using data compression typically reduces the size of the movie resource by 50% or more. For QuickTime movies that are streamed over the Internet, this can substantially reduce the startup latency of the movie, and therefore has a number of distinct advantages.

#### Allowing Quicktime to Compress the Movie Resource

Most application developers won’t need to know the details of how movie resources are compressed. The Movie Toolbox `FlattenMovie` and `FlattenMovieData` functions compress the movie resource if so requested by the application. To accomplish this, applications only need to set the `flattenCompressMovieResource` flag when calling either function. The QuickTime movie export component also provides users with the option of compressing the movie resource when exporting or creating a new movie through export.

#### Structure of a Compressed Movie Resource

A compressed movie resource, similar to an uncompressed movie resource, is made up of a group of QuickTime atoms arranged in a hierarchy.

Like an uncompressed movie resource, the outermost atom is a movie atom. Within the movie atom, there is a single compressed movie atom, which contains all other required atoms. The compressed movie atom has two sub atoms. The first is a data compression atom, which contains a single 32-bit integer that identifies what lossless data compression algorithm was used to compress the movie resource. The second child atom is the compressed movie data, which contains the compressed movie resource itself. The first 32-bit integer in the compressed movie data atom indicates the uncompressed size of the movie resource, and then the compressed movie resource data follows.

The contents of a complete compressed movie are shown in the table below. The constants that define the atom types are defined in `MoviesFormat.h`. The four-character codes for each atom type are also shown.

| Atom type | Four-character code |
| --- | --- |
| Movie | `'moov'` |
| Compressed movie | `'cmov'` |
| Data compression atom | `'dcom'` |
| Compressed movie data | `'cmvd'` |
| 32-bit integer | Uncompressed size |

## See Also

- [Reference movies](reference_movies.md)
  A movie that contains references to alternate movies is called a reference movie.
- [Authoring movies with external movie targets](authoring_movies_with_external_movie_targets.md)
  Specify elements of an external movie in your movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/compressed_movie_resources)*