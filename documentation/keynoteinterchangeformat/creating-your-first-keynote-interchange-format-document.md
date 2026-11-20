# Creating your first Keynote Interchange Format document

**Framework**: Keynote Interchange Format  
**Role**: Article

Create a one-slide presentation with text, a shape, and an image.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Overview

Learn how to build a small presentation by hand, a few lines of JSON at a time, and open it in Keynote after each step to see the result. As part of the project, you write the three JSON files that a document can contain and add an image from the archive’s `Data/` directory.

You need a Mac with Keynote, a text editor, Terminal, and a JPEG image to place on the slide.

For background on the objects you write here, see [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md).

## Create a blank presentation

In Terminal, create a directory for the document’s contents:

```shell
mkdir MyPresentation
cd MyPresentation
```

In that directory, create a file named `main.json` with these contents:

```json
{
  "type_identifier" : "com.apple.apps.content-language.presentation",
  "theme" : {
    "type_identifier" : "com.apple.apps.content-language.keynote-theme",
    "name" : "White"
  },
  "slide_size" : {
    "type_identifier" : "com.apple.apps.content-language.size",
    "width" : 1920,
    "height" : 1080
  },
  "slides" : [
    {
      "type_identifier" : "com.apple.apps.content-language.slide",
      "identifier" : "slide-1",
      "contents" : [

      ]
    }
  ]
}
```

This is a presentation based on Keynote’s White theme, with one 1920 × 1080 slide that has nothing on it yet.

## Package and open the document

From inside the `MyPresentation` directory, create the archive and open it:

```shell
zip -X -r ../MyPresentation.keyx main.json
open ../MyPresentation.keyx
```

Run `zip` from inside the directory so that `main.json` is at the top level of the archive rather than inside a `MyPresentation` folder. The `-X` option leaves out macOS file attributes that the document doesn’t need.

![A screenshot of Keynote for Mac showing a blank presentation.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/creating-your-first-keynote-interchange-format-document-01@2x.png)

Keynote opens a presentation with one blank slide. Close it without saving before you continue.

## Add a title

Replace the empty `contents` array of the slide with this one, which places a text box near the top of the slide:

```json
"contents" : [
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
            "x" : 160,
            "y" : 120
          },
          "size" : {
            "type_identifier" : "com.apple.apps.content-language.size",
            "width" : 1600,
            "height" : 160
          }
        },
        "text" : {
          "type_identifier" : "com.apple.apps.content-language.text",
          "string" : "My First Presentation"
        }
      }
    }
  }
]
```

The entry wraps the text box in two layers: the slide object, which says that someone added it to the slide directly, and the canvas object, whose `textbox` key says what kind of object it is.

Package and open the document again, using the same commands as before. The slide shows the title in the White theme’s text box style.

![A screenshot of Keynote for Mac showing a presentation with a single text box.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/creating-your-first-keynote-interchange-format-document-02@2x.png)

## Add a colored shape

Add a second entry to the slide’s `contents` array, after the text box:

```json
{
  "type_identifier" : "com.apple.apps.content-language.slide-object",
  "source_kind" : "user",
  "object" : {
    "type_identifier" : "com.apple.apps.content-language.canvas-object",
    "shape" : {
      "type_identifier" : "com.apple.apps.content-language.shape",
      "geometry" : {
        "type_identifier" : "com.apple.apps.content-language.geometry",
        "position" : {
          "type_identifier" : "com.apple.apps.content-language.position",
          "x" : 160,
          "y" : 400
        },
        "size" : {
          "type_identifier" : "com.apple.apps.content-language.size",
          "width" : 400,
          "height" : 400
        }
      },
      "fill" : {
        "type_identifier" : "com.apple.apps.content-language.fill",
        "color" : {
          "type_identifier" : "com.apple.apps.content-language.color",
          "rgba" : {
            "type_identifier" : "com.apple.apps.content-language.color.rgba",
            "color_space" : "srgb",
            "red" : 0,
            "green" : 0.635,
            "blue" : 1,
            "alpha" : 1
          }
        }
      }
    }
  }
}
```

