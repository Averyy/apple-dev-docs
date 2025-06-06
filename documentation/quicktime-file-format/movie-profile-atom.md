# Movie profile atom ('prfl')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that summarizes the features and complexity of a movie.

**Availability**:
- Unknown ?+ - Deprecated

## Mentions

- [QuickTime File Format change log](revision_history.md)

#### Overview

The movie profile atom summarizes the features and complexity of a movie, such as the required codecs and maximum bit rate, in order to help player applications or devices quickly determine whether they have the necessary resources to play the movie.

Features for a movie typically include the movie’s maximum video and audio bit rate, a list of audio and video codec types, the movie’s video dimensions, and any applicable MPEG-4 profiles and levels. This is all information that can also be obtained by examining the contents of the movie file in more detail. This summary is intended to allow applications or devices to quickly determine whether they can play the movie. It is not intended as a container for information that is not found elsewhere in the movie, and should not be used as one.

> **Note**: The fact that a feature does not appear in the profile atom does not mean it is not present in the movie. The profile atom itself may not be present, or may list only a subset of movie features. The features listed in the profile atom are all present, but the list is not necessarily complete.

The fact that a feature does not appear in the profile atom does not mean it is not present in the movie. The profile atom itself may not be present, or may list only a subset of movie features. The features listed in the profile atom are all present, but the list is not necessarily complete.

When creating a profile atom, it is permissible to omit some features that are present in the movie, but it is required to fully specify any features that are included in the profile. For example, a movie containing video may or may not have a video codec type feature in the profile atom, but if any video codec type feature is included in the profile atom, every required video codec must be listed in the profile atom.

The movie profile atom is a profile atom (`'prfl'`) whose parent is a movie atom. This is distinct from the track profile atom, whose parent is a track atom. The structure of the profile atom is identical in both cases, but the contents of a movie profile atom describe the movie as a whole, while the contents of a track profile atom are specific to a particular track.

The profile atom contains a list of features. In a movie profile atom, these features summarize the movie as a whole. In a track profile atom, these features describe a particular track.

For details on the structure and contents of profile atoms, see [`Appendix F: Profile atom guidelines`](appendix_f_profile_atom_guidelines.md).

## Topics

### Data fields
- [Reserved](movie_profile_atom/reserved.md)
  A 32-bit field.
- [Part-ID](movie_profile_atom/part-id.md)
  A 32-bit field that defines the feature as being either brand-specific or universal.
- [Feature code](movie_profile_atom/feature_code.md)
  A 32-bit unsigned integer that represents a code specifying a feature.
- [Value](movie_profile_atom/value.md)
  A 32-bit field that represents a value related to a feature.

## See Also

- [Track profile atom ('prfl')](track_profile_atom.md)
  A child atom of movie atoms or track atoms.
- [Appendix F: Profile atom guidelines](appendix_f_profile_atom_guidelines.md)
  Summarize profile information about a QuickTime movie so readers can easily determine features and complexity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/movie_profile_atom)*