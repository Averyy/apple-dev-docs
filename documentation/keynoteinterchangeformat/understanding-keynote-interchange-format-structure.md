# Understanding Keynote Interchange Format structure

**Framework**: Keynote Interchange Format  
**Role**: Article

Trace how a presentation, its slides, and the objects on them fit together, and where each object gets its style.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Overview

A Keynote Interchange Format (`.keyx`) file describes a Keynote presentation as a tree of JSON objects. This format is a documented format for exchanging presentations with other tools, not the native format Keynote uses on disk. Keynote reads `.keyx` files and can export a presentation as one, so exporting an existing presentation is a good way to see how the format represents something you’ve built in Keynote.

This article describes the structure common to every document. Any software that consumes a `.keyx` file is called a *reader* in the format’s documentation. Keynote is one reader and your own tools can also be readers.

## Explore the files in a document

A `.keyx` file is a ZIP archive. At its top level, it contains up to three JSON files and a directory of media:

![A diagram of a document named MyPresentation.keyx. The document contains three JSON files, main.json, manifest.json, and presets.json, followed by a directory named Data that contains an image file named photo.jpg.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/understanding-keynote-interchange-format-structure-01@2x.png)

- **`main.json`**: The presentation itself: its theme, slide size, and slides. This is the only file a document requires.
- **`manifest.json`**: The version of Keynote Interchange Format that the document uses.
- **`presets.json`**: Reusable sets of properties that objects in `main.json` can adopt.
- **`Data/`**: Media files, such as images and movies, that objects in `main.json` refer to by name.

## Follow the presentation tree

The root object in `main.json` is a [`Presentation`](./presentation.md). A presentation holds an array of slides in presentation order, and each [`Slide`](./slide.md) holds an array of the objects on it, in its `contents` property. The objects are ordered back to front, so the first object in the array is the farthest back.

Each entry in a slide’s contents has two layers:

- **[`SlideObject`](./slideobject.md)**: The information that’s specific to the object’s place on this slide, such as whether it fills one of the layout’s placeholders and whether someone added it directly.
- **[`CanvasObject`](./canvasobject.md)**: The object itself: a text box, shape, image, movie, audio clip, table, chart, connection line, or group.

For example, the entry below places a text box on a slide:

```json
{
  "type_identifier" : "com.apple.apps.content-language.slide-object",
  "source_kind" : "user",
  "object" : {
    "type_identifier" : "com.apple.apps.content-language.canvas-object",
    "textbox" : {
      "type_identifier" : "com.apple.apps.content-language.textbox",
      "geometry" : {
        "type_identifier" : "com.apple.apps.content-language.geometry",
        "position" : {
          "type_identifier" : "com.apple.apps.content-language.position",
          "x" : 64,
          "y" : 200
        },
        "size" : {
          "type_identifier" : "com.apple.apps.content-language.size",
          "width" : 896,
          "height" : 100
        }
      },
      "text" : {
        "type_identifier" : "com.apple.apps.content-language.text",
        "string" : "Hello, World!"
      }
    }
  }
}
```

The outer object is the slide object, its `object` property holds the canvas object, and the canvas object’s single key, `textbox`, holds the text box’s own properties. Groups nest the same way: a [`Group`](./group.md) contains canvas objects in its `children`, and those can include further groups.

## Recognize values that take one of several forms

Many types in the format hold exactly one of several alternatives. You write these as a JSON object with a single key that names the alternative you chose, and that key holds the form’s contents. [`CanvasObject`](./canvasobject.md) is one of these types, which is why the text box above appears under a `textbox` key. Others you use often include:

| Type | Forms |
| --- | --- |
| [`Text`](./text.md) | `string`, `paragraphs`, or `text_runs` |
| [`Fill`](./fill.md) | `color`, `gradient`, or `image` |
| [`Resource`](./resource.md) | `indirect` or `base64_encoded` |
| [`Stroke`](./stroke.md) | `line`, `frame`, or `empty` |

The reference page for every type will list the valid forms for that type.

When a form carries no contents, you write just its name as a string. For example, a shape with no border has a stroke of `"empty"` rather than `{ "empty" : {} }`.

## Identify objects by type

Every object can carry a `type_identifier`, a reverse-DNS string such as `com.apple.apps.content-language.textbox` that names its type. A reader can usually work out an object’s type from where it appears, so the identifier is optional, but it is recommended that you write a `type_identifier`, because it makes a document self-describing and easier to debug. Each type identifier corresponds to a type in this reference and to a schema file in the downloadable JSON Schema archive.

## Base slides on a theme and its layouts

Every presentation has a [`KeynoteTheme`](./keynotetheme.md), which supplies the presentation’s slide layouts, its default styles, and its backgrounds. The theme is specified with the `theme` property. If the property is absent, or the named theme is missing, Keynote uses the default `White` theme.

A [`SlideLayout`](./slidelayout.md) is a template that slides share: it provides a background, a set of objects, and the placeholders a slide can turn on, such as the title and body. Each slide’s `layout` names the layout on which it’s based; a slide that doesn’t name one uses the theme’s first layout.

A slide object’s `source_kind` says why the object is on the slide:

- **`user`**: Someone added the object to the slide directly. This is the default.
- **`placeholder`**: The object fills one of the layout’s placeholders, which its `placeholder_info` identifies.
- **`layout`**: The object belongs to the slide’s layout.

A predefined placeholder is one of `title`, `body`, `object`, or `slide_number`. A slide lists a placeholder it has turned off too, so the presence of `placeholder_info` alone doesn’t mean a reader displays a placeholder; you set the `is_visible` property to control whether it appears on the slide.

## Style objects with presets

A [`Preset`](./preset.md) is a reusable, named set of properties. Declare presets in `presets.json`, and adopt them in an object by setting its `preset_identifier` to the preset’s identifier. A preset can name a parent with `parent_identifier`, and inherits any property it doesn’t set from that parent.

When a reader needs one of an object’s properties, it looks in this order and uses the first value it finds:

1. The object itself
2. The preset the object adopts
3. That preset’s parent, then the parent’s parent, and so on
4. The property’s declared default in the schema

For example, this preset gives shapes a blue fill:

```json
[
  {
    "identifier" : "blueShape",
    "display_name" : "Blue Shape",
    "properties" : {
      "fill" : {
        "type_identifier" : "com.apple.apps.content-language.fill",
        "color" : {
          "type_identifier" : "com.apple.apps.content-language.color",
          "rgba" : {
            "type_identifier" : "com.apple.apps.content-language.color.rgba",
            "color_space" : "srgb",
            "red" : 0,
            "green" : 0.478,
            "blue" : 1,
            "alpha" : 1
          }
        }
      }
    }
  }
]
```

A shape that sets `"preset_identifier" : "blueShape"` and writes no `fill` of its own is blue. A shape that adopts the same preset and writes its own `fill` uses that fill instead, and still inherits every other property the preset supplies.

The presentation’s `stylesheet` holds named styles, such as paragraph, character, and list styles. A few types look up their preset identifier in the stylesheet before `presets.json`, and their reference pages say so. When a presentation has no stylesheet, Keynote uses the theme’s styles.

## Turn off an inherited value

Leaving a property out of an object and setting it to `null` mean different things:

- **Omitting a property**: The reader looks up the value through the preset chain and falls back to the default, as described above.
- **Writing `null`**: The reader stops looking and treats the property as having no value. This is the only way to turn off a value the object otherwise inherits.

For example, if a shape’s preset gives it a shadow, writing `"shadow" : null` on the shape removes the shadow from that shape alone. A `null` in a preset works the same way for every object that adopts the preset.

Consult the property’s schema to see whether `null` is one of its permitted values.

## Store media as resources

Images, movies, audio, image fills, and image bullets get their data from a [`Resource`](./resource.md), which takes one of two forms:

- **`indirect`**: The data is in a file in the archive’s `Data/` directory.
- **`base64_encoded`**: The data is a Base64 string inside the resource itself.

Use `base64_encoded` to keep the `main.json` self-contained; use `indirect` to reduce the size of the archive.

## Interpret numeric values

Unless a property’s documentation says otherwise, every type uses these conventions:

| Quantity | Convention |
| --- | --- |
| Lengths, such as positions, sizes, indents, font sizes, and stroke widths | Points, at 72 to the inch. |
| Origin | The top-left corner of the containing space: a slide, an image, or a mask. |
| Vertical axis | Increases downward. |
| Rotation | Degrees, counterclockwise, about the center of the unrotated bounding box. |
| Color channels and opacities | 0 to 1 inclusive. |

Some numeric properties use other units; consult their schema to understand their meaning. For example, character spacing is a fraction of the font’s em (a unit equal to the specified point size), and a gutter is a percentage of the layout width.

## Distinguish the two kinds of version

The format tracks versions at two levels:

- **Package version**: The version of Keynote Interchange Format that a whole document uses, written in `manifest.json`. A reader checks it before decoding anything else.
- **Type version**: The version of an individual type, written in an object’s optional `version` property. When the meaning of a type changes, such as when it gains members, its version increases. An object without a version is read at the latest version of its type that the reader supports.

Both use major.minor format, and most types are currently at version 1.0.

## See Also

### Related Documentation
- [Creating your first Keynote Interchange Format document](./creating-your-first-keynote-interchange-format-document.md)
  Create a one-slide presentation with text, a shape, and an image.
- [Understanding authoring requirements for Keynote Interchange Format](./understanding-authoring-requirements-for-keynote-interchange-format.md)
  Meet the requirements that a reader expects every Keynote Interchange Format document to satisfy.
### Essentials
- [Creating your first Keynote Interchange Format document](./creating-your-first-keynote-interchange-format-document.md)
  Create a one-slide presentation with text, a shape, and an image.
- [Writing common presentation content](./writing-common-presentation-content.md)
  Structure a presentation and add common kinds of content to its slides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/understanding-keynote-interchange-format-structure)*