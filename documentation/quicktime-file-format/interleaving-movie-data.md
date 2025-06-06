# Interleaving movie data

**Framework**: QuickTime File Format

Interleave data in your movie for optimal playback.

#### Overview

In order to get optimal movie playback, you must create the movie with interleaved data. Because the data for the movie is placed on disk in time order, the data for a particular time in the movie is close together in the file. This means that you must intersperse the data from different tracks. To illustrate this, consider a movie with a single video and a single sound track.

The following figure shows how the movie data was collected, and how the data would need to be played back for proper synchronization. In this example, the video data is recorded at 10 frames per second and the audio data is grouped into half-second chunks.

![A diagram that shows one horizontal bar representing video frames above another horizontal bar representing an audio track. The video bar is divided into smaller sections representing frames. The audio bar is divided into smaller sections representing half-second chunks, with each chunk numbered from one to seven. Stretching across the bars are three equidistant vertical lines. Below the bars are labels representing seconds. The first vertical line crosses the video bar with a label indicating 10 frames; it crosses the audio bar at the end of the second chunk, and has a Seconds label “1”. The second vertical line crosses the video bar with a label indicating 20 frames; it crosses the audio bar at the end of the fourth chunk, and has a Seconds label “2”. The third vertical line crosses the video bar with a label indicating 30 frames; it crosses the audio bar at the end of the sixth chunk, and has a Seconds label “3”.](https://docs-assets.developer.apple.com/published/409adbd73088b7c00238d9fc7d1bf90e/non-interleaved-movie-data%402x.png)

After the data has been interleaved on the disk, the movie data atom would contain movie data in the order shown in the following figure.

![A diagram that shows a small, empty section on the left with a caption “‘moov’”, and a larger section on the right with the caption “‘mdat’” and a horizontal bar. The horizontal bar is divided into sections. The first two sections starting from the left represent audio chunks, and have the numbers 1 and 2. The next five sections represent video tracks, numbered 1 through 5. The next section represents an audio chunk with the number 3. The next five sections represent video tracks, numbered 6 through 10. The next section represents an audio chunk with the number 34. The next five sections represent video tracks, numbered 11 through 15.](https://docs-assets.developer.apple.com/published/c96e97b3f2bfc410aaa63d028a47dab7/interleaved-movie-data%402x.png)

In this example, the file begins with the movie atom (`'moov'`), followed by the movie data atom (`'mdat'`). In order to overcome any latencies in sound playback, at least one second of sound data is placed at the beginning of the interleaved data. This means that the sound and video data are offset from each other in the file by one second.

## See Also

- [Movie atom ('moov')](movie_atom.md)
  An atom that specifies the information that defines a movie.
- [Movie header atom ('mvhd')](movie_header_atom.md)
  An atom that specifies the characteristics of an entire QuickTime movie.
- [Color table atom ('ctab')](color_table_atom.md)
  An atom that defines a list of preferred colors for displaying the movie on devices that support only 256 colors.
- [User data atoms](user_data_atoms.md)
  Atoms you use to define and store data associated with a QuickTime object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/interleaving_movie_data)*