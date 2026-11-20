# Understanding authoring requirements for Keynote Interchange Format

**Framework**: Keynote Interchange Format  
**Role**: Article

Meet the requirements that a reader expects every Keynote Interchange Format document to satisfy.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Overview

Learn the rules for writing a Keynote Interchange Format (`.keyx`) document so a reader can load as it as you intend. This article assumes familiarity with the structure of a document, as described in [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md).

The JSON Schema files define the shape of every type: the properties it contains, which properties are required, their defaults, and the values each permits. This article covers only what a schema can’t state. For how to get the schema, see [Downloading the schema for Keynote Interchange Format](./downloading-the-schema-for-keynote-interchange-format.md).

In the rules below, *must* and *must not* mark requirements, and the remaining rules are recommendations.

## Write valid JSON

- You must write a document that parses under [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259).
- You must write all JSON text as UTF-8. You can escape non-ASCII characters or write them raw.
- You must not repeat a member name within one object. This is the one condition in the format whose handling is undefined, so the resulting document has no meaning.
- You must write Booleans as the JSON literals `true` and `false`, not as strings.
- You can write an object’s members in any order. Member order carries no meaning.
- You can pretty-print. Whitespace between tokens carries no meaning.
- You can write an integer-typed value in decimal form, for example, with a trailing zero, as long as it has no fractional part. A fractional value where the schema expects an integer isn’t valid.

JSON has no comments, so a document can’t contain them.

## Create the archive

The container is a standard ZIP archive, as the [PKWARE APPNOTE](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT) describes.

- You must write a valid ZIP archive containing `main.json`.
- You must write every entry name in the archive as UTF-8.
- You can write either stored or deflated entries in the archive.
- You must write each entry name exactly as this documentation gives it. A reader matches entry names case-sensitively.
- You must store the data for each indirectly referenced resource as a file directly inside the archive’s `Data/` directory, named with the resource’s `identifier`. If the resource has no `identifier`, a reader uses its `filename` as the name instead.
- You must not include a path separator in the name. A reader looks for the file by an exact, case-sensitive match against the entries directly inside `Data/`, so it doesn’t find a file you place in a subdirectory.

## Write required and usable values

- You must write every property that the schema marks as required for an object’s type.
- You must write a real, usable value wherever the schema describes one. A value that satisfies the schema but that a reader can’t interpret, such as an ill-formed path string or embedded resource data that isn’t valid Base64, isn’t conforming. A reader usually doesn’t repair an invalid value, but drops the object that contains the value.
- When a schema offers more than one encoding for the same content, write the form that readers of your target version can resolve. Valid content for a wrong version may be ignored or used incorrectly. The schema notes which encodings are valid for which versions.
- Write an empty array rather than omitting a required array property.
- When a property takes one of several named forms and the form you write has no contents, write just its name as a string instead of using an object.
- Write the type identifier on every non-primitive object. A reader infers an object’s type from its context when the identifier is absent, but at the top level of a file there’s no surrounding context to infer from.

> **Note**: The Keynote Interchange Format defines `required` narrowly to mean a property that must be present for the object to be valid. Any property that has a default is not marked required.

## Write nulls only where you mean them

- You must write `null` only for a property whose schema permits it.
- In particular, you must not write `null` in place of a required property. A `null` is a value, so it doesn’t satisfy the requirement, and it doesn’t invite a default either.
- Write `null` only to turn off a value that the object would otherwise inherit. To accept the inherited value, omit the property instead. A `null` in a preset clears the property for every object that adopts the preset, and stops the search for a value; a preset that omits the property defers to its own parent, and then to the default.

For more info about the use of `null` values, see [Style objects with presets](./understanding-keynote-interchange-format-structure.md#Style-objects-with-presets) and [Turn off an inherited value](./understanding-keynote-interchange-format-structure.md#Turn-off-an-inherited-value).

## Write unique object identifiers

- You must make each object identifier you write unique across the whole document.

> **Note**: A duplicate object identifier doesn’t stop the document from loading, but only one of the objects can be referred to by that identifier, so you lose an object without any report.

## Declare presets

- You must give each preset a unique identifier. A duplicate preset identifier stops the document from loading when it is inside `presets.json`.
- You must not create a cycle in your presets’ parent references.
- Write `presets.json` even when it’s empty. It isn’t required, but an empty `presets.json` saves a reader from deciding whether a missing one was intentional.

## Declare versions

- Write `manifest.json`. It isn’t required, but writing the package version lets a reader reject a file it can’t read before decoding any of it.
- You must write a package version as two non-negative integers separated by a period. A reader treats a malformed package version as absent. A reader will usually read any document with the same major version it supports.
- You can omit an object’s `version`; when it is not present, a reader reads an object at the latest version of its type that it supports. The schema for each type gives the type’s latest version as the default.

## Express lengths and coordinates

Express lengths in points and use the format’s coordinate conventions, except where a property’s documentation says otherwise. For the conventions, see [Interpret numeric values](./understanding-keynote-interchange-format-structure.md#Interpret-numeric-values).

## Validate what you write

Extract `main.json` from the archive and validate it against the presentation schema using any conforming [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12) validator. Validate `manifest.json` against the manifest schema, and each preset in `presets.json` against the preset schema, the same way.

Validation establishes that the structure is correct. A conforming validator neither checks a default nor fills one in, so validation doesn’t cover defaults, and two other classes of requirement remain outside it:

- **Values that drop an object or stop the document from loading**: A reader degrades or drops most unusable values, and the document still loads. A value that isn’t usable, as described in [Write required and usable values](./understanding-authoring-requirements-for-keynote-interchange-format.md#Write-required-and-usable-values), usually makes a reader drop the object that contains it. In some cases, such as a named style or in a slide’s presenter notes, an unusable value can stop the document from loading.
- **References between files**: Validating one file in isolation can’t check a reference that resolves against another file, or against the theme the document names rather than the document itself.

## See Also

### Authoring requirements
- [Downloading the schema for Keynote Interchange Format](./downloading-the-schema-for-keynote-interchange-format.md)
  Get a machine-readable set of the JSON Schema files that define every type in Keynote Interchange Format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/understanding-authoring-requirements-for-keynote-interchange-format)*