# Image tracks in cubic nodes

**Framework**: QuickTime File Format

Store cubic nodes that represent a panorama.

#### Overview

For a cubic node the image track contains six samples that correspond to the six square faces of the cube. The same applies to hot spot and preview tracks. The following diagram shows how the order of samples in the track corresponds to the orientation of the cube faces.

![A diagram that shows numbered cube faces laid in sample order at the top, numbered 1, 2, 3, 4, 5, and 6. Below that, the diagram shows the layout of cube faces. The first box, on the top left, is labeled 5. Below that, there are four boxes lined up horizontally, labeled 1, 2, 3, and 4. Below that, on the bottom left, there is a box labeled 6.](https://docs-assets.developer.apple.com/published/86228e1b1bd1f7fd0ad06cc77e38fd7c/cubic-node-cube-face%402x.png)

Note that the frames are oriented horizontally. There is no provision for frames that are rotated 90 counterclockwise as there are for cylindrical panoramas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/image_tracks_in_cubic_nodes)*