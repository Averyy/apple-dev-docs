# Reference movies

**Framework**: Quicktime File Format

A movie that contains references to alternate movies is called a reference movie.

#### Overview

A QuickTime movie can act as a container for a set of alternate movies to display under specific conditions. One of these movies may be contained within the same file; any others are included by reference.

For example, a QuickTime movie can contain a list of references to movies having different data rates, allowing an application to choose the best-looking movie that can play smoothly as it downloads over the Internet, based on the user’s connection speed.

A movie that contains references to alternate movies is called a reference movie.

A reference movie contains a reference movie atom (`'rmra'`) at the top level of the movie atom. The movie atom may also contain a movie header atom, or it may contain the reference movie atom alone.

The reference movie atom contains one or more reference movie descriptor atoms, each of which describes an alternate movie.

Each reference movie descriptor atom contains a data reference atom, which specifies the location of a movie.

> **Note**: Movie locations are specified using QuickTime data references. QuickTime supports multiple types of data reference, but alternate movies are generally specified using data reference types of either url (`'url '`) or file alias (`'alis'`).

A reference movie descriptor atom may contain other atoms that specify the movie’s system requirements and the movie quality. If so, there will be an atom of an appropriate type for each requirement that must be met for the movie to play, and there may be a quality atom as well.

Applications play the highest-quality movie whose requirements are met by the user’s system. If the data reference to the selected movie cannot be resolved — because the file cannot be found, for example — the application recursively attempts to play the next-highest-quality movie until it succeeds or has exhausted the list of movies whose requirements are met.

If a movie contains both a reference movie atom and a movie header atom, applications play the appropriate movie indicated by the reference movie atom.

If the user’s system does not meet any of the alternate movies’ criteria, or none of the qualifying data references can be resolved, applications play the movie defined in the movie header atom. (The movie defined in the movie header atom can also be indicated by one of the alternate movie references.)

The movie header atom is sometimes used to provide a fallback movie for applications that can play older QuickTime movies but do not understand reference movies.

When parsing a reference movie, treat the URL or file reference in the reference movie atom as a new starting point, making no assumptions that the reference is a valid URL, or an existing file, or a well-formed and playable QuickTime movie.

## Topics

### Describing reference movies
- [Reference movie atom ('rmra')](reference_movie_atom.md)
  A reference movie atom contains references to one or more movies.
- [Reference movie descriptor atom ('rmda')](reference_movie_descriptor_atom.md)
  An atom that contains other atoms that describe where to find a particular movie, the system requirements to play that movie, and a quality rating.
- [Reference movie data reference atom ('rdrf')](reference_movie_data_reference_atom.md)
  An atom that contains the information necessary to locate a movie, stream or file.
- [Data rate atom ('rmdr')](data_rate_atom.md)
  A data rate atom specifies the minimum data rate required to play a movie.
- [CPU speed atom ('rmcs')](cpu_speed_atom.md)
  A CPU speed atom specifies the minimum computing power needed to display a movie.
- [Version check atom ('rmvc')](version_check_atom.md)
  A version check atom specifies a software package, such as QuickTime or QuickTime VR, and the version of that package needed to display a movie.
- [Component detect atom ('rmcd')](component_detect_atom.md)
  A component detect atom specifies a QuickTime component, such as a particular video decompressor, required to play the movie.
- [Movie importer component flags](movie_importer_component_flags.md)
  Flags that adjust the behavior of the movie import component.
- [Quality atom ('rmqu')](quality_atom.md)
  A quality atom describes the relative quality of a movie.

## See Also

- [Compressed movie resources](compressed_movie_resources.md)
  Reduce file size and startup latency by compressing movie resources.
- [Authoring movies with external movie targets](authoring_movies_with_external_movie_targets.md)
  Specify elements of an external movie in your movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/reference_movies)*