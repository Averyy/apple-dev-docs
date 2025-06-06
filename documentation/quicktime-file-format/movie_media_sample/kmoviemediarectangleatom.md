# kMovieMediaRectangleAtom

**Framework**: QuickTime File Format  
**Kind**: property

Four atoms that define a rectangle.

#### Overview

Not all atoms must be present: top and left must both appear together, width and height must both appear together. The dimensions contained in this rectangle are used in place of the track box when applying the contents of the spatial adjustment atom. If the top and left are not specified, the top and left of the containing track’s box are used. If the width and height are not specified, the width and height of the containing track’s box are used. Each atom contains a `UInt32`.

## See Also

- [kMovieMediaDataReference](movie_media_sample/kmoviemediadatareference.md)
  A data reference type and a data reference.
- [kMovieMediaDefaultDataReferenceID](movie_media_sample/kmoviemediadefaultdatareferenceid.md)
  An identifier for the data reference to use when instantiating the embedded movie for this sample.
- [kMovieMediaAutoPlay](movie_media_sample/kmoviemediaautoplay.md)
  A Boolean that indicates whether or not the embedded movie starts playing immediately after  instantiation.
- [kMovieMediaLoop](movie_media_sample/kmoviemedialoop.md)
  An 8-byte unsigned integer that indicates how the embedded movie should loop.
- [kMovieMediaUseMIMEType](movie_media_sample/kmoviemediausemimetype.md)
  Text (not a C string or a pascal string) that indicates the MIME type of the movie import component that should be used to instantiate this media.
- [kMovieMediaTitle](movie_media_sample/kmoviemediatitle.md)
  Currently unused.
- [kMovieMediaAltText](movie_media_sample/kmoviemediaalttext.md)
  Text (not a C string or a pascal string) that is displayed to the user when the embedded movie is being instantiated or if the embedded movie cannot be instantiated.
- [kMovieMediaClipBegin](movie_media_sample/kmoviemediaclipbegin.md)
  A record that indicates the time of the embedded movie to use.
- [kMovieMediaClipDuration](movie_media_sample/kmoviemediaclipduration.md)
  A record that indicates the duration of the embedded movie to use.
- [kMovieMediaEnableFrameStepping](movie_media_sample/kmoviemediaenableframestepping.md)
  A Boolean that indicates whether the embedded movie should be considered when performing step operations.
- [kMovieMediaBackgroundColor](movie_media_sample/kmoviemediabackgroundcolor.md)
  A color that is used for filling the background when the movie is being instantiated or when it fails to instantiate.
- [kMovieMediaRegionAtom](movie_media_sample/kmoviemediaregionatom.md)
  A number of atoms, which describe how the Movie Media Handler should resize the embedded movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/movie_media_sample/kmoviemediarectangleatom)*