The shape has no `path`, so Keynote draws a rectangle the size of its geometry. Its `fill` takes the `color` form, and the color takes the `rgba` form, with each channel ranging from `0` to `1`.

Package and open the document. A blue square appears below the title, on the left.

![A screenshot of Keynote for Mac showing a presentation with a text box at the top and a blue shape at bottom left.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/creating-your-first-keynote-interchange-format-document-03@2x.png)

## Add an image

Create a directory named `Data` next to `main.json`, and copy a JPEG image into it with the name `photo.jpg`:

```shell
mkdir Data
cp ~/Pictures/example.jpg Data/photo.jpg
```

Replace `~/Pictures/example.jpg` with the path to your image.

Add a third entry to the slide’s `contents` array:

```json
{
  "type_identifier" : "com.apple.apps.content-language.slide-object",
  "source_kind" : "user",
  "object" : {
    "type_identifier" : "com.apple.apps.content-language.canvas-object",
    "image" : {
      "type_identifier" : "com.apple.apps.content-language.image",
      "geometry" : {
        "type_identifier" : "com.apple.apps.content-language.geometry",
        "position" : {
          "type_identifier" : "com.apple.apps.content-language.position",
          "x" : 760,
          "y" : 400
        },
        "size" : {
          "type_identifier" : "com.apple.apps.content-language.size",
          "width" : 1000,
          "height" : 560
        }
      },
      "resource" : {
        "type_identifier" : "com.apple.apps.content-language.resource",
        "indirect" : {
          "type_identifier" : "com.apple.apps.content-language.resource.indirect-resource",
          "filename" : "photo.jpg"
        }
      }
    }
  }
}
```

The image’s `resource` takes the `indirect` form, which names a file in the archive’s `Data/` directory. The name must match the file’s name exactly, including its case.

Include the `Data` directory when you package the document:

```shell
zip -X -r ../MyPresentation.keyx main.json Data
open ../MyPresentation.keyx
```

The image appears to the right of the square. If you see the slide without the image, check that the file in `Data/` is named exactly `photo.jpg`.

![A screenshot of Keynote for Mac showing a presentation with a text box at the top, a blue shape at bottom left, and at the bottom right, a photo of a large, dark yellow banana slug on the forest floor among leaf litter, twigs, and grasses.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/creating-your-first-keynote-interchange-format-document-04@2x.png)

## Add a manifest and presets

Create a file named `manifest.json` that declares the version of the format the document uses:

```json
{
  "package_version" : "1.0"
}
```

Then create a file named `presets.json` that contains an empty array:

```json
[

]
```

Writing both files lets a reader check the format version before it reads anything else, and tells it that the absence of presets is intentional.

Package the complete document:

```shell
zip -X -r ../MyPresentation.keyx main.json manifest.json presets.json Data
open ../MyPresentation.keyx
```

The presentation looks the same as before. The finished document has this structure:

![A diagram of the finished document, MyPresentation.keyx. The document contains main.json, manifest.json, and presets.json, followed by a directory named Data that contains an image file named photo.jpg.](https://developer.apple.com/tutorials/images/com.apple.KeynoteInterchangeFormat/creating-your-first-keynote-interchange-format-document-05@2x.png)

## Learn next steps

To style objects with reusable presets, place text in a layout’s placeholders, and group slides, see [Writing common presentation content](./writing-common-presentation-content.md). Before you write documents from your own tool, review [Understanding authoring requirements for Keynote Interchange Format](./understanding-authoring-requirements-for-keynote-interchange-format.md), which describes the rules a reader expects every document to follow and how to validate your files against the schema.

## See Also

### Essentials
- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)
  Trace how a presentation, its slides, and the objects on them fit together, and where each object gets its style.
- [Writing common presentation content](./writing-common-presentation-content.md)
  Structure a presentation and add common kinds of content to its slides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/creating-your-first-keynote-interchange-format-document)*