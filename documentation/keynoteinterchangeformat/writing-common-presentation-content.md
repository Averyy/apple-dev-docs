# Writing common presentation content

**Framework**: Keynote Interchange Format  
**Role**: Article

Structure a presentation and add common kinds of content to its slides.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Overview

Each example in this article shows the JSON for one common task. Examples that structure a whole presentation are complete `main.json` files. Examples that add content to a slide are entries that you add to a slide’s `contents` array, or, where noted, a part of one.

The examples write a `type_identifier` on every object and order each object’s members alphabetically, the way Keynote does when it exports a presentation. Neither is required: type identifiers are optional where a reader can infer the type, and member order carries no meaning.

To package an example and open it in Keynote, follow the steps in [Creating your first Keynote Interchange Format document](./creating-your-first-keynote-interchange-format-document.md). For an explanation of the objects in these examples, see [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md).

## Create the smallest valid document

This `main.json` is the smallest document that loads: one blank slide in the default theme. The document has no `manifest.json`, no `presets.json`, and no `Data/` directory.

```json
{
  "slide_size" : {
    "height" : 768,
    "type_identifier" : "com.apple.apps.content-language.size",
    "width" : 1024
  },
  "slides" : [
    {
      "contents" : [

      ],
      "identifier" : "slide-1",
      "type_identifier" : "com.apple.apps.content-language.slide"
    }
  ],
  "type_identifier" : "com.apple.apps.content-language.presentation"
}
```

## Group slides and add presenter notes

The slide navigator groups slides by each slide’s `depth`, not by nesting arrays. A slide with a greater depth than the slide before it becomes that slide’s child. In this `main.json`, the second slide is a child of the first, and the third slide returns to the top level. The second slide also has presenter notes, in its `note` property.

```json
{
  "slide_size" : {
    "height" : 1080,
    "type_identifier" : "com.apple.apps.content-language.size",
    "width" : 1920
  },
  "slides" : [
    {
      "contents" : [

      ],
      "depth" : 1,
      "identifier" : "intro",
      "type_identifier" : "com.apple.apps.content-language.slide"
    },
    {
      "contents" : [

      ],
      "depth" : 2,
      "identifier" : "details",
      "note" : {
        "string" : "Talk about details here.",
        "type_identifier" : "com.apple.apps.content-language.text"
      },
      "type_identifier" : "com.apple.apps.content-language.slide"
    },
    {
      "contents" : [

      ],
      "depth" : 1,
      "identifier" : "summary",
      "type_identifier" : "com.apple.apps.content-language.slide"
    }
  ],
  "type_identifier" : "com.apple.apps.content-language.presentation"
}
```

![A screenshot of Keynote for Mac showing a presentation with three slides. The second slide is indented beneath the first slide, and presenter notes are visible.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/writing-common-presentation-content-01@2x.png)

## Add a text box with several paragraphs

This slide-contents entry places a text box with two paragraphs on a slide. The text takes the `paragraphs` form, which holds an array of paragraphs. Each paragraph’s `contents` holds runs of text, and each run has a single character style. In the second paragraph, the middle run is bold, so the paragraph splits into three runs where the style changes.

For text in a single style, the `string` form is simpler: write `"text" : { "string" : "Quarterly results" }`. For an example, see [Creating your first Keynote Interchange Format document](./creating-your-first-keynote-interchange-format-document.md).

```json
{
  "object" : {
    "textbox" : {
      "geometry" : {
        "position" : {
          "type_identifier" : "com.apple.apps.content-language.position",
          "x" : 64,
          "y" : 200
        },
        "size" : {
          "height" : 200,
          "type_identifier" : "com.apple.apps.content-language.size",
          "width" : 896
        },
        "type_identifier" : "com.apple.apps.content-language.geometry"
      },
      "text" : {
        "paragraphs" : [
          {
            "contents" : [
              {
                "run" : {
                  "string" : "Quarterly results",
                  "type_identifier" : "com.apple.apps.content-language.text-run"
                },
                "type_identifier" : "com.apple.apps.content-language.paragraph.constituent"
              }
            ],
            "type_identifier" : "com.apple.apps.content-language.paragraph"
          },
          {
            "contents" : [
              {
                "run" : {
                  "string" : "Revenue grew ",
                  "type_identifier" : "com.apple.apps.content-language.text-run"
                },
                "type_identifier" : "com.apple.apps.content-language.paragraph.constituent"
              },
              {
                "run" : {
                  "string" : "12 percent",
                  "style" : {
                    "bold" : true,
                    "type_identifier" : "com.apple.apps.content-language.character-properties"
                  },
                  "type_identifier" : "com.apple.apps.content-language.text-run"
                },
                "type_identifier" : "com.apple.apps.content-language.paragraph.constituent"
              },
              {
                "run" : {
                  "string" : " over the previous quarter.",
                  "type_identifier" : "com.apple.apps.content-language.text-run"
                },
                "type_identifier" : "com.apple.apps.content-language.paragraph.constituent"
              }
            ],
            "type_identifier" : "com.apple.apps.content-language.paragraph"
          }
        ],
        "type_identifier" : "com.apple.apps.content-language.text"
      },
      "type_identifier" : "com.apple.apps.content-language.textbox"
    },
    "type_identifier" : "com.apple.apps.content-language.canvas-object"
  },
  "source_kind" : "user",
  "type_identifier" : "com.apple.apps.content-language.slide-object"
}
```

