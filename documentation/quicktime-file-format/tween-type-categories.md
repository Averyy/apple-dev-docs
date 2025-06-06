# Tween type categories

**Framework**: QuickTime File Format

#### Overview

Each of the tween types supported by QuickTime belongs to one of these categories:

- Numeric tween types, which have pairs of numeric values, such as long integers, as input. For these types, linear interpolation is used to generate output values.
- QuickDraw tween types, most of which have pairs of QuickDraw structures, such as points or rectangles, as input. For these types, one or more structure elements are interpolated, such as the h and v values for points, and each element that is interpolated is interpolated separately from others.
- 3D tween types, which have a QuickDraw 3D structure such as `TQ3Matrix4x4` or `TQ3RotateAboutAxisTransformData` as input. For these types, a specific 3D transformation is performed on the data to generate output.
- The polygon tween type, which takes three four-sided polygons as input. One polygon (such as the bounds for a sprite or track) is transformed, and the two others specify the start and end of the range of polygons into which the tween operation maps it. You can use the output (a `MatrixRecord` data structure) to map the source polygon into any intermediate polygon. The intermediate polygon is interpolated from the start and end polygons for each particular time in the tween duration.
- Path tween types, which have as input a QuickTime vector data stream for a path. Four of the path tween types also have as input a percentage of path’s length; for these types, either a point on the path or a data structure is returned. Two other path tween types treat the path as a function: one returns the `y` value of the point on the path with a given `x` value, and the other returns the `x` value of the point on the path with a given `y` value.
- The list tween type, which has as input a QT atom container that contains leaf atoms of a specified atom type. For this tween type category, the duration of the tween operation is divided by the number of leaf atoms of the specified type. For time points within the first time division, the data for the first leaf atom is returned; for the second time division, the data for the second leaf atom is returned; and so on. The resulting tween operation proceeds in discrete steps (one step for each leaf atom), instead of the relatively continuous tweening produced by other tween type categories.

## See Also

- [Tween sample description](tween_sample_description.md)
  An atom that contains information for converting from media time to sample number to sample location for tweens.
- [Tween sample data](tween_sample_data.md)
- [Tween QT atom container](tween_qt_atom_container.md)
  Specify the characteristics of a tween with atoms in a tween QT atom container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/tween_type_categories)*