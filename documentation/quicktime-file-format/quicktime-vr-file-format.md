# QuickTime VR file format

**Framework**: QuickTime File Format

A file format used to store a QuickTime VR movie on disk.

#### Overview

> ❗ **Important**: VR Media is deprecated in the QuickTime file format. The information that follows documents existing content containing VR Media and should not be used for new development.

A QuickTime VR movie is stored on disk in a format known as the QuickTime VR file format. Beginning in QuickTime VR 2.0, a QuickTime VR movie could contain one or more nodes. Each node is either a panorama or an object. In addition, a QuickTime VR movie could contain various types of hot spots, including links between any two types of nodes.

> ❗ **Important**: This section describes the file format supported by version 2.1 of the QuickTime VR Manager.

All QuickTime VR movies contain a single QTVR track, a special type of QuickTime track that maintains a list of the nodes in the movie. Each individual sample in a QTVR track contains general information and hot spot information for a particular node.

If a QuickTime VR movie contains any panoramic nodes, that movie also contains a single panorama track, and if it contains any object nodes, it also contains a single object track. The panorama and object tracks contain information specific to the panoramas or objects in the movie. The actual image data for both panoramas and objects is usually stored in standard QuickTime video tracks, hereafter referred to as image tracks. (An image track can also be any type of track that is capable of displaying an image, such as a QuickTime 3D track.) The individual frames in the image track for a panorama make up the diced frames of the original single panoramic image. The frames for the image track of an object represent the many different views of the object. Hot spot image data is stored in parallel video tracks for both panoramas and objects.

## Topics

### Storing QuickTime VR files
- [Single-node panoramic movies](single-node_panoramic_movies.md)
  Store a QTVR track, a panorama track, and a panorama image track in a single-node panoramic movie.
- [Single-node object movies](single-node_object_movies.md)
  Store a QTVR track, an object track, and an object image track in a single-node object movie.
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

## See Also

- [Sprite media](sprite_media.md)
  Sprite media is used to store character-based animation data in QuickTime movies.
- [Sprite track properties](sprite_track_properties.md)
  Define properties that apply to an entire sprite track.
- [Sprite track media format](sprite_track_media_format.md)
  A media format for that stores sprite track information in atoms.
- [Sprite media atom and data types](sprite_media_atom_and_data_types.md)
  Atoms that represent sprite media and data types.
- [Sprite button behaviors](sprite_button_behaviors.md)
  Specify simple button behaviors for sprites in a sprite track.
- [QT atom container description key](qt_atom_container_description_key.md)
  Build QT atom container-based data structures.
- [Sprite media handler track properties QT atom container format](sprite_media_handler_track_properties_qt_atom_container_format.md)
  Set sprite media handler track properties in a QT atom container.
- [Sprite media handler sample QT atom container formats](sprite_media_handler_sample_qt_atom_container_formats.md)
  Set sprite media handlers in QT atom containers.
- [Wired action grammar](wired_action_grammar.md)
  Embed QT event handlers in their media samples.
- [Tween media](tween_media.md)
  Store pairs of values to be interpolated between in QuickTime movies using tween media.
- [3D media](3d_media.md)
  Store 3D image data in a base media in QuickTime movies.
- [VR media](vr_media.md)
  Atoms that describe the QuickTime VR world.
- [Node parent atom](node_parent_atom.md)
  An atom that is the parent of one or more node ID atoms.
- [Node location atom structure ('nloc')](node_location_atom_structure.md)
  An atom that describes the type of a node and its location.
- [Custom cursor atom](custom_cursor_atom.md)
  An atom you use to replace the default cursors used by QuickTime VR.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/quicktime_vr_file_format)*