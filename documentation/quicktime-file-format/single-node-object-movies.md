# Single-node object movies

**Framework**: QuickTime File Format

Store a QTVR track, an object track, and an object image track in a single-node object movie.

#### Overview

Every object movie contains at least three tracks: a QTVR track, an object track, and an object image track.

For a single-node object movie, the QTVR track contains just one sample. There is a corresponding sample in the object track, whose time and duration are the same as the time and duration of the sample in the QTVR track. The time base of the movie is used to locate the proper video samples in the object image track.

For an object movie, the frame corresponding to the first row and column in the object image array is located at the same time as the corresponding QTVR and object track samples. The total duration of all the video samples is the same as the duration of the corresponding QTVR sample and the object sample.

In addition to these three required tracks, an object movie can also contain a hot spot image track and any number of standard QuickTime tracks (such as video, sound, and text tracks). A hot spot image track for an object is a QuickTime video track that contains images of regions filled with color delineating the hot spots; an image in the hot spot image track must be synchronized to match the appropriate image in the object image track. A hot spot image track should be 8 bits deep and can be compressed with any lossless compressor (including temporal compressors). This is also true of panoramas.

> **Note**: To assign a single fixed-position hot spot to all views of an object, you should create a hot spot image track that consists of a single video frame whose duration is the entire node time.

To assign a single fixed-position hot spot to all views of an object, you should create a hot spot image track that consists of a single video frame whose duration is the entire node time.

To play a time-based track with the object movie, you must synchronize the sample data of that track to the start and stop times of a view in the object image track. For example, to play a different sound with each view of an object, you might store a sound track in the movie file with each set of sound samples synchronized to play at the same time as the corresponding object’s view image. (This technique also works for video samples.) Another way to add sound or video is simply to play a sound or video track during the object’s view animation; to do this, you need to add an active track to the object that is equal in duration to the object’s row duration.

> ❗ **Important**: In a QuickTime VR movie file, the panorama image tracks and panorama hot spot tracks must be disabled. For an object, the object image tracks must be enabled and the object hot spot tracks must be disabled.

In a QuickTime VR movie file, the panorama image tracks and panorama hot spot tracks must be disabled. For an object, the object image tracks must be enabled and the object hot spot tracks must be disabled.

## See Also

- [Single-node panoramic movies](single-node_panoramic_movies.md)
  Store a QTVR track, a panorama track, and a panorama image track in a single-node panoramic movie.
- [Multinode movies](multinode_movies.md)
  Store any number of object and panoramic nodes in a multinode QuickTime VR movie.
- [Getting the name of a QuickTime VR node](getting_the_name_of_a_quicktime_vr_node.md)
  Retrieve information from a QuickTime VR node with QuickTime atom container functions.
- [Adding custom atoms in a QuickTime VR movie](adding_custom_atoms_in_a_quicktime_vr_movie.md)
  Provide additional information about a QuickTime VR movie using custom atoms.
- [Adding atom containers in a QuickTime VR Movie](adding_atom_containers_in_a_quicktime_vr_movie.md)
  Add node information to your QuickTime VR world.
- [Optimizing QuickTime VR movies for web playback](optimizing_quicktime_vr_movies_for_web_playback.md)
  Prevent having to download an entire movie before starting playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/single-node_object_movies)*