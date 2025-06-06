# Appendix F: Profile atom guidelines

**Framework**: QuickTime File Format

Summarize profile information about a QuickTime movie so readers can easily determine features and complexity.

#### Overview

> ❗ **Important**: Profile atoms are deprecated in the QuickTime file format. The information that follows documents existing content containing profile atoms and should not be used for new development.

Profile atoms are deprecated in the QuickTime file format. The information that follows documents existing content containing profile atoms and should not be used for new development.

This section introduces and defines some of the ways that profile information about a QuickTime movie file can be summarized in a profile atom near the beginning of the file, so that software reading the file can easily determine some aspects of its features and complexity.

The information in this section should not be seen as a replacement for, or even a functional overlap with, the definition of the file-type atom. The file-type atom expresses which specifications a file is compatible with: reading software should not attempt to play files unless they are compatible with one or more specifications the reader implements, and should not refuse to play a file if it is marked as so compatible. However, reading software may use profiling information to issue warnings, request user decisions, and so on.

Reading software should not present excessive warnings to the user in the absence of summarized features. Additionally, readers are encouraged to try to play content even though crucial profile information is missing or incomplete.

Profiles may exist at the movie level or the track level. Track-level profiles summarize features of that track only. Movie-level profiles may summarize features across tracks or summarize features that are only relevant at the movie level (for example, the movie’s maximum bit rate).

If the movie contains runtime variables that might affect a feature, such as the presence of alternate tracks that would affect the movie bit-rate, the affected feature should either be absent or report the worst case (for example, the highest bit-rate).

If a feature value cannot be accurately represented (for example, the value is not an integer, but the field is formatted as an integer) then the value should be rounded up to the nearest representable value.

## Topics

### Building a profile atom
- [About this appendix](about_this_appendix.md)
- [Profile atom ('prfl')](profile_atom.md)
  An atom that expresses profiles or feature codes for features that occur in the movie.
- [Universal features](universal_features.md)
  Features that you include in any file that includes a profile atom.

## See Also

- [Movie profile atom ('prfl')](movie_profile_atom.md)
  An atom that summarizes the features and complexity of a movie.
- [Track profile atom ('prfl')](track_profile_atom.md)
  A child atom of movie atoms or track atoms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/appendix_f_profile_atom_guidelines)*