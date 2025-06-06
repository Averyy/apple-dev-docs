# Modifier tracks

**Framework**: QuickTime File Format

Create dynamic movies with modifier tracks that send data to another track.

#### Overview

The addition of modifier tracks in QuickTime 2.1 introduced the capability for creating dynamic movies. (A modifier track sends data to another track; by comparison, a track reference is an association.) For example, instead of playing video in a normal way, a video track could send its image data to a sprite track. The sprite track then could use that video data to replace the image of one of its sprites. When the movie is played, the video track appears as a sprite.

Modifier tracks are not a new type of track. Instead, they are a new way of using the data in existing tracks. A modifier track does not present its data, but sends it to another track that uses the data to modify how it presents its own data. Any track can be either a sender or a presenter, but not both. Previously, all tracks were presenters.

Another use of modifier tracks is to store a series of sound volume levels, which is what occurs when you work with a tween track. These sound levels can be sent to a sound track as it plays to dynamically adjust the volume. A similar use of modifier tracks is to store location and size information. This data can be sent to a video track to cause it to move and resize as it plays.

Because a modifier track can send its data to more than one track, you can easily synchronize actions between multiple tracks. For example, a single modifier track containing matrices as its samples can make two separate video tracks follow the same path.

See [`Creating movies with modifier tracks`](creating_movies_with_modifier_tracks.md) for more information about using modifier tracks.

#### Limitations of Spatial Modifier Tracks

A modifier track may cause a track to move outside of its original boundary regions. This may present problems, since applications do not expect the dimensions or location of a QuickTime movie to change over time.

To ensure that a movie maintains a constant location and size, the Movie Toolbox limits the area in which a spatially modified track can be displayed. A movie’s “natural” shape is defined by the region returned by the `GetMovieBoundsRgn` function. The toolbox clips all spatially modified tracks against the region returned by `GetMovieBoundsRgn`. This means that a track can move outside of its initial boundary regions, but it cannot move beyond the combined initial boundary regions of all tracks in the movie. Areas uncovered by a moving track are handled by the toolbox in the same way as areas uncovered by tracks with empty edits.

If a track has to move through a larger area than that defined by the movie’s boundary region, the movie’s boundary region can be enlarged to any desired size by creating a spatial track (such as a video track) of the desired size but with no data. As long as the track is enabled, it contributes to the boundary regions of the movie.

## See Also

- [Creating movies with modifier tracks](creating_movies_with_modifier_tracks.md)
  Send data to another media handler instead of presenting media directly.
- [Track references](track_references.md)
  Relate a movie’s tracks to one another with track references.
- [Chapter lists](chapter_lists.md)
  A chapter list provides a set of named entry points into a movie.
- [Streaming media](streaming_media.md)
  Store streaming data in a streaming media track for QuickTime movies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/modifier_tracks)*