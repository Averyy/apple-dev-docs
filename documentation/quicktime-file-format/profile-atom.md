# Profile atom ('prfl')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that expresses profiles or feature codes for features that occur in the movie.

#### Overview

At the movie level, the profile atom must occur within the movie atom before the movie header atom. A reader may stop the search for the profile atom once the profile atom or the movie header atom is found. Because new atoms may be introduced into the movie atom (type `'moov'`) in the future, a reader must not expect the first child atom of the movie atom to be either the profile (type `'prfl'`) or the movie header (`'mvhd'`) atom. This rule allows for new atoms in the future but still accommodates readers that do not want to perform an exhaustive enumeration of all the child atoms in a movie atom.

The profile atom expresses profiles or feature codes for features that occur in the movie. The list is not necessarily exhaustive, and there may be multiple profile values recorded for the same profile code. For example, if there are two independent sequences of MPEG-4 video in the movie, using different profile-level IDs, both might be recorded here.

Each feature is either universal or is documented in a specific specification, identified by a brand as used in the file type atom. The only brands that should occur in a given profile atom are the universal brand or brands that occur in the file type atom in the same file.

Feature value ranges should in general never include an unknown point; if the value of a feature is unknown, the feature should be absent from the profile atom.

Feature values should be deducible by fairly simple inspection of the rest of the movie: for example, extracting the profile-level ID from a video header, or calculations using information from the sample table (for example, overall average bit rate by summing the sample sizes and the sample durations). It is not appropriate to have features which cannot be computed, or only computed with difficulty (e.g. a buffer model estimation which requires emulating a video decoder on the entire bit stream). The algorithm to extract or deduce the feature value from the rest of the file must be defined.

Empty slots in the profile atom structure must be filled with zeroes.

If there are multiple parts of the file to which the same feature apply, yet they have different feature values, then either there must be entries for each occurrence or none at all. For example, if there are two MPEG-4 visual sequences, using different visual profiles, there are either two profile entries in the profile table (one for each sequence) or none at all. Features must not be partially documented.

Profile atoms may also occur at the track level. A track-level profile atom must occur within the track atom before the track header atom (`'tkhd'`). A reader should stop searching for a track’s profile atom if either the profile or the track header atom is found, ignoring any other atoms present.

A track profile atom should only summarize features within that track. If track profile atoms exist, a movie profile atom can be built largely by copying feature entries from the profile atom of the movie’s tracks to the profile atom at the movie level. It is possible to have multiple track profiles with different values which must be resolved to a single value for the movie as whole, however—such as multiple video tracks with different maximum bit rates—so not all features can be copied directly from the track to the movie profile. Additionally, the movie profile may summarize features that cannot occur at the track level, such as total movie bit rate.

When building a movie profile, you must include either all instances of a track-level feature or no instances of that feature. For example, if you have multiple video tracks that use different codecs, you must either include an entry at the movie level for each codec, or put no codec feature entries at the movie level at all.

The following table shows the layout of the profile atom.

| Data field | Bytes |
| --- | --- |
| [`Size`](profile_atom/size.md) | 4 |
| [`Type`](profile_atom/type.md) = `'prfl'` | 4 |
| [`Version`](profile_atom/version.md) | 1 |
| [`Flags`](profile_atom/flags.md) | 3 |
| [`Number of feature entries`](profile_atom/number_of_feature_entries.md) | 4 |
| [`Feature entries`](profile_atom/feature_entries.md) | `n` x 32 |

#### Syntax

```c
aligned(8) class ProfileAtom
    extends FullAtom('prfl') {
    unsigned int(32) feature-record-count;
    for (i=1; i<feature-record-count; i++) {
        unsigned int(32) reserved = 0;
        unsigned int(32) part-ID;
        unsigned int(32) feature-code;
        unsigned int(32) feature-value
    }
}
```

#### Semantics

The profile atom is a full atom, so it has an 8-bit version and 24 bits of flags. For this specification, the version is `0` and the flags have the value `0`. A reader compliant with this specification should treat any profile atom with a nonzero version value as if it did not exist.

For more information on setting feature entries, see [`Feature entries`](profile_atom/feature_entries.md).

## Topics

### Data fields
- [Size](profile_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this atom.
- [Type](profile_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](profile_atom/version.md)
  An 8-bit integer that holds the version.
- [Flags](profile_atom/flags.md)
  An 8-bit integer with flags.
- [Number of feature entries](profile_atom/number_of_feature_entries.md)
  A 32-bit integer that indicates how many feature entries are in the atom.
- [Feature entries](profile_atom/feature_entries.md)
  A list of feature entries.

## See Also

- [About this appendix](about_this_appendix.md)
- [Universal features](universal_features.md)
  Features that you include in any file that includes a profile atom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/profile_atom)*