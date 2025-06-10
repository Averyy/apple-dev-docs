# Authoring movies with external movie targets

**Framework**: QuickTime File Format

Specify elements of an external movie in your movie.

#### Overview

QuickTime 4 enables you to author movies with external movie targets. To specify an action that targets an element of an external movie, you must identify the external movie by either its name or its ID. Two new target atom types have been introduced for this purpose; these atoms are used in addition to the existing target atoms, which you may use to specify that the element is a particular track or object within a track, such as a sprite.

> **Note**: A movie ID may be specified by an expression.

These additional target atoms provided in QuickTime 4:

```c
[(ActionTargetAtoms)] =
    <kActionTarget>
 
        <kTargetMovieName>
            [Pstring MovieName]
        OR
        <kTargetMovieID>
            [long MovieID]
            OR
            [(kExpressionAtoms)]
```

To tag a movie with a name or ID, you add a user data item of type `'plug'` to the movie’s user data. The index of the user data does not matter. The data specifies the name or ID.

You add a user data item of type `'plug'` to the movie’s user data with its data set to

```c
"Movieid=MovieName"
```

where `MovieName` is the name of the movie.

You add a user data item of type `'plug'` to the movie’s user data with its data set to

```c
"Movieid=MovieID"
```

where the ID is a signed long integer.

The QuickTime plug-in additionally supports `EMBED` tag parameters, which allow you to override a movie’s name or ID within an HTML page.

#### Target Atoms for Embedded Movies

QuickTime 4.1 introduced target atoms to accommodate the addition of embedded movies. These target atoms allow for paths to be specified in a hierarchical movie tree.

Target movies may be an external movie, the default movie, or any movie embedded within another movie. Targets are specified by using a movie path that may include parent and child movie relationships, and may additionally include track and track object target atoms as needed.

By using embedded `kActionTarget` atoms along with parent and child movie target atoms, you can build up paths for movie targets. Note that QuickTime looks for these embedded `kActionTarget` atoms only when evaluating a movie target, and any movie target type may contain a sibling `kActionTarget` atom.

Paths begin from the current movie, which is the movie containing the object that is handling an event. You may go up the tree using a `kTargetParentMovie` atom, or down the tree using one of five new child movie atoms. You may use a `kTargetRootMovie` atom as a shortcut to get to the top of the tree containing an embedded movie and may use the `movieByName` and `movieByID` atoms to specify a root external movie.

The target atoms are:

- `kTargetRootMovie` (leaf atom, no data). This is the root movie containing the action handler.
- `kTargetParentMovie` (leaf atom, no data). This is the parent movie.

Note that there are five ways to specify an embedded child movie. Three of them specify movie track properties. Two specify properties of the currently loaded movie in a movie track.

- `kTargetChildMovieTrackName`. A child movie track specified by track name.
- `kTargetChildMovieTrackID`. A child movie track specified by track ID.
- `kTargetChildMovieTrackIndex`. A child movie track specified by track index.
- `kTargetChildMovieMovieName`. A child movie specified by the currently loaded movie’s movie name. The child movie must contain movieName user data with the specified name.
- `kTargetChildMovieMovieID`. A child movie specified by the currently loaded movie’s movie ID. The child movie must contain movieID user data with the specified ID.

## See Also

- [Compressed movie resources](compressed_movie_resources.md)
  Reduce file size and startup latency by compressing movie resources.
- [Reference movies](reference_movies.md)
  A movie that contains references to alternate movies is called a reference movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/authoring_movies_with_external_movie_targets)*