# Track profile atom ('prfl')

**Framework**: QuickTime File Format  
**Kind**: class

A child atom of movie atoms or track atoms.

## Mentions

- [QuickTime File Format change log](revision_history.md)

#### Overview

Profile atoms can be children of movie atoms or track atoms. For details on profile atoms, see [`Movie profile atom ('prfl')`](movie_profile_atom.md).

## Topics

### Data fields
- [Reserved](track_profile_atom/reserved.md)
  A 32-bit field.
- [Part-ID](track_profile_atom/part-id.md)
  A 32-bit field that defines the feature as being either brand-specific or universal.
- [Feature code](track_profile_atom/feature_code.md)
  A 32-bit unsigned integer that represents a code specifying a feature.
- [Value](track_profile_atom/value.md)
  A 32-bit field that represents a value related to a feature.

## See Also

- [Movie profile atom ('prfl')](movie_profile_atom.md)
  An atom that summarizes the features and complexity of a movie.
- [Appendix F: Profile atom guidelines](appendix_f_profile_atom_guidelines.md)
  Summarize profile information about a QuickTime movie so readers can easily determine features and complexity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_profile_atom)*