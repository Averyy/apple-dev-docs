# CanvasObject

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The identity, placement, and accessibility properties shared by objects you can place on a slide, in a group, or inline in text.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(CanvasObject.audio | CanvasObject.chart | CanvasObject.connectionLine | CanvasObject.group | CanvasObject.image | CanvasObject.movie | CanvasObject.shape | CanvasObject.table | CanvasObject.textbox) CanvasObject
```

## Mentions

- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)



**Allowed Types**: `CanvasObject.audio`, `CanvasObject.chart`, `CanvasObject.connectionLine`, `CanvasObject.group`, `CanvasObject.image`, `CanvasObject.movie`, `CanvasObject.shape`, `CanvasObject.table`, `CanvasObject.textbox`

## Discussion

When authoring a Keynote Interchange Format document, you don’t create these directly, but instead create objects with the `type_identifier` that include these same properties directly rather than under a key of their own. The same name is also the type that holds any one of those objects, which is what `SlideObject.object`, `Group.children`, and a paragraph’s inline object contain.

This value takes one of the following forms:

- `audio`: A sound attached to a slide. An audio object has no visible size of its own; it appears as a fixed-size icon, so Keynote ignores the size in `geometry` and only uses the position.
- `chart`: An object that plots a grid of data in a visual style such as column, pie, or scatter. Write a chart as an object with a single key, which names its chart type, such as `column` or `pie`, and holds that type’s settings. The chart type decides only how Keynote plots the series: every chart type uses the same chart data, so when you change a chart’s type, that change replots the existing series without rewriting the data.
- `connectionLine`: A line drawn from its tail end to its head end, each of which can attach to another object. The route comes from `tail`, `head`, and (for a curved or corner line) the control position carried by `line_type`. Because the line’s position and size follow from the route, `geometry` only transforms the supplied end points and control position, and is omitted when Keynote writes out a connection line.
- `group`: An ordered set of objects that behave as one when selected, moved, or transformed. The group’s position and size are those of the smallest rectangle enclosing its children, so the reader uses only the rotation and flip from its `geometry`.
- `image`: A picture defined by a resource with optional styling. When `geometry` is absent, the reader places the image at the natural size of `resource`. When Keynote exports a presentation, it writes an object the format has no type for as an image. A 3D object, a drawing, an image gallery, a web video, a live video, or a comment on a slide becomes a picture of the object as it appears, with its rotation, flip, title, and caption drawn in, so the image has no `title` or `caption`, and its `geometry` is an unrotated rectangle enclosing the whole picture, including any shadow or reflection. Keynote also writes such an image without a `description`, so the object’s accessibility description is lost. A comment appears in its image only if comments are shown when someone exports the presentation; otherwise the image is empty.
- `movie`: A movie or animated image defined by a resource with optional styling. When `geometry` is omitted, the object takes the resource’s natural size, falling back to 640 × 480 points when the reader cannot measure that size. Placed inline in the text of a text box or shape, an unplayable movie removes that whole text box or shape, including all of its text; in a slide’s presenter notes, it stops the document from loading.
- `shape`: A path with a fill and a stroke. When `geometry` is absent, the geometry defaults to the smallest rectangle that encloses the path. Shapes can have an open or a closed path; a path is *open* when it has a single subpath, no `closepath` command, and ends that don’t meet. Open shapes can have endpoints, `head` and `tail`. Keynote reads a `path` that is a single, straight, open segment as a line and takes its styling from the line presets. A shape with either `Geometry.width_valid` or `Geometry.height_valid` set to `false` becomes an auto-sizing text box. Paths that aren’t straight lines can contain text that appears inside the shape.
- `table`: A table of cells, nested two levels deep. `content` holds the table’s rows, ordered top to bottom, and each row’s `cells` holds that row’s cells, ordered left to right. The first `number_of_header_rows` rows are header rows, and the last `number_of_footer_rows` are footer rows. Rows and cells that carry nothing may be omitted, so `Table.Row.row_index` and `Table.Cell.column_index` mark where a run resumes after a gap. On a slide, a table whose `title` is absent, has no text, or reads `Unnamed` or `Unnamed Table` gets a default name such as Table `1` as its built-in title, and Keynote renames tables there that share a name the same way until each has its own; which of them keeps the name isn’t defined, and Keynote reports no warning.
- `textbox`: A container for text that someone places directly on a slide or slide layout. It takes its typography and background from the text-box presets rather than the shape presets. A `shape` can hold text too.

## Topics

### Dictionaries
- [object CanvasObject.audio](./canvasobject/audio.md)
  A sound attached to a slide.
- [object CanvasObject.chart](./canvasobject/chart.md)
  An object that plots a grid of data in a visual style such as column, pie, or scatter.
- [object CanvasObject.connectionLine](./canvasobject/connectionline.md)
  A line drawn from its tail end to its head end, each of which can attach to another object.
- [object CanvasObject.group](./canvasobject/group.md)
  An ordered set of objects that behave as one when selected, moved, or transformed.
- [object CanvasObject.image](./canvasobject/image.md)
  A picture defined by a resource with optional styling.
- [object CanvasObject.movie](./canvasobject/movie.md)
  A movie or animated image defined by a resource with optional styling.
- [object CanvasObject.shape](./canvasobject/shape.md)
  A path with a fill and a stroke.
- [object CanvasObject.table](./canvasobject/table.md)
  A table of cells, nested two levels deep.
- [object CanvasObject.textbox](./canvasobject/textbox.md)
  A container for text that someone places directly on a slide or slide layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/canvasobject)*