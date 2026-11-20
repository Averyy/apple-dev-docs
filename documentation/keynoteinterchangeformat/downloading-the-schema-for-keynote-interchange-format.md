# Downloading the schema for Keynote Interchange Format

**Framework**: Keynote Interchange Format  
**Role**: Article  
**Download**: [keynote-interchange-format-json-schema.zip](https://developer.apple.com/download/files/keynote-interchange-format-json-schema.zip)

Get a machine-readable set of the JSON Schema files that define every type in Keynote Interchange Format.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Overview

Download a ZIP archive of the JSON Schema files for Keynote Interchange Format (`.keyx`) to help implement support for the file format in your tool, app, or AI agent. The files use [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12).

> ❗ **Important**: The JSON schemas are the authoritative definition of Keynote Interchange Format. Wherever this documentation disagrees with the schemas about a type’s shape, properties, defaults, or permitted values, defer to the schemas.

## Understand the schema structure

The archive contains one `<TypeName>.schema.json` file per type, for example, `Presentation.schema.json`, `Slide.schema.json`, and `CanvasObject.schema.json`. Each file defines one type, its type identifier, and the properties of which it’s made.

> **Note**: The schema only defines the structure of the JSON objects in Keynote Interchange Format. To learn more about how to create a valid keyx file, see [Understanding authoring requirements for Keynote Interchange Format](./understanding-authoring-requirements-for-keynote-interchange-format.md).

## See Also

### Authoring requirements
- [Understanding authoring requirements for Keynote Interchange Format](./understanding-authoring-requirements-for-keynote-interchange-format.md)
  Meet the requirements that a reader expects every Keynote Interchange Format document to satisfy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/downloading-the-schema-for-keynote-interchange-format)*