![A screenshot of Keynote for Mac showing a presentation containing a text box with two paragraphs of text. Some words in the second paragraph are styled with bold type.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/writing-common-presentation-content-02@2x.png)

## Fill a layout’s title placeholder

This slide-contents entry fills a layout placeholder with a text box. The text box the same structure as any other, plus the `placeholder_info` that identifies the layout placeholder it fills, with visibility turned on, and a `source_kind` of `placeholder`.

```json
{
  "object" : {
    "textbox" : {
      "geometry" : {
        "position" : {
          "type_identifier" : "com.apple.apps.content-language.position",
          "x" : 64,
          "y" : 64
        },
        "size" : {
          "height" : 120,
          "type_identifier" : "com.apple.apps.content-language.size",
          "width" : 896
        },
        "type_identifier" : "com.apple.apps.content-language.geometry"
      },
      "text" : {
        "string" : "Title",
        "type_identifier" : "com.apple.apps.content-language.text"
      },
      "type_identifier" : "com.apple.apps.content-language.textbox"
    },
    "type_identifier" : "com.apple.apps.content-language.canvas-object"
  },
  "placeholder_info" : {
    "defined" : {
      "is_visible" : true,
      "kind" : "title",
      "type_identifier" : "com.apple.apps.content-language.slide-object.placeholder-info.placeholder-definition"
    },
    "type_identifier" : "com.apple.apps.content-language.slide-object.placeholder-info"
  },
  "source_kind" : "placeholder",
  "type_identifier" : "com.apple.apps.content-language.slide-object"
}
```

![A screenshot of Keynote for Mac showing a presentation containing a text box. The slide’s Format inspector is shown and the Title placeholder checkbox is checked.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/writing-common-presentation-content-03@2x.png)

## Place an image from the data directory

This slide-contents entry places an image whose data is in a file in the archive’s `Data/` directory:

![A diagram of a document named MyPresentation.keyx that contains main.json and a directory named Data. The diagram highlights the Data directory, which contains an image file named photo.jpg.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/writing-common-presentation-content-04@2x.png)

Use the resource’s `indirect` form to refer to a file in `Data/` by name. The name must match an entry directly inside `Data/` exactly, including its case, and it can’t contain a path separator.

```json
{
  "object" : {
    "image" : {
      "geometry" : {
        "position" : {
          "type_identifier" : "com.apple.apps.content-language.position",
          "x" : 100,
          "y" : 100
        },
        "size" : {
          "height" : 336,
          "type_identifier" : "com.apple.apps.content-language.size",
          "width" : 600
        },
        "type_identifier" : "com.apple.apps.content-language.geometry"
      },
      "resource" : {
        "indirect" : {
          "filename" : "photo.jpg",
          "type_identifier" : "com.apple.apps.content-language.resource.indirect-resource"
        },
        "type_identifier" : "com.apple.apps.content-language.resource"
      },
      "type_identifier" : "com.apple.apps.content-language.image"
    },
    "type_identifier" : "com.apple.apps.content-language.canvas-object"
  },
  "source_kind" : "user",
  "type_identifier" : "com.apple.apps.content-language.slide-object"
}
```

![A screenshot of Keynote for Mac showing a presentation containing a photo of a large, dark yellow banana slug on the forest floor among leaf litter, twigs, and grasses.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/writing-common-presentation-content-05@2x.png)

The example writes only a `filename`, so a reader looks for `Data/photo.jpg`. To store the file under a different name from the one Keynote shows, such as a name your tool generates, write the file’s name in `identifier` as well. This `resource` value tells a reader to load `Data/3F2A9C.jpg` and show the name `Beach.jpg`:

```json
{
  "indirect" : {
    "filename" : "Beach.jpg",
    "identifier" : "3F2A9C.jpg",
    "type_identifier" : "com.apple.apps.content-language.resource.indirect-resource"
  },
  "type_identifier" : "com.apple.apps.content-language.resource"
}
```

![A screenshot of Keynote for Mac showing a presentation containing a photo of seaweed-covered rocks and small tidal pools with the sun setting in the sky behind them. The Image inspector shows that the image is named Beach.jpg.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/writing-common-presentation-content-06@2x.png)

## Embed an image in the JSON

This slide-contents entry carries the image’s data in the JSON itself, so the document needs no `Data/` directory. The resource takes the `base64_encoded` form: `string` holds the file’s bytes in Base64, and `filename` gives the name Keynote shows for the image, including the extension that identifies its format. For brevity, the data in this example is a 1 × 1 pixel PNG image.

```json
{
  "object" : {
    "image" : {
      "geometry" : {
        "position" : {
          "type_identifier" : "com.apple.apps.content-language.position",
          "x" : 100,
          "y" : 100
        },
        "size" : {
          "height" : 300,
          "type_identifier" : "com.apple.apps.content-language.size",
          "width" : 400
        },
        "type_identifier" : "com.apple.apps.content-language.geometry"
      },
      "resource" : {
        "base64_encoded" : {
          "filename" : "pixel.png",
          "string" : "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==",
          "type_identifier" : "com.apple.apps.content-language.resource.base64-encoded-resource"
        },
        "type_identifier" : "com.apple.apps.content-language.resource"
      },
      "type_identifier" : "com.apple.apps.content-language.image"
    },
    "type_identifier" : "com.apple.apps.content-language.canvas-object"
  },
  "source_kind" : "user",
  "type_identifier" : "com.apple.apps.content-language.slide-object"
}
```

![A screenshot of Keynote for Mac showing a presentation containing an image of a lavender rectangle.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/writing-common-presentation-content-07@2x.png)

## Style shapes with a preset

This example declares a preset that gives shapes a blue fill, and two shapes that adopt it. The first shape writes no fill of its own, so it inherits the preset’s blue. The second shape writes its own fill, which takes precedence, so it’s orange; it still inherits any other property the preset supplies.

An identifier that matches no preset isn’t an error: the properties the preset would have supplied fall back to their declared defaults.

Write this to `presets.json`:

```json
[
  {
    "display_name" : "Blue Shape",
    "identifier" : "blueShape",
    "properties" : {
      "fill" : {
        "color" : {
          "rgba" : {
            "alpha" : 1,
            "blue" : 1,
            "color_space" : "srgb",
            "green" : 0.478,
            "red" : 0,
            "type_identifier" : "com.apple.apps.content-language.color.rgba"
          },
          "type_identifier" : "com.apple.apps.content-language.color"
        },
        "type_identifier" : "com.apple.apps.content-language.fill"
      }
    }
  }
]
```

Add this entry, which adopts the preset and inherits its fill, to a slide’s `contents` array in `main.json`:

```json
{
  "object" : {
    "shape" : {
      "geometry" : {
        "position" : {
          "type_identifier" : "com.apple.apps.content-language.position",
          "x" : 100,
          "y" : 400
        },
        "size" : {
          "height" : 200,
          "type_identifier" : "com.apple.apps.content-language.size",
          "width" : 200
        },
        "type_identifier" : "com.apple.apps.content-language.geometry"
      },
      "preset_identifier" : "blueShape",
      "type_identifier" : "com.apple.apps.content-language.shape"
    },
    "type_identifier" : "com.apple.apps.content-language.canvas-object"
  },
  "source_kind" : "user",
  "type_identifier" : "com.apple.apps.content-language.slide-object"
}
```

Then add this entry, which adopts the same preset and overrides its fill:

```json
{
  "object" : {
    "shape" : {
      "fill" : {
        "color" : {
          "rgba" : {
            "alpha" : 1,
            "blue" : 0,
            "color_space" : "srgb",
            "green" : 0.584,
            "red" : 1,
            "type_identifier" : "com.apple.apps.content-language.color.rgba"
          },
          "type_identifier" : "com.apple.apps.content-language.color"
        },
        "type_identifier" : "com.apple.apps.content-language.fill"
      },
      "geometry" : {
        "position" : {
          "type_identifier" : "com.apple.apps.content-language.position",
          "x" : 400,
          "y" : 400
        },
        "size" : {
          "height" : 200,
          "type_identifier" : "com.apple.apps.content-language.size",
          "width" : 200
        },
        "type_identifier" : "com.apple.apps.content-language.geometry"
      },
      "preset_identifier" : "blueShape",
      "type_identifier" : "com.apple.apps.content-language.shape"
    },
    "type_identifier" : "com.apple.apps.content-language.canvas-object"
  },
  "source_kind" : "user",
  "type_identifier" : "com.apple.apps.content-language.slide-object"
}
```

![A screenshot of Keynote for Mac showing two rectangles. The rectangle on the left is blue, and the rectangle on the right is orange.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/writing-common-presentation-content-08@2x.png)

## See Also

### Essentials
- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)
  Trace how a presentation, its slides, and the objects on them fit together, and where each object gets its style.
- [Creating your first Keynote Interchange Format document](./creating-your-first-keynote-interchange-format-document.md)
  Create a one-slide presentation with text, a shape, and an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/writing-common-presentation-content)*