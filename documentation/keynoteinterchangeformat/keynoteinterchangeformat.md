# Keynote Interchange Format

**Framework**: Keynote Interchange Format  
**Kind**: module  
**Role**: Technology

Read and write Keynote presentations using a JSON-based file format.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Overview

Use the Keynote Interchange Format to represent a Keynote presentation as a ZIP archive of JSON files and media assets, with the filename extension `.keyx`. This format facilitates interchange with external tools, scripts, and AI agents that need to read or write Keynote presentations programmatically.

## Topics

### Essentials
- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)
  Trace how a presentation, its slides, and the objects on them fit together, and where each object gets its style.
- [Creating your first Keynote Interchange Format document](./creating-your-first-keynote-interchange-format-document.md)
  Create a one-slide presentation with text, a shape, and an image.
- [Writing common presentation content](./writing-common-presentation-content.md)
  Structure a presentation and add common kinds of content to its slides.
### Authoring requirements
- [Understanding authoring requirements for Keynote Interchange Format](./understanding-authoring-requirements-for-keynote-interchange-format.md)
  Meet the requirements that a reader expects every Keynote Interchange Format document to satisfy.
- [Downloading the schema for Keynote Interchange Format](./downloading-the-schema-for-keynote-interchange-format.md)
  Get a machine-readable set of the JSON Schema files that define every type in Keynote Interchange Format.
### File format
- [object Presentation](./presentation.md)
  A document’s root object, which describes one Keynote presentation.
- [object Manifest](./manifest.md)
  An object that declares which version of Keynote Interchange Format a .keyx file uses.
- [object Preset](./preset.md)
  A reusable, named set of properties that other objects inherit.
### Release notes
- [Keynote Interchange Format release notes](./keynote-interchange-format-release-notes.md)
  Review the Keynote features that each version of Keynote Interchange Format supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat)*