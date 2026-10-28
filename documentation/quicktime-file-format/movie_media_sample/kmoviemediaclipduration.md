# kMovieMediaClipDuration

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A record that indicates the duration of the embedded movie to use.

## Overview

A `MovieMediaTimeRecord` that indicates the duration of the embedded movie that should be used. The clip duration atom is applied by removing media from end of the embedded movie. If the clip duration atom is not present, then no media is removed from the end of the embedded movie. In situations where the sample contains both a clip duration and a clip begin atom, the clip begin is applied first. If the clip duration specifies a value that is larger than the duration of the embedded movie, no change is made to the embedded movie.

## See Also

### Data fields
- [kMovieMediaDataReference](./kmoviemediadatareference.md)
  A data reference type and a data reference.
- [kMovieMediaDefaultDataReferenceID](./kmoviemediadefaultdatareferenceid.md)
  An identifier for the data reference to use when instantiating the embedded movie for this sample.
- [kMovieMediaAutoPlay](./kmoviemediaautoplay.md)
  A Boolean that indicates whether or not the embedded movie starts playing immediately after  instantiation.
- [kMovieMediaLoop](./kmoviemedialoop.md)
  An 8-byte unsigned integer that indicates how the embedded movie should loop.
- [kMovieMediaUseMIMEType](./kmoviemediausemimetype.md)
  Text (not a C string or a pascal string) that indicates the MIME type of the movie import component that should be used to instantiate this media.
- [kMovieMediaTitle](./kmoviemediatitle.md)
  Currently unused.
- [kMovieMediaAltText](./kmoviemediaalttext.md)
  Text (not a C string or a pascal string) that is displayed to the user when the embedded movie is being instantiated or if the embedded movie cannot be instantiated.
- [kMovieMediaClipBegin](./kmoviemediaclipbegin.md)
  A record that indicates the time of the embedded movie to use.
- [kMovieMediaEnableFrameStepping](./kmoviemediaenableframestepping.md)
  A Boolean that indicates whether the embedded movie should be considered when performing step operations.
- [kMovieMediaBackgroundColor](./kmoviemediabackgroundcolor.md)
  A color that is used for filling the background when the movie is being instantiated or when it fails to instantiate.
- [kMovieMediaRegionAtom](./kmoviemediaregionatom.md)
  A number of atoms, which describe how the Movie Media Handler should resize the embedded movie.
- [kMovieMediaRectangleAtom](./kmoviemediarectangleatom.md)
  Four atoms that define a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/movie_media_sample/kmoviemediaclipduration)*