# Track references

**Framework**: QuickTime File Format

Relate a movie’s tracks to one another with track references.

#### Overview

Although QuickTime has always allowed the creation of movies that contain more than one track, it has not been able to specify relationships between those tracks. Track references are a feature of QuickTime that allows you to relate a movie’s tracks to one another. The QuickTime track-reference mechanism supports many-to-many relationships. That is, any movie track may contain one or more track references, and any track may be related to one or more other tracks in the movie.

Track references can be useful in a variety of ways. For example, track references can be used to relate timecode tracks to other movie tracks. You can use track references to identify relationships between video and sound tracks such as identifying the track that contains dialog and the track that contains background sounds. Another use of track references is to associate one or more text tracks that contain subtitles with the appropriate sound track or tracks.

Track references are also used to create chapter lists, as described in [`Chapter lists`](chapter_lists.md).

Every movie track contains a list of its track references. Each track reference identifies another related track. That related track is identified by its track identifier. The track reference itself contains information that allows you to classify the references by type. This type information is stored in an `OSType` data type. You are free to specify any type value you want. Note, however, that Apple has reserved all lowercase type values.

You may create as many track references as you want, and you may create more than one reference of a given type. Each track reference of a given type is assigned an index value. The index values start at `1` for each different reference type. The Movie Toolbox maintains these index values, so that they always start at `1` and count by `1`.

Using the `AddTrackReference` function, you can relate one track to another. The `DeleteTrackReference` function will remove that relationship. The `SetTrackReference` and `GetTrackReference` functions allow you to modify an existing track reference so that it identifies a different track. The `GetNextTrackReferenceType` and `GetTrackReferenceCount` functions allow you to scan all of a track’s track references.

For a list of track reference types, see [`Track reference atoms`](track_reference_atoms.md).

## See Also

- [Modifier tracks](modifier_tracks.md)
  Create dynamic movies with modifier tracks that send data to another track.
- [Creating movies with modifier tracks](creating_movies_with_modifier_tracks.md)
  Send data to another media handler instead of presenting media directly.
- [Chapter lists](chapter_lists.md)
  A chapter list provides a set of named entry points into a movie.
- [Streaming media](streaming_media.md)
  Store streaming data in a streaming media track for QuickTime movies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_references)*