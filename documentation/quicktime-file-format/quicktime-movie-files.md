# QuickTime movie files

**Framework**: QuickTime File Format

The QuickTime file format describes the characteristics of QuickTime movie files.

#### Overview

A QuickTime movie file contains a QuickTime movie resource, or else points to one or more external sources using movie references. The media samples used by the movie (such as video frames or groups of audio samples) may be included in the movie file, or may be external to the movie file in one or more files, streams, or other sources.

A QuickTime movie is not limited to video and audio; it may use any subset or combination of media types that QuickTime supports, including video, sound, still images, text, Flash, 3D models, and virtual reality panoramas. It supports both time-based and nonlinear interactive media.

In file systems that support filename extensions, QuickTime movie files should have an extension of `.mov`. On the Macintosh platform, QuickTime files have a Mac OS file type of `'MooV'`. QuickTime movie files should always be associated with the MIME type `"video/quicktime"`, whether or not the movie contains video.

> **Note**: The use of resource forks for the storage of QuickTime media is deprecated in the QuickTime file format. The information below documents existing content and should not be used for new development. In file systems that support both a resource fork and a data fork, the movie resource may be contained in the resource fork. The default, however, is for the movie resource to be contained in the data fork for all file systems. If media sample data is included in the movie file, it is always in the data fork.

A QuickTime movie file is structured as a collection of atoms that together identify the file as a QuickTime movie, describe the structure of the movie, and may contain the sample data needed to play the movie. Not all atoms are required.

The file format is extensible, and from time to time new atom types are introduced. If your application encounters an unknown atom type in a QuickTime file, it should simply ignore it. This allows the file format to be extended without breaking existing applications, and provides a measure of forward compatibility. Because the first field in any atom contains its size, including any contained atoms, it is easy to skip to the end of an unknown atom type and continue parsing the file.

> ❗ **Important**: Generally speaking, atoms can be present in any order. Do not conclude that a particular atom is not present until you have parsed all the atoms in the file.

An exception is the file type atom, which typically identifies the file as a QuickTime movie. If present, this atom precedes any movie atom, movie data, preview, or free space atoms. If you encounter one of these other atom types prior to finding a file type atom, you may assume the file type atom is not present. (This atom is introduced in the  for 2004, and is not present in QuickTime movie files created prior to 2004).

While other atoms can be in any order, unless specified in this documentation, for practical reasons there is a recommended order that you should use when creating a QuickTime movie file. For example, the atom containing the movie resource should precede any atoms containing the movie’s sample data. If you follow this recommended atom order, it is possible to play a movie over a network while the movie file is in the process of downloading.

A QuickTime movie file must contain a movie atom, which contains either the movie structure or a reference to one or more alternate movie sources external to the file. Generally speaking, these alternate sources will be QuickTime movie files that contain movie structures.

A QuickTime movie file typically contains one or more movie data atoms, which contain media sample data such as video frames and groups of audio samples. There may be no movie data atoms in the file, however, as the movie may depend on sample data external to the movie file, such as external data files or live streams on the Internet. A single movie data atom may contain sample data for a variety of different media. Generally speaking, it is possible to contain all the media samples used by a movie in a single movie data atom. Movie data atoms can be quite large, and sometimes exceed 2^32 bytes.

The following figure shows the essential atom types in a QuickTime movie file within which other atoms are stored. In addition, the file may contain free space atoms, preview atoms, and other atoms not enumerated in this file format specification. Unknown atom types should be ignored.

![The structure of a QuickTime movie file.](https://docs-assets.developer.apple.com/published/72054fb3cc6f4cd8bffcd14d1797cb7d/quicktime-movie-file-structure%402x.png)

The following table lists the basic atom types.

| Atom type | Use |
| --- | --- |
| `'ftyp'` | File type compatibility—identifies the file type and differentiates it from similar file types, such as MPEG-4 files and JPEG-2000 files. |
| `'moov'` | Movie resource metadata about the movie (number and type of tracks, location of sample data, and so on). Describes where the movie data can be found and how to interpret it. |
| `'mdat'` | Movie sample data—media samples such as video frames and groups of audio samples. Usually this data can be interpreted only by using the movie resource. |
| `'free'` | Unused space available in file. |
| `'skip'` | Unused space available in file. |
| `'wide'` | Reserved space—can be overwritten by an extended size field if the following atom exceeds 2^32 bytes, without displacing the contents of the following atom. |
| `'pnot'` | Reference to movie preview data. |

The following sections describe these basic atom types (except for the movie atom) in more detail, including descriptions of other atoms that each basic atom may contain. The movie atom is described separately in Movie Atoms.

## Topics

### Declaring compatibility
- [File type compatibility atom ('ftyp')](file_type_compatibility_atom.md)
  An atom that identifies the file type specifications with which the file is compatible.
### Setting free space
- [Free space atom ('free')](free_space_atom.md)
  An atom that designates unused space in the movie data file.
- [Skip atom ('skip')](skip_atom.md)
  An atom that designates unused space in the movie data file.
- [Wide atom ('wide')](wide_atom.md)
  An atom that designates reserved space in the movie data file.
### Describing movie data
- [Movie data atom ('mdat')](movie_data_atom.md)
  An atom that contains movie data.
### Describing preview information
- [Preview atom ('pnot')](preview_atom.md)
  An atom that contains information that allows you to find the preview image associated with a QuickTime movie.

## See Also

- [Atoms](atoms.md)
  The basic data unit in a QuickTime file is the atom.
- [QT atoms and atom containers](qt_atoms_and_atom_containers.md)
  An enhanced data structure that provide a more general-purpose storage format.
- [Creating, copying, and disposing of atom containers](creating_copying_and_disposing_of_atom_containers.md)
  Manage atoms in atom containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/quicktime_movie_files)*