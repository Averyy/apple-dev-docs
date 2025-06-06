# Chapter lists

**Framework**: QuickTime File Format

A chapter list provides a set of named entry points into a movie.

#### Overview

A chapter list provides a set of named entry points into a movie, allowing the user to jump to a preselected point in the movie from a convenient pop-up list.

The movie controller automatically recognizes a chapter list and will create a pop-up list from it. When the user makes a selection from the pop-up, the controller will jump to the appropriate point in the movie. Note that if the movie is sized so that the controller is too narrow to display the chapter names, the pop-up list will not appear.

To create a chapter list, you must create a text track with one sample for each chapter. The display time for each sample corresponds to the point in the movie that marks the beginning of that chapter. You must also create a track reference of type `'chap'` from an enabled track of the movie to the text track. It is the `'chap'` track reference that makes the text track into a chapter list. The track containing the reference can be of any type (audio, video, MPEG, and so on), but it must be enabled for the chapter list to be recognized.

Given an enabled track `myVideoTrack`, for example, you can use the `AddTrackReference` function to create the chapter reference:

```c
AddTrackReference( myVideoTrack, theTextTrack,
    kTrackReferenceChapterList,
    &addedIndex );
```

`kTrackReferenceChapterList` is defined in `Movies.h`. It has the value `'chap'`.

The text track that constitutes the chapter list does not need to be enabled, and normally is not. If it is enabled, the text track will be displayed as part of the movie, just like any other text track, in addition to functioning as a chapter list.

If more than one enabled track includes a `'chap'` track reference, QuickTime uses the first chapter list that it finds.

## See Also

- [Modifier tracks](modifier_tracks.md)
  Create dynamic movies with modifier tracks that send data to another track.
- [Creating movies with modifier tracks](creating_movies_with_modifier_tracks.md)
  Send data to another media handler instead of presenting media directly.
- [Track references](track_references.md)
  Relate a movie’s tracks to one another with track references.
- [Streaming media](streaming_media.md)
  Store streaming data in a streaming media track for QuickTime movies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/chapter_lists